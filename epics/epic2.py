from functools import reduce
from typing import Tuple
from algorithms import kmeans
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import year, col, size, split, explode, regexp_replace, count, sequence, lit, max as smax

user_features = ['average_stars', 'sum_of_compliments', 'fans', 'review_count', 'times_of_elite',
                 'sum_of_sentiment_labels']


def epic2_task1(user_df: DataFrame):
    """ Given a DataFrame containing user data, return the number of users 
        who joined each year.
    Parameters:
    user_df: DataFrame - a DataFrame containing user data
    Returns:
    DataFrame - a DataFrame containing the number of users who joined each year
    """
    user_df_with_year = user_df.withColumn('join_year', year('yelping_since'))
    return user_df_with_year.groupBy('join_year').count().orderBy('join_year')


def epic2_task2(user_df: DataFrame):
    """ Given a DataFrame containing user data, return the sequence of users based on 
        the number of reviews they have written.
    Parameters:
    user_df: DataFrame - a DataFrame containing user data
    Returns:
    DataFrame - a DataFrame containing the sequence of users based on the number of reviews they have written
    """
    user_order_by_review_count = user_df.orderBy('review_count', ascending=False)
    return user_order_by_review_count.select('user_id', 'name', 'review_count', 'elite')


def epic2_task3(user_df: DataFrame):
    """ Given a DataFrame containing user data, return the sequence of users based on 
        the number of fans they have.
    Parameters:
    user_df: DataFrame - a DataFrame containing user data
    Returns:
    DataFrame - a DataFrame containing the sequence of users based on the number of fans they have
    """
    user_order_by_fans = user_df.orderBy('fans', ascending=False)
    return user_order_by_fans.select('user_id', 'name', 'fans')


def epic2_task4(user_df: DataFrame):
    """ Given a DataFrame containing user data, using the k-means algorithm 
        to classify users into normal users and premium users.
    Parameters:
    user_df: DataFrame - a DataFrame containing user data
    Returns:
    DataFrame - a DataFrame containing the users classified into normal users and premium users, if predict field is 0, it means the user
    is a premium user, if predict field is 1, it means the user is a normal user
    """
    sentiment_labels = ['cool', 'funny', 'useful']
    compliment_columns = [column for column in user_df.columns if column.startswith('compliment')]
    sum_of_compliments = reduce(lambda x, y: x + y, [col(column) for column in compliment_columns])
    classify_user_data = user_df.withColumn('sum_of_compliments', sum_of_compliments)
    classify_user_data = classify_user_data.withColumn('times_of_elite', size(split(col('elite'), ',')))
    sum_of_sentiment_labels = reduce(lambda x, y: x + y, [col(column) for column in sentiment_labels])
    classify_user_data = classify_user_data.withColumn('sum_of_sentiment_labels',
                                                       sum_of_sentiment_labels)
    kmeans.kmeans_predict(user_features, classify_user_data)


def epic2_task5(user_df: DataFrame, review_df: DataFrame) -> DataFrame:
    """ Given a DataFrame containing user data and a DataFrame containing review data, return the ratio of silent users for each year.
    Parameters:
    user_df: DataFrame - a DataFrame containing user data
    review_df: DataFrame - a DataFrame containing review data
    Returns:
    DataFrame - a DataFrame containing the ratio of silent users for each year
    """
    sup_year = user_df.select(smax(year('yelping_since'))).collect()[0][0]
    user_years = user_df.withColumn('join_year', year('yelping_since')) \
        .withColumn('years', sequence(col('join_year'), lit(sup_year)))
    user_year_count = user_years.select('user_id', explode('years').alias('year')) \
        .groupby('year') \
        .agg(count('user_id').alias('total_users'))
    review_year_count = review_df.withColumn('review_year', year('date')) \
        .dropDuplicates(['review_year', 'user_id']) \
        .groupBy('review_year') \
        .agg(count('user_id').alias('active_users'))
    silent_user_ratio = user_year_count.join(review_year_count,
                                             user_year_count['year'] == review_year_count['review_year'], 'left_outer') \
        .withColumn('silent_user_ratio', (col('total_users') - col('active_users')) / col('total_users')) \
        .select('year', 'silent_user_ratio')
    return silent_user_ratio.filter(col('silent_user_ratio').isNotNull()).orderBy('year')


def epic2_task6(user_df: DataFrame, review_df: DataFrame,
                tip_df: DataFrame, checkin_df: DataFrame) -> Tuple[DataFrame, DataFrame, DataFrame,
DataFrame, DataFrame]:
    """ Given a DataFrame containing user data, a DataFrame containing review data, 
        a DataFrame containing tip data, and a DataFrame containing checkin data, 
        return the number of new users, the number of elite users, the number of reviews, 
        the number of tips, and the number of checkins for each year.
    Parameters:
        user_df: DataFrame from user.json
        review_df: DataFrame from review.json
        tip_df: DataFrame from tip.json
        checkin_df: DataFrame from checkin.json
    Returns:
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
