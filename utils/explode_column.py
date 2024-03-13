from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import col, explode, split


def explode_column(df: DataFrame, col_name: str, split_by: str) -> DataFrame:
    ''' Explode a column in a DataFrame
    Parameters:
        df (DataFrame): DataFrame to be exploded
        col_name (str): Column name to be exploded
        split_by (str): Delimiter to split the column
    Returns:
        DataFrame: DataFrame with exploded column'''
    return df.withColumn(col_name, explode(split(col(col_name), split_by)))
