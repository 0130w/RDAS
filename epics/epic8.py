from typing import Tuple

from pyspark.ml.feature import Tokenizer, IDF, HashingTF
from pyspark.sql import SparkSession
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import col, udf, lit, array, avg
from pyspark.sql.types import DoubleType, StringType, ArrayType, FloatType
from utils import extractor, pre_process, sentiments, randn, prompt_generate, request
from algorithms import similarity


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

    similarity_df = spark.createDataFrame([], schema=business_df.schema.add("similarity", DoubleType()).add(
        "relevant_business_id", StringType()))

    # compute the similarity between the businesses visited by user and other businesses
    for row in user_businesses.collect():
        business_id = row['business_id']
        categories = row['categories']

        new_rows = business_df.withColumn(
            "similarity",
            jaccard_similarity_udf(array([lit(c) for c in categories]), col("categories"))
        ).withColumn(
            "relevant_business_id", lit(business_id)
        )

        similarity_df = similarity_df.union(new_rows)

    return similarity_df


def epic8_task1(spark: SparkSession, user_id: str, tip_df: DataFrame,
                review_df: DataFrame, business_df: DataFrame) \
        -> DataFrame:
    """ Recommend businesses based on user's consumption history
    Parameters:
        spark (SparkSession)
        user_id (str): the id of the user
        tip_df (DataFrame): the dataframe read from tip json
        review_df (DataFrame): the dataframe read from review json
        business_df (DataFrame): the dataframe read from business json
    Returns:
        DataFrame: the dataframe with business_id and grade_scope sorted by grade_scope
    """
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
    similarities = (calculate_user_business_similarity(spark, business_features_df, user_business_ids)
                    .orderBy(col('similarity').desc(), col('stars').desc()))
    # Get comments from review_df and tip_df with given user
    user_review_df = review_df.filter(col('user_id') == user_id)
    user_tip_df = tip_df.filter(col('user_id') == user_id)
    # Do sentiment analysis to review_df and tip_df
    user_review_df = user_review_df.withColumn('sentiment', sentiments.analyze_sentiment(col('text')))
    user_tip_df = user_tip_df.withColumn('sentiment', sentiments.analyze_sentiment(col('text')))
    user_review_df = user_review_df.withColumnRenamed("business_id", "relevant_business_id")
    user_tip_df = user_tip_df.withColumnRenamed("business_id", "relevant_business_id")
    user_review_df = similarities.join(user_review_df, "relevant_business_id")
    user_tip_df = similarities.join(user_tip_df, "relevant_business_id")
    # Calculate grade score
    review_grade_score = user_review_df.withColumn('grade_score', col('sentiment') * col('similarity'))
    tip_grade_score = user_tip_df.withColumn('grade_score', col('sentiment') * col('similarity'))
    # Select business_id and grade_score
    review_grade_score_selected = review_grade_score.select('business_id', 'grade_score')
    tip_grade_score_selected = tip_grade_score.select('business_id', 'grade_score')
    # Combine two score table
    combined_grade_score = review_grade_score_selected.union(tip_grade_score_selected)
    combined_grade_score = (combined_grade_score.groupBy('business_id').agg(avg('grade_score').alias('grade_score')))
    final_df = (randn.add_random_noise(combined_grade_score, 'grade_score', 0.001, 0.001)
                .orderBy('grade_score', ascending=False))
    return final_df


def epic8_task2(business_id: str, review_df: DataFrame, tip_df: DataFrame) -> Tuple[DataFrame, str]:
    """ Give business advice by analyzing the review and tip
    Parameters:
        business_id (str): id of the input business
        review_df (DataFrame): dataframe read from review json
        tip_df (DataFrame): dataframe read from tip json
    Returns:
        DataFrame: dataframe contains text, sentiments and keywords
        str: contains advice given based on the text, sentiments and keywords
    """
    # Select business_id and text
    review_df = review_df.select('business_id', 'text').filter(col('business_id') == business_id).drop('business_id')
    tip_df = tip_df.select('business_id', 'text').filter(col('business_id') == business_id).drop('business_id')
    extract_keywords_udf = udf(sentiments.extract_keywords, ArrayType(StringType()))

    def sentiment_analysis(df: DataFrame) -> DataFrame:
        df = df.withColumn('sentiment', sentiments.analyze_sentiment(col('text')))
        df = df.withColumn('keywords', extract_keywords_udf(col('text')))
        return df
    # Do sentiment analysis with review and tip text
    review_df = sentiment_analysis(review_df)
    tip_df = sentiment_analysis(tip_df)

    union_df = review_df.union(tip_df)

    prompt = prompt_generate.generate_comprehensive_prompt(union_df)

    response = request.request_llm('gpt-3.5-turbo', prompt)

    return union_df, response


def epic8_task3(user_id: str, review_df: DataFrame,
                tip_df: DataFrame, user_df: DataFrame, n_recommendations=6):

    user_reviews = review_df.filter(review_df['user_id'] == user_id).select('text')
    user_tips = tip_df.filter(tip_df['user_id'] == user_id).select('text')
    user_data = user_reviews.union(user_tips).withColumnRenamed('text', 'user_text')

    # randomly get 20 users from user_df
    other_users = user_df.filter(user_df['user_id'] != user_id).sample(False, 0.1).limit(20)
    other_user_ids = [row['user_id'] for row in other_users.collect()]

    # tokenize the texts
    tokenizer = Tokenizer(inputCol="user_text", outputCol="words")
    user_words = tokenizer.transform(user_data)

    # calculate tf-idf
    hashing_tf = HashingTF(inputCol="words", outputCol="rawFeatures")
    featured_data = hashing_tf.transform(user_words)
    idf = IDF(inputCol="rawFeatures", outputCol="features")
    idf_model = idf.fit(featured_data)
    user_features = idf_model.transform(featured_data)

    # store similarity and user_id
    similarities = []

    for other_user in other_user_ids:
        other_reviews = review_df.filter(review_df['user_id'] == other_user).select('text')
        other_tips = tip_df.filter(tip_df['user_id'] == other_user).select('text')
        other_data = other_reviews.union(other_tips).withColumnRenamed('text', 'user_text')
        other_words = tokenizer.transform(other_data)
        other_featured_data = hashing_tf.transform(other_words)
        other_features = idf_model.transform(other_featured_data)

        other_features = other_features.withColumnRenamed('features', 'other_features')

        # get cosine_similarity
        sim = user_features.crossJoin(other_features) \
            .select(similarity.cosine_similarity_udf("features", "other_features").alias("similarity")) \
            .collect()[0]["similarity"]
        similarities.append((other_user, sim))

    similarities.sort(key=lambda x: x[1], reverse=True)
    recommended_friends = [user[0] for user in similarities[:n_recommendations]]

    # TODO! convert list to dataframe
    return recommended_friends
