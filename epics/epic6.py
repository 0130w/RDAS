from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import col, count, avg
from utils import normalize_columns


def get_top_businesses(city: str, review_df: DataFrame,
                       checkin_df: DataFrame, business_df: DataFrame) -> DataFrame:
    """ Get top businesses
    Parameters:
        city (str): city name
        review_df (DataFrame): dataframe read from review json
        checkin_df (DataFrame): dataframe read from checkin json
        business_df (DataFrame): dataframe read from business json
    Returns:
        DataFrame: dataframe contains top businesses
    """
    def calculate_sort_value(norm_reviews_build_in: float, norm_avg_stars_build_in: float,
                             norm_checkin_build_in: float):
        return norm_reviews_build_in * -1.5 + norm_avg_stars_build_in * 0.3 + norm_checkin_build_in * 0.2

    city_business_df = business_df.filter(col('city') == city)
    review_count = review_df.groupBy('business_id').agg(count('*').alias('reviews_count'))
    review_avg_stars = review_df.groupBy('business_id').agg(avg('stars').alias('avg_stars'))
    checkin_count = checkin_df.groupBy('business_id').agg(count('*').alias('checkin_count'))
    city_business_stats = city_business_df.join(review_count, 'business_id', 'left') \
        .join(review_avg_stars, 'business_id', 'left') \
        .join(checkin_count, 'business_id', 'left') \
        .na.fill(-1)
    city_business_stats = (normalize_columns.normalize_columns
                           (city_business_stats, ['reviews_count', 'avg_stars', 'checkin_count']))
    city_business_stats = city_business_stats.withColumn(
        'sort_value',
        calculate_sort_value(col('norm_reviews_count'), col('norm_avg_stars'), col('norm_checkin_count'))
    )
    return city_business_stats.orderBy(col('sort_value').desc())    \
        .select('address', 'hours', 'name', 'review_count', 'avg_stars', 'checkin_count')


def epic6_task1(city: str, review_df: DataFrame, checkin_df: DataFrame, business_df: DataFrame) -> DataFrame:
    """ Given a city, return the top 5 businesses based on the number of reviews,
        average stars, and checkins.
    Parameters:
    city: str - the city to search for businesses in
    review_df: DataFrame - the DataFrame containing the reviews data
    checkin_df: DataFrame - the DataFrame containing the checkin data
    business_df: DataFrame - the DataFrame containing the business data
    Returns:
    DataFrame - a DataFrame containing the top 5 businesses based on the number of reviews, average stars, and checkins
    """
    return get_top_businesses(city, review_df, checkin_df, business_df).limit(5)
