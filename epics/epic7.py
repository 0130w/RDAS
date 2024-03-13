from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType
from typing import Tuple
from algorithms import geohash, haversine
from enum import Enum
from epics import epic6


def epic7_task1(location: Tuple[float, float], business_df: DataFrame,
                precision: int = 6) -> DataFrame:
    """ List nearby businesses according to the location of user
    Parameters:
        location (Tuple[float, float]) : location of user
        business_df (DataFrame) : business data
        precision (int, optional) : precision of the geohash
    Returns:
        DataFrame: sorted nearby businesses
    """
    latitude, longitude = location[0], location[1]
    geohash_udf = udf(geohash.geohash_udf, StringType())
    business_df = business_df.withColumn("geohash", geohash_udf(col("latitude"), col("longitude")))
    user_geohash = geohash.geohash_udf(latitude, longitude, precision)
    nearby_business_df = business_df.filter(business_df.geohash.startswith(user_geohash))
    sorted_nearby_business_df = haversine.haversine_distance(nearby_business_df, "latitude",
                                                             "longitude", latitude, longitude)
    return sorted_nearby_business_df


def epic7_task2():
    """ This task is not needed to be done in big data end """
    pass


class SortConditions(Enum):
    Synthesis = 1
    Distance = 2
    Stars = 3


def epic7_task3(sort_conditions: SortConditions, city: str, location: Tuple[float, float],
                review_df: DataFrame, checkin_df: DataFrame, business_df: DataFrame):
    """ Sort businesses based on sort conditions
    Parameters:
        sort_conditions (SortConditions): sort conditions
        city (str): city name of the user
        location (Tuple[float, float]): location of the user
        review_df (DataFrame): review dataframe read from review json
        checkin_df (DataFrame): checkin dataframe read from checkin json
        business_df (DataFrame): business dataframe read from business json
    Returns:
        DataFrame: sorted businesses based on sort conditions
    """
    if sort_conditions == SortConditions.Synthesis:
        return epic6.get_top_businesses(city, review_df, checkin_df, business_df).limit(10)
    elif sort_conditions == SortConditions.Distance:
        return epic7_task1(location, business_df)
    return business_df.orderBy('stars', ascending=False)
