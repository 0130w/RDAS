from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import col, count, avg
from utils import normalize_columns


def epic6_task1(city: str, review_df: DataFrame, checkin_df: DataFrame, business_df: DataFrame) -> DataFrame:

    def calculate_sort_value(norm_reviews_build_in: float, norm_avg_stars_build_in: float, norm_checkin_build_in: float):
        return norm_reviews_build_in * 0.5 + norm_avg_stars_build_in * 0.3 + norm_checkin_build_in * 0.2

    city_business_df = business_df.filter(col('city') == city)
    review_count = review_df.groupBy('business_id').agg(count('*').alias('reviews_count'))
    review_avg_stars = review_df.groupBy('business_id').agg(avg('stars').alias('avg_stars'))
    checkin_count = checkin_df.groupBy('business_id').agg(count('*').alias('checkin_count'))
    city_business_stats = city_business_df.join(review_count, 'business_id', 'left') \
        .join(review_avg_stars, 'business_id', 'left') \
        .join(checkin_count, 'business_id', 'left') \
        .na.fill(0)
    city_business_stats = (normalize_columns.normalize_columns
                           (city_business_stats, ['reviews_count', 'avg_stars', 'checkin_count']))
    city_business_stats = city_business_stats.withColumn(
        'sort_value',
        calculate_sort_value(col('norm_reviews_count'), col('norm_avg_stars'), col('norm_checkin_count'))
    )
    top_5_businesses = city_business_stats.orderBy(col('sort_value').desc()).limit(5)\
        .select('address', 'hours', 'name', 'review_count', 'avg_stars', 'checkin_count')
    return top_5_businesses
