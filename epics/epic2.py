from functools import reduce
from algorithms import kmeans
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import year, col, size, split

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
    classify_user_data.withColumn('sum_of_sentiment_labels',
                                  sum_of_sentiment_labels)
    kmeans.kmeans_test(user_features, classify_user_data)
