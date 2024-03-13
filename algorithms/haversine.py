from pyspark.sql.functions import sin, cos, asin, sqrt, radians, col
import math


def haversine_distance(df, lat1_col, lon1_col, lat2, lon2, r=6371):
    lat1 = radians(col(lat1_col))
    lon1 = radians(col(lon1_col))
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    d_lat = lat2 - lat1
    d_lon = lon2 - lon1

    a = sin(d_lat / 2) ** 2 + cos(lat1) * math.cos(lat2) * sin(d_lon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return df.withColumn("distance", c * r)
