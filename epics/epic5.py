from pyspark.sql.functions import date_format, col, avg, expr, count, month, quarter, year, when
from pyspark.sql.dataframe import DataFrame
from typing import Tuple


def epic5_task1(review_df: DataFrame):
    review_df = review_df.withColumn('weekday', date_format(col('date'), 'E'))
    weekday_review_stats = review_df.groupBy('weekday') \
        .agg(
        count('review_id').alias('review_count'),
        avg('stars').alias('average_stars')
    )

    weekday_review_stats = weekday_review_stats.withColumn(
        'weekday_order',
        expr("CASE weekday " +
             "WHEN 'Mon' THEN 1 " +
             "WHEN 'Tue' THEN 2 " +
             "WHEN 'Wed' THEN 3 " +
             "WHEN 'Thu' THEN 4 " +
             "WHEN 'Fri' THEN 5 " +
             "WHEN 'Sat' THEN 6 " +
             "WHEN 'Sun' THEN 7 " +
             "END")
    )
    return weekday_review_stats.orderBy('weekday_order').select('weekday', 'review_count', 'average_stars')


def epic5_task2(review_df: DataFrame) -> Tuple[DataFrame, DataFrame, DataFrame]:
    intervals = [
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5)
    ]

    def get_stats(col_name: str, date_extractor) -> DataFrame:
        df = review_df.withColumn(col_name, date_extractor('date'))
        for i, (lower_bound, upper_bound) in enumerate(intervals):
            df = df.withColumn(f'stars_{lower_bound}_{upper_bound}',
                               when((col('stars') >= lower_bound) & (col('stars') < upper_bound), 1)
                               .otherwise(0))
        return df.groupBy(col_name).sum(*[f'stars_{lower_bound}_{upper_bound}'
                                          for lower_bound, upper_bound in intervals]).orderBy(col_name)

    return (get_stats('month', month), get_stats('season', quarter),
            get_stats('year', year))
