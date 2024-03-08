from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import col, max, min


def normalize_columns(df: DataFrame, columns: list) -> DataFrame:
    max_min_values = df.agg(
        *(max(col(c)).alias(f'max_{c}') for c in columns),
        *(min(col(c)).alias(f'min_{c}') for c in columns)
    ).collect()[0]

    for c in columns:
        df = df.withColumn(f'norm_{c}',
            (col(c) - max_min_values[f'min_{c}']) / (max_min_values[f'max_{c}'] - max_min_values[f'min_{c}']))
    return df
