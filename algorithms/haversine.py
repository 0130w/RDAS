from pyspark.sql import DataFrame
from pyspark.sql.functions import sin, cos, asin, sqrt, radians, col
import math


def haversine_distance(df: DataFrame, lat1_col: str, lon1_col: str,
                       lat2: float, lon2: float, r: int = 6371) -> DataFrame:
    """ Calculate the great circle distance between a list of place and a place
    Parameters:
        df (DataFrame): input dataframe
        lat1_col (str): lat1 column name
        lon1_col (str): lon1 column name
        lat2 (float): value of lat2
        lon2 (float): value of lon2
        r (int, optional): radius of the great circle
    Returns:
        DataFrame: dataframe with haversine distance(add 'distance' column to dataframe)
    """
    lat1 = radians(col(lat1_col))
    lon1 = radians(col(lon1_col))
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    d_lat = lat2 - lat1
    d_lon = lon2 - lon1

    a = sin(d_lat / 2) ** 2 + cos(lat1) * math.cos(lat2) * sin(d_lon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return df.withColumn("distance", c * r)
