# import
from pyspark.sql import SparkSession
from epics import epic7
# Driver
spark = SparkSession \
    .builder \
    .master('local') \
    .appName('SparkProj') \
    .getOrCreate()

# define dataset files path
business_path = 'dataset/yelp_academic_dataset_business.json'
checkin_path = 'dataset/yelp_academic_dataset_checkin.json'
review_path = 'dataset/yelp_academic_dataset_review.json'
tip_path = 'dataset/yelp_academic_dataset_tip.json'
user_path = 'dataset/yelp_academic_dataset_user.json'

review_df = spark.read.json(review_path)
tip_df = spark.read.json(tip_path)
business_df = spark.read.json(business_path)
user_df = spark.read.json(user_path)
checkin_df = spark.read.json(checkin_path)
# similarity = epic8.epic8_task1(spark, "_7bHUi9Uuf5__HHc_Q8guQ", tip_df, review_df, business_df)

result = epic7.epic7_task3(epic7.SortConditions.Distance, 'Affton', (38.551126, -90.335695),
                           review_df, checkin_df, business_df)

result.show(5)
