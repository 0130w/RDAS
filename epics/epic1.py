from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import col, size, split, avg, count


# task1: 找出美国最常见商户（前20）
def epic1_task1(business_df: DataFrame):
    return business_df.groupBy("name")\
        .count()\
        .orderBy(col("count").desc())\
        .limit(20)

# task2: 找出美国商户最多的前10个城市
def epic1_task2(business_df: DataFrame):
    return business_df.groupBy("city")\
        .count()\
        .orderBy(col("count").desc())\
        .limit(10)

# task3: 找出美国商户最多的前5个州
def epic1_task3(business_df: DataFrame):
    return  business_df.groupBy("state")\
        .count()\
        .orderBy(col("count").desc())\
        .limit(10)

# task4: 找出美国最常见商户，并显示平均评分（前20）
def epic1_task4(business_df: DataFrame):
    return business_df.groupBy("name")\
        .agg(count("*").alias("count"),avg(col('stars')).alias('avg_stars'))\
        .orderBy(col("count").desc())\
        .select("name",col("count"),col('avg_stars'))\
        .limit(20)

# task5: 统计评分最高的城市（前10）
def epic1_task5(business_df: DataFrame):
    return business_df.groupBy("city")\
        .agg(avg("stars").alias("avg_stars"))\
        .orderBy(col("avg_stars").desc())\
        .limit(10)

# task6: 统计category的数量
def epic1_task6(business_df: DataFrame):
    return business_df.select("categories").distinct().count()

# task7: 统计最多的category及数量（前10）
def epic1_task7(business_df: DataFrame):
    return business_df.groupby("categories")\
        .count()\
        .select("categories",col("count"))\
        .show(10)

# task8: 收获五星评论最多的商户（前20）
def epic1_task8(business_df: DataFrame, review_df: DataFrame):
    return review_df.filter(col("stars") == 5)\
        .groupby("business_id")\
        .agg(count("*").alias("five_star_reviews_count"))\
        .orderBy(col("five_star_reviews_count").desc())\
        .join(business_df, review_df["business_id"] == business_df["business_id"],"inner")\
        .select("name", col("five_star_reviews_count"))

