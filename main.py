"""films geo html-map"""
import math


def read_locations():
    """
    Takes path to a file with locations.
    """
    lst = []
    with open('C:/Users/User/Downloads/locations.list', 'r', encoding='ISO-8859-1') as file:
        for _ in range(14):
            file.readline()
        for _ in range(2):
            line = file.readline()
            line = line.strip().split('\t')
            lst.append((line[0], line[-1]))
    return lst


def haversine(lat_1, lon_1, lat_2, lon_2):
    """
    Calculates the distance between two points on the Earth, given these points` coordinates.
    """
    lat_1, lon_1, lat_2, lon_2 = map(
        math.radians, [lat_1, lon_1, lat_2, lon_2])

    lon = lon_2 - lon_1
    lat = lat_2 - lat_1

    haver = pow(math.sin(lat/2), 2) + math.cos(lat_1) * \
        math.cos(lat_2) * pow(math.sin(lon/2), 2)

    distance = 2 * 6371 * math.asin(math.sqrt(haver))

    return distance
