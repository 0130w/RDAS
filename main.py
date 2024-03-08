# import
from pyspark.sql import SparkSession
from epics import  epic1

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

# epic1 测试代码
# b_df = spark.read.json(business_path)
# r_df = spark.read.json(review_path)

# epic1.epic1_task1(b_df).show()
# epic1.epic1_task2(b_df).show()
# epic1.epic1_task3(b_df).show()
# epic1.epic1_task4(b_df).show()
# epic1.epic1_task5(b_df).show()
# print(epic1.epic1_task6(b_df))
# epic1.epic1_task7(b_df).show()
# epic1.epic1_task8(b_df,r_df).show()
# epic1.epic1_task9(b_df).show()
# epic1.epic1_task10(b_df).show()
# epic1.epic1_task11(b_df).show()