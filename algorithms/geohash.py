import pygeohash as pgh


def geohash_udf(lat, lon, precision=6):
    return pgh.encode(lat, lon, precision)
