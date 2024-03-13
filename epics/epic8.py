from pyspark.sql import SparkSession
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import struct, col, collect_list, udf, lit, array
from typing import Tuple
from pyspark.sql.types import DoubleType, StringType
from utils import extractor, pre_process
from algorithms import similarity


def create_consumption_history(user_id: str, tip_df: DataFrame, review_df: DataFrame) -> \
        Tuple[DataFrame, DataFrame]:
    """ Creates consumption history
    Parameters:
        user_id (str): id of the user
        tip_df (DataFrame): dataframe read from tip json
        review_df (DataFrame): dataframe read from review json
    Returns:
         tip_df_consumption_history (DataFrame), review_df_consumption_history (DataFrame)
    """
    user_review_history_df = review_df.filter(review_df.user_id == user_id).select(
        "business_id", "date", "stars", "text"
    )
    user_tip_history_df = tip_df.filter(tip_df.user_id == user_id).select(
        "business_id", "date", "text"
    )
    review_consumption_history = user_review_history_df.agg(
        collect_list(
            struct(
                "business_id",
                "date",
                "stars",
                "text"
            )
        ).alias("review_consumption_history")
    )
    tip_consumption_history = user_tip_history_df.agg(
        collect_list(
            struct(
                "business_id",
                "date",
                "text"
            )
        ).alias("tip_consumption_history")
    )
    return tip_consumption_history, review_consumption_history


def get_user_business_ids(review_df: DataFrame, tip_df: DataFrame, user_id: str) -> DataFrame:
    """ Get businesses visited by user with user_id from review_df and tip_df
    Parameters:
        review_df: Dataframe read from review json
        tip_df: Dataframe read from tip json
        user_id: the id of the user
    Returns:
        DataFrame joined by review_df and tip_df with user_id equal to given user_id
    """
    review_business_ids = review_df.filter(col("user_id") == user_id).select('business_id').distinct()
    tip_business_ids = tip_df.filter(col('user_id') == user_id).select('business_id').distinct()
    user_business_ids = review_business_ids.union(tip_business_ids).distinct()
    return user_business_ids


def calculate_user_business_similarity(spark: SparkSession, business_df: DataFrame,
                                       user_business_ids: DataFrame) -> DataFrame:
    """ Calculate similarities between businesses in user_business_ids and others
    Parameters:
        spark: Spark session
        business_df: Dataframe contains information about businesses
        user_business_ids: Dataframe contains information about businesses with a particular user_id
    Returns:
        DataFrame: similarities
    """
    jaccard_similarity_udf = udf(similarity.jaccard_similarity, DoubleType())
    user_businesses = business_df.join(user_business_ids, business_df.business_id ==
                                       user_business_ids.business_id)

    # 创建一个DataFrame，包含用户评价过的商家与其他所有商家之间的相似度
    similarity_df = spark.createDataFrame([], schema=business_df.schema.add("similarity", DoubleType()).add(
        "relevant_business_id", StringType()))

    # 计算用户评价过的商家与其他所有商家之间的相似度
    for row in user_businesses.collect():
        business_id = row['business_id']
        categories = row['categories']

        # 计算当前商家与其他所有商家之间的相似度
        new_rows = business_df.withColumn(
            "similarity",
            jaccard_similarity_udf(array([lit(c) for c in categories]), col("categories"))
        ).withColumn(
            "relevant_business_id", lit(business_id)
        )

        similarity_df = similarity_df.union(new_rows)

    return similarity_df


def epic8_task1(spark, user_id: str, tip_df: DataFrame, review_df: DataFrame, business_df: DataFrame)\
        -> DataFrame:
    # Pre-process
    review_df = pre_process.pre_process_review(review_df)
    tip_df = pre_process.pre_process_tip(tip_df)
    user_business_ids = get_user_business_ids(review_df, tip_df, user_id)

    # Feature extract
    business_features = ["business_id", "categories", "stars"]
    business_features_df = extractor.features_extractor(business_df, business_features)

    # Filter the business with stars greater than 3.5
    business_features_df = business_features_df.filter(col('stars') > 3.5)

    # Process categories and attributes for similarity calculation
    business_features_df = pre_process.process_categories(business_features_df)

    # Calculate similarities between businesses based on categories and attributes
    return (calculate_user_business_similarity(spark, business_features_df, user_business_ids)
            .orderBy(col('similarity').desc(), col('stars').desc()))
