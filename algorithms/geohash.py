import pygeohash as pgh


def geohash_udf(lat: float, lon: float, precision: int = 6):
    """ Compute geohash
    Parameters:
        lat (float): latitude
        lon (float): longitude
        precision (int): precision of the geohash
    Returns:
        Hash value
    """
    return pgh.encode(lat, lon, precision)
