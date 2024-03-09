from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import col, max, min


def normalize_columns(df: DataFrame, columns: list) -> DataFrame:
    """ Given a DataFrame and a list of columns, 
        return the DataFrame containing the normalized columns.
    Parameters:
    df: DataFrame - the DataFrame containing the data
    columns: list - a list of columns to normalize
    Returns:
    DataFrame - a DataFrame containing the normalized columns
    """
    max_min_values = df.agg(
        *(max(col(c)).alias(f'max_{c}') for c in columns),
        *(min(col(c)).alias(f'min_{c}') for c in columns)
    ).collect()[0]

    for c in columns:
        df = df.withColumn(f'norm_{c}',
            (col(c) - max_min_values[f'min_{c}']) / (max_min_values[f'max_{c}'] - max_min_values[f'min_{c}']))
    return df
