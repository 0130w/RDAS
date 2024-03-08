from pyspark.sql.dataframe import DataFrame
from pyspark.sql import Window
from pyspark.sql.functions import col, year, count, sum, explode, split, hour


#  将date列中的标签拆分为单独的行
def explode_date(checkin_df: DataFrame):
    return checkin_df.withColumn("date", explode(split(col("date"), ", ")))


# task1: 统计每年的打卡次数
def epic4_task1(checkin_df: DataFrame):
    window_spec = Window.partitionBy("business_id", "year")
    exploded_checkin_df = explode_date(checkin_df)
    return exploded_checkin_df.withColumn("year", year(col("date"))) \
        .select("business_id", "year", count("*").over(window_spec).alias("year_checkin_count")) \
        .orderBy("business_id", "year") \
        .distinct()

def epic4_task1_selectById(checkin_df: DataFrame, business_id):
    exploded_checkin_df = explode_date(checkin_df)
    return exploded_checkin_df.filter(col("business_id") == business_id)\
        .withColumn("year", year(col("date"))) \
        .groupBy("year")\
        .agg(count("*").alias("year_checkin_count")) \
        .orderBy("year") \
        .select("year", "year_checkin_count") \
        .distinct()


# task2: 统计24小时每小时打卡次数
def epic4_task2(checkin_df: DataFrame):
    window_spec = Window.partitionBy("business_id", "hour")
    exploded_checkin_df = explode_date(checkin_df)
    return exploded_checkin_df.withColumn("hour", hour(col("date"))) \
        .select("business_id", "hour", count("*").over(window_spec).alias("hour_checkin_count")) \
        .orderBy("business_id", "hour") \
        .distinct()

def epic4_task2_selectById(checkin_df: DataFrame, business_id):
    exploded_checkin_df = explode_date(checkin_df)
    return exploded_checkin_df.filter(col("business_id") == business_id)\
        .withColumn("hour", hour(col("date"))) \
        .groupBy("hour")\
        .agg(count("*").alias("hour_checkin_count")) \
        .orderBy("hour") \
        .select("hour", "hour_checkin_count") \
        .distinct()

# task3: 统计最喜欢打卡的城市
def epic4_task3(checkin_df: DataFrame, business_df: DataFrame):
    window_spec = Window.partitionBy("city")
    exploded_checkin_df = explode_date(checkin_df)
    return exploded_checkin_df.groupby("business_id") \
        .agg(count("*").alias("checkin_count")) \
        .join(business_df, checkin_df["business_id"] == business_df["business_id"], "inner") \
        .select("city", sum("checkin_count").over(window_spec).alias("total_checkin_count")) \
        .distinct() \
        .orderBy(col("total_checkin_count").desc()) \


# task4: 全部商家的打卡排行榜
def epic4_task4(checkin_df: DataFrame, business_df: DataFrame):
    exploded_checkin_df = explode_date(checkin_df)
    return exploded_checkin_df.groupby("business_id") \
        .agg(count("*").alias("checkin_count")) \
        .orderBy(col("checkin_count").desc()) \
        .join(business_df, checkin_df["business_id"] == business_df["business_id"], "inner") \
        .select("name", "checkin_count") \
        .show()
