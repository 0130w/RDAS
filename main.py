# import
from pyspark.sql import SparkSession
from epics import epic5

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

a, b, c = epic5.epic5_task2(review_df)
a.show()
b.show()
c.show()
