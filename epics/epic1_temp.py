from pyspark.sql.dataframe import DataFrame
from pyspark.sql import Window
from pyspark.sql.functions import col, count, avg, sum, max, min, when,year


def epic1_task1(business_df: DataFrame):
    """ Given a DataFrame containing business data, return the most common business in the US.
    Parameters:
    business_df: DataFrame - a DataFrame containing business data
    Returns:
    DataFrame - a DataFrame containing the most common business in the US"""
    return business_df.groupBy("name") \
        .count() \
        .orderBy(col("count").desc()) \
        .limit(20)


def epic1_task2(business_df: DataFrame):
    """ Given a DataFrame containing business data, return the most common city in the US.
    Parameters:
    business_df: DataFrame - a DataFrame containing business data
    Returns:
    DataFrame - a DataFrame containing the most common city in the US"""
    return business_df.groupBy("city") \
        .count() \
        .orderBy(col("count").desc()) \
        .limit(10)


def epic1_task3(business_df: DataFrame):
    """ Given a DataFrame containing business data, return the most common state in the US.
    Parameters:
    business_df: DataFrame - a DataFrame containing business data
    Returns:
    DataFrame - a DataFrame containing the most common state in the US"""
    return business_df.groupBy("state") \
        .count() \
        .orderBy(col("count").desc()) \
        .limit(10)


def epic1_task4(business_df: DataFrame):
    """ Given a DataFrame containing business data, return the top 20 businesses with the most reviews.
    Parameters:
    business_df: DataFrame - a DataFrame containing business data
    Returns:
    DataFrame - a DataFrame containing the top 20 businesses with the most reviews"""
    return business_df.groupBy("name") \
        .agg(count("*").alias("count"), avg(col('stars')).alias('avg_stars')) \
        .orderBy(col("count").desc()) \
        .select("name", col("count"), col('avg_stars')) \
        .limit(20)


def epic1_task5(business_df: DataFrame):
    """ Given a DataFrame containing business data, return the average stars for each city.
    Parameters:
    business_df: DataFrame - a DataFrame containing business data
    Returns:
    DataFrame - a DataFrame containing the average stars for each city"""
    window_spec = Window.partitionBy("city")
    return business_df.select(
        col("city"),
        avg(col("stars")).over(window_spec).alias("avg_stars"),
    ) \
        .distinct() \
        .limit(10)


def epic1_task6(business_df: DataFrame):
    """ Given a DataFrame containing business data, return the number of unique categories.
    Parameters:
    business_df: DataFrame - a DataFrame containing business data
    Returns:
    int - the number of unique categories"""
    return business_df.select("categories").distinct().count()


def epic1_task7(business_df: DataFrame):
    """ Given a DataFrame containing business data, return the top 10 most common categories.
    Parameters:
    business_df: DataFrame - a DataFrame containing business data
    Returns:
    DataFrame - a DataFrame containing the top 10 most common categories"""
    return business_df.groupby("categories") \
        .count() \
        .orderBy(col("count").desc()) \
        .select("categories", col("count")) \
        .limit(10)


def epic1_task8(business_df: DataFrame, review_df: DataFrame):
    """ Given a DataFrame containing business data and a DataFrame containing review data,
        return the top 20 businesses with the most 5-star reviews.
    Parameters:
    business_df: DataFrame - a DataFrame containing business data
    review_df: DataFrame - a DataFrame containing review data
    Returns:
    DataFrame - a DataFrame containing the top 20 businesses with the most 5-star reviews"""
    return review_df.filter(col("stars") == 5) \
        .groupby("business_id") \
        .agg(count("*").alias("five_star_reviews_count")) \
        .orderBy(col("five_star_reviews_count").desc()) \
        .join(business_df, review_df["business_id"] == business_df["business_id"], "inner") \
        .select("name", col("five_star_reviews_count")) \
        .limit(20)


# define target_cuisines
target_cuisines_task9to12 = ['Chinese', 'American', 'Mexican']


