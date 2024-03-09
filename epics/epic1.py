from pyspark.sql.dataframe import DataFrame
from pyspark.sql import Window
from pyspark.sql.functions import col, count, avg, sum, max, min, when


# task1: 找出美国最常见商户（前20）
def epic1_task1(business_df: DataFrame):
    return business_df.groupBy("name") \
        .count() \
        .orderBy(col("count").desc()) \
        .limit(20)


# task2: 找出美国商户最多的前10个城市
def epic1_task2(business_df: DataFrame):
    return business_df.groupBy("city") \
        .count() \
        .orderBy(col("count").desc()) \
        .limit(10)


# task3: 找出美国商户最多的前5个州
def epic1_task3(business_df: DataFrame):
    return business_df.groupBy("state") \
        .count() \
        .orderBy(col("count").desc()) \
        .limit(10)


# task4: 找出美国最常见商户，并显示平均评分（前20）
def epic1_task4(business_df: DataFrame):
    return business_df.groupBy("name") \
        .agg(count("*").alias("count"), avg(col('stars')).alias('avg_stars')) \
        .orderBy(col("count").desc()) \
        .select("name", col("count"), col('avg_stars')) \
        .limit(20)


# task5: 统计评分最高的城市（前10）
def epic1_task5(business_df: DataFrame):
    # 通过窗口函数统计平均评分
    window_spec = Window.partitionBy("city")
    return business_df.select(
        col("city"),
        avg(col("stars")).over(window_spec).alias("avg_stars"),
    ) \
        .distinct()\
        .limit(10)


# task6: 统计category的数量 (需print打印，无法调用show())
def epic1_task6(business_df: DataFrame):
    return business_df.select("categories").distinct().count()


# task7: 统计最多的category及数量（前10）
def epic1_task7(business_df: DataFrame):
    return business_df.groupby("categories") \
        .count() \
        .orderBy(col("count").desc())\
        .select("categories", col("count")) \
        .limit(10)


# task8: 收获五星评论最多的商户（前20）
def epic1_task8(business_df: DataFrame, review_df: DataFrame):
    return review_df.filter(col("stars") == 5) \
        .groupby("business_id") \
        .agg(count("*").alias("five_star_reviews_count")) \
        .orderBy(col("five_star_reviews_count").desc()) \
        .join(business_df, review_df["business_id"] == business_df["business_id"], "inner") \
        .select("name", col("five_star_reviews_count"))\
        .limit(20)


# task9-12目标分类
target_cuisines_task9to12 = ['Chinese', 'American', 'Mexican']

# 定义函数，根据目标餐厅类型对商户进行分类
def epic1_filter_by_target_cuisines(business_df: DataFrame, target_cuisines: list):
    # 定义过滤条件
    conditions = [business_df["categories"].contains("Restaurant") & business_df["categories"].contains(cuisine) for
                  cuisine in target_cuisines]
    # 创建目标餐厅类型列
    business_df = business_df.withColumn("target_cuisines", when(conditions[0], target_cuisines[0]))
    # 逐个添加条件
    for i in range(1, len(conditions)):
        business_df = business_df.withColumn("target_cuisines", when(conditions[i], target_cuisines[i]).otherwise(
            business_df["target_cuisines"]))
    # 过滤出目标餐厅类型的商户
    return business_df.filter(business_df["target_cuisines"].isin(target_cuisines))

# task9: 统计不同类型（中国菜、美式、墨西哥）的餐厅类型及数量
def epic1_task9(business_df: DataFrame, target_cuisines=None):
    if target_cuisines is None:
        target_cuisines = target_cuisines_task9to12
    filtered_business_df = epic1_filter_by_target_cuisines(business_df, target_cuisines)
    return filtered_business_df.groupBy("target_cuisines")\
        .count()\
        .orderBy(col("count").desc())\

# task10: 统计不同类型（中国菜、美式、墨西哥）的餐厅类型及数量
def epic1_task10(business_df: DataFrame, target_cuisines=None):
    if target_cuisines is None:
        target_cuisines = target_cuisines_task9to12
    filtered_business_df = epic1_filter_by_target_cuisines(business_df, target_cuisines)
    # 使用窗口函数计算每种商家类型的评论数量
    window_spec = Window.partitionBy("target_cuisines")
    return filtered_business_df.select(
        col("target_cuisines"),
        sum(col("review_count")).over(window_spec).alias("total_review_count")
    )\
        .distinct()

# task11: 统计不同类型（中国菜、美式、墨西哥）的餐厅的评分分布
def epic1_task11(business_df: DataFrame, target_cuisines=None):
    if target_cuisines is None:
        target_cuisines = target_cuisines_task9to12
    filtered_business_df = epic1_filter_by_target_cuisines(business_df, target_cuisines)
    # 使用窗口函数计算每种商家类型的评分平均值、最小值和最大值
    window_spec = Window.partitionBy("target_cuisines")
    return filtered_business_df.select(
        col("target_cuisines"),
        avg(col("stars")).over(window_spec).alias("avg_stars"),
        min(col("stars")).over(window_spec).alias("min_stars"),
        max(col("stars")).over(window_spec).alias("max_stars")
    )\
        .distinct()