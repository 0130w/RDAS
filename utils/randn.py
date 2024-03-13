from pyspark.sql import DataFrame
from pyspark.sql.functions import col, randn


def add_random_noise(df: DataFrame, column_name: str, mean: float = 0, variance: float = 0.01) -> DataFrame:
    """ Add Gaussian noise in particular column
    Parameters:
        df (DataFrame): input dataframe
        column_name (str): name of the column to add gaussian noise
        mean (float): mean of the gaussian noise
        variance (float): variance of the gaussian noise
    Returns:
        DataFrame: input dataframe with added gaussian noise
    """
    return df.withColumn(
        column_name,
        col(column_name) + mean + variance * randn()
    )