def epic1_filter_by_target_cuisines(business_df: DataFrame, target_cuisines: list):
    """ Given a DataFrame containing business data and a list of target cuisines,
        return a DataFrame containing only businesses that serve the target cuisines.
    Parameters:
    business_df: DataFrame - a DataFrame containing business data
    target_cuisines: list - a list of target cuisines
    Returns:
    DataFrame - a DataFrame containing only businesses that serve the target cuisines"""
    conditions = [business_df["categories"].contains("Restaurant") & business_df["categories"].contains(cuisine) for
                  cuisine in target_cuisines]
    business_df = business_df.withColumn("target_cuisines", when(conditions[0], target_cuisines[0]))
    for i in range(1, len(conditions)):
        business_df = business_df.withColumn("target_cuisines", when(conditions[i], target_cuisines[i]).otherwise(
            business_df["target_cuisines"]))
    return business_df.filter(business_df["target_cuisines"].isin(target_cuisines))


def epic1_task9(business_df: DataFrame, target_cuisines=None):
    """ Given a DataFrame containing business data, return the number of businesses that serve each target cuisine.
    Parameters:
    business_df: DataFrame - a DataFrame containing business data
    target_cuisines: list - a list of target cuisines
    Returns:
    DataFrame - a DataFrame containing the number of businesses that serve each target cuisine"""
    if target_cuisines is None:
        target_cuisines = target_cuisines_task9to12
    filtered_business_df = epic1_filter_by_target_cuisines(business_df, target_cuisines)
    return filtered_business_df.groupBy("target_cuisines") \
        .count() \
        .orderBy(col("count").desc()) \


def epic1_task10(business_df: DataFrame, target_cuisines=None):
    """ Given a DataFrame containing business data, return the total number of reviews for each target cuisine.
    Parameters:
    business_df: DataFrame - a DataFrame containing business data
    target_cuisines: list - a list of target cuisines
    Returns:
    DataFrame - a DataFrame containing the total number of reviews for each target cuisine"""
    if target_cuisines is None:
        target_cuisines = target_cuisines_task9to12
    filtered_business_df = epic1_filter_by_target_cuisines(business_df, target_cuisines)
    # 使用窗口函数计算每种商家类型的评论数量
    window_spec = Window.partitionBy("target_cuisines")
    return filtered_business_df.select(
        col("target_cuisines"),
        sum(col("review_count")).over(window_spec).alias("total_review_count")
    ) \
        .distinct()


def epic1_task11(business_df: DataFrame, target_cuisines=None):
    """ Given a DataFrame containing business data, return the average stars for each target cuisine.
    Parameters:
    business_df: DataFrame - a DataFrame containing business data
    target_cuisines: list - a list of target cuisines
    Returns:
    DataFrame - a DataFrame containing the average stars for each target cuisine"""
    if target_cuisines is None:
        target_cuisines = target_cuisines_task9to12
    filtered_business_df = epic1_filter_by_target_cuisines(business_df, target_cuisines)
    window_spec = Window.partitionBy("target_cuisines")
    return filtered_business_df.select(
        col("target_cuisines"),
        avg(col("stars")).over(window_spec).alias("avg_stars"),
        min(col("stars")).over(window_spec).alias("min_stars"),
        max(col("stars")).over(window_spec).alias("max_stars")
    ) \
        .distinct()

def epic1_task12(business_df:DataFrame,checkin_df:DataFrame, target_cuisines: list):
    """
    Parameters:
        business_df: DataFrame - a DataFrame containing business data
        checkin_df: DataFrame - a DataFrame containing checkin data
        target_cuisines: list - a list of target cuisines
    Returns:
        DataFrame - a DataFrame containing the number of checkins for each target cuisine by year"""
    join_business = business_df.join(checkin_df, business_df['business_id'] == checkin_df['business_id']) 
    if target_cuisines is None:
        target_cuisines = target_cuisines_task9to12
    filtered_business_df = epic1_filter_by_target_cuisines(join_business, target_cuisines_task9to12)
    filtered_business_df = filtered_business_df.withColumn('year',year('date')).drop('date')

    American_count_by_year = filtered_business_df.filter(filtered_business_df.target_cuisines == 'American').groupBy("year").count().orderBy("year")
    Mexican_count_by_year = filtered_business_df.filter(filtered_business_df.target_cuisines == 'Mexican').groupBy("year").count().orderBy("year")
    Chinese_count_by_year = filtered_business_df.filter(filtered_business_df.target_cuisines == 'Chinese').groupBy("year").count().orderBy("year")

    return American_count_by_year, Mexican_count_by_year, Chinese_count_by_year
