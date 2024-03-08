from functools import reduce

from typing import Tuple

from algorithms import kmeans
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import year, col, size, split, explode, regexp_replace

user_features = ['average_stars', 'sum_of_compliments', 'fans', 'review_count', 'times_of_elite',
                 'sum_of_sentiment_labels']


def epic2_task1(user_df: DataFrame):
    user_df_with_year = user_df.withColumn('join_year', year('yelping_since'))
    return user_df_with_year.groupBy('join_year').count().orderBy('join_year')


def epic2_task2(user_df: DataFrame):
    user_order_by_review_count = user_df.orderBy('review_count', ascending=False)
    return user_order_by_review_count.select('user_id', 'name', 'review_count', 'elite')


def epic2_task3(user_df: DataFrame):
    user_order_by_fans = user_df.orderBy('fans', ascending=False)
    return user_order_by_fans.select('user_id', 'name', 'fans')


def epic2_task4(user_df: DataFrame):
    sentiment_labels = ['cool', 'funny', 'useful']
    compliment_columns = [column for column in user_df.columns if column.startswith('compliment')]
    sum_of_compliments = reduce(lambda x, y: x + y, [col(column) for column in compliment_columns])
    classify_user_data = user_df.withColumn('sum_of_compliments', sum_of_compliments)
    classify_user_data = classify_user_data.withColumn('times_of_elite', size(split(col('elite'), ',')))
    sum_of_sentiment_labels = reduce(lambda x, y: x + y, [col(column) for column in sentiment_labels])
    classify_user_data = classify_user_data.withColumn('sum_of_sentiment_labels',
                                                       sum_of_sentiment_labels)
    kmeans.kmeans_predict(user_features, classify_user_data)


def epic2_task5(user_df: DataFrame):
    count_zero = user_df.filter(col('review_count') == 0).count()
    count_total = user_df.count()
    return count_zero, count_total


def epic2_task6(user_df: DataFrame, review_df: DataFrame,
                tip_df: DataFrame, checkin_df: DataFrame) -> Tuple[DataFrame, DataFrame, DataFrame,
DataFrame, DataFrame]:
    """
    Parameters:
        user_df: DataFrame from user.json
        review_df: DataFrame from review.json
        tip_df: DataFrame from tip.json
        checkin_df: DataFrame from checkin.json
    Return:
        new_users_count, elite_users_count, review_count, tip_count, checkin_count
    """
    new_users_count = user_df.withColumn('year', year('yelping_since')) \
        .groupBy('year').count().orderBy('year')
    elite_array_df = user_df.filter(col('elite') != '') \
        .withColumn('elite', regexp_replace(col('elite'), '20,20', '2020')) \
        .withColumn('elite_array', split(col('elite'), ','))
    elite_expand_df = elite_array_df.select(explode(col('elite_array')).alias('year'))
    elite_users_count = elite_expand_df.groupBy('year').count().orderBy('year')
    review_count = review_df.withColumn('year', year('date')) \
        .groupBy('year').count().orderBy('year')
    tip_count = tip_df.withColumn('year', year('date')) \
        .groupBy('year').count().orderBy('year')
    checkin_count = checkin_df.withColumn('year', year('date')) \
        .groupBy('year').count().orderBy('year')

    return new_users_count, elite_users_count, review_count, tip_count, checkin_count
