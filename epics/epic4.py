from pyspark.sql.dataframe import DataFrame
from pyspark.sql import Window
from pyspark.sql.functions import col, year, count, sum, hour
from utils import explode_column


def epic4_task1(checkin_df: DataFrame):
    """ Count the number of checkins for each business in each year
    Parameters:
    checkin_df (DataFrame): DataFrame with checkin data
    Returns:
    DataFrame: DataFrame with business_id, year, and year_checkin_count columns"""
    window_spec = Window.partitionBy("business_id", "year")
    exploded_checkin_df = explode_column.explode_column(checkin_df, "date", ", ")
    return exploded_checkin_df.withColumn("year", year(col("date"))) \
        .select("business_id", "year", count("*").over(window_spec).alias("year_checkin_count")) \
        .orderBy("business_id", "year") \
        .distinct()


def epic4_task1_selectById(checkin_df: DataFrame, business_id):
    """ Count the number of checkins for a specific business in each year
    Parameters:
    checkin_df (DataFrame): DataFrame with checkin data
    business_id (str): The business_id to filter the DataFrame
    Returns:
    DataFrame: DataFrame with year and year_checkin_count columns for the specified business_id"""
    exploded_checkin_df = explode_column.explode_column(checkin_df, "date", ", ")
    return exploded_checkin_df.filter(col("business_id") == business_id) \
        .withColumn("year", year(col("date"))) \
        .groupBy("year") \
        .agg(count("*").alias("year_checkin_count")) \
        .orderBy("year") \
        .select("year", "year_checkin_count") \
        .distinct()


def epic4_task2(checkin_df: DataFrame):
    """ Count the number of checkins for each business in each hour
    Parameters:
    checkin_df (DataFrame): DataFrame with checkin data
    Returns:
    DataFrame: DataFrame with business_id, hour, and hour_checkin_count columns"""
    window_spec = Window.partitionBy("business_id", "hour")
    exploded_checkin_df = explode_column.explode_column(checkin_df, "date", ", ")
    return exploded_checkin_df.withColumn("hour", hour(col("date"))) \
        .select("business_id", "hour", count("*").over(window_spec).alias("hour_checkin_count")) \
        .orderBy("business_id", "hour") \
        .distinct()


def epic4_task2_selectById(checkin_df: DataFrame, business_id):
    """ Count the number of checkins for a specific business in each hour
    Parameters:
    checkin_df (DataFrame): DataFrame with checkin data
    business_id (str): The business_id to filter the DataFrame
    Returns:
    DataFrame: DataFrame with hour and hour_checkin_count columns for the specified business_id"""
    exploded_checkin_df = explode_column.explode_column(checkin_df, "date", ", ")
    return exploded_checkin_df.filter(col("business_id") == business_id) \
        .withColumn("hour", hour(col("date"))) \
        .groupBy("hour") \
        .agg(count("*").alias("hour_checkin_count")) \
        .orderBy("hour") \
        .select("hour", "hour_checkin_count") \
        .distinct()


def epic4_task3(checkin_df: DataFrame, business_df: DataFrame):
    """ Count the number of checkins for each city
    Parameters:
    checkin_df (DataFrame): DataFrame with checkin data
    business_df (DataFrame): DataFrame with business data
    Returns:
    DataFrame: DataFrame with city and total_checkin_count columns
    for each city in descending order of total_checkin_count"""
    window_spec = Window.partitionBy("city")
    exploded_checkin_df = explode_column.explode_column(checkin_df, "date", ", ")
    return exploded_checkin_df.groupby("business_id") \
        .agg(count("*").alias("checkin_count")) \
        .join(business_df, checkin_df["business_id"] == business_df["business_id"], "inner") \
        .select("city", sum("checkin_count").over(window_spec).alias("total_checkin_count")) \
        .distinct() \
        .orderBy(col("total_checkin_count").desc()) \



def epic4_task4(checkin_df: DataFrame, business_df: DataFrame):
    """ Count the number of checkins for each business
    Parameters:
    checkin_df (DataFrame): DataFrame with checkin data
    business_df (DataFrame): DataFrame with business data
    Returns:
    DataFrame: DataFrame with name and checkin_count columns
    for each business in descending order of checkin_count"""
    exploded_checkin_df = explode_column.explode_column(checkin_df, "date", ", ")
    return exploded_checkin_df.groupby("business_id") \
        .agg(count("*").alias("checkin_count")) \
        .orderBy(col("checkin_count").desc()) \
        .join(business_df, checkin_df["business_id"] == business_df["business_id"], "inner") \
        .select("name", "checkin_count")
