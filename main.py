# import
from pyspark.sql import SparkSession

# Driver
spark = SparkSession \
    .builder \
    .master('local') \
    .appName('SparkProj') \
    .config("spark.sql.parquet.output.committer.class", "org.apache.spark.sql.parquet.DirectParquetOutputCommitter") \
 \
    .getOrCreate()

# define dataset files path
business_path = 'dataset/yelp_academic_dataset_business.json'
checkin_path = 'dataset/yelp_academic_dataset_checkin.json'
review_path = 'dataset/yelp_academic_dataset_review.json'
tip_path = 'dataset/yelp_academic_dataset_tip.json'
user_path = 'dataset/yelp_academic_dataset_user.json'
