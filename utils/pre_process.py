from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import col, split


def process_categories(df: DataFrame) -> DataFrame:
    """ Split categories into separate strings
    Parameters:
        df (DataFrame): Dataframe with categorical columns
    Returns:
        DataFrame after splitting categorical columns
    """
    df = df.withColumn("categories", split(col("categories"), ", "))
    return df


def pre_process_review(review_df: DataFrame) -> DataFrame:
    """ Fill missing values with 0 and cast date column to date type
    Parameters:
         review_df (DataFrame): Dataframe read from review json
    Returns:
        DataFrame: review_df after preprocessing
    """
    review_df = review_df.fillna({'stars': 0, 'useful': 0, 'funny': 0, 'cool': 0})
    review_df = review_df.withColumn('date', col('date').cast('date'))
    return review_df


def pre_process_tip(tip_df: DataFrame) -> DataFrame:
    """ Fill missing values with 0 and cast date column to date type
    Parameters:
         tip_df (DataFrame): Dataframe read from tip json
    Returns:
        DataFrame: tip_df after preprocessing
    """
    tip_df = tip_df.fillna({'compliment_count': 0})
    tip_df = tip_df.withColumn('date', col('date').cast('date'))
    return tip_df


