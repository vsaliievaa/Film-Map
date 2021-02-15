"""films geo html-map"""
import folium
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable
import math
import random
import re


def processing_locations(locations: list) -> list:
    """
    Calculates the cordinates for locations, appends them to locations list
    and returns the list.
    """
    for i in range(len(locations)):
        coords = coordinates(locations[i][1])
        if coords != 'Not found' and coords != None:
            locations[i].append(coords)
    return locations


def read_locations(year: int) -> list:
    """
    Takes path to a file with locations, returns a list of all films, that
    match the year, entered by user, and are available for geocoding.
    """
    locations = []
    with open('locations.list', 'r', encoding='ISO-8859-1') as file:
        for _ in range(14):
            file.readline()
        for line in file:
            if re.findall(str(year), line):
                line = line.strip().split('\t')
                if len(line[-1].split("(")) == 1:
                    f_line = list(filter(None, line))
                    locations.append([f_line[0], f_line[1:]])
    return locations


def coordinates(place: str) -> tuple:
    """
    Defines the coordinates of the given location using geopy, returns 'Not found'
    if coordinates of the given place cannot be found.
    """
    try:
        geolocator = Nominatim(user_agent="Film-Map")
        location = geolocator.geocode(place)
        if hasattr(location, 'latitude') and location.latitude is not None:
            if hasattr(location, 'longitude') and location.longitude is not None:
                return ((location.latitude, location.longitude))
        return 'Not found'
    except:
        'GeocoderUnavailable'


def haversine(lat_1: str, lon_1: str, lat_2: str, lon_2: str) -> str:
    """
    Calculates the distance between two points on the Earth, given these points` coordinates.
    """
    lat_1, lon_1, lat_2, lon_2 = map(
        math.radians, [float(lat_1), float(lon_1), float(lat_2), float(lon_2)])

    lon = lon_2 - lon_1
    lat = lat_2 - lat_1

    haver = pow(math.sin(lat/2), 2) + math.cos(lat_1) * \
        math.cos(lat_2) * pow(math.sin(lon/2), 2)

    distance = 2 * 6371 * math.asin(math.sqrt(haver))

    return str(distance)


def sort_locations(locations: list) -> list:
    """
    Sorts all locations of the given year by distance and returns them.
    """
    locations.sort(key=lambda x: float(x[-1]))
    return locations


def create_map(locations: list, home_lat: float, home_lon: float):
    colors = ["red", "blue", "purple", "orange", "gray", "pink", "beige", "darkblue",\
        "cadetblue", "darkpurple"]
    geomap = folium.Map(zoom_start=10)
    fg = folium.FeatureGroup(name="Films Around Me")
    fg_1 = folium.FeatureGroup(name="Distances", show=False)
    fg_2 = folium.FeatureGroup(name="Home Layer")
    fg_2.add_child(folium.Marker(location=[home_lat, home_lon], popup="You are currently here.", icon=folium.Icon(color="green", icon="home")))
    for i in range(len(locations)):
        coords = locations[i][-2]
        lat, lon = coords[0], coords[1]
        info = locations[i][0]
        distance = locations[i][-1]
        fg.add_child(folium.Marker(location=[lat, lon], popup=info, icon=folium.Icon(color=random.choice(colors))))
        fg_1.add_child(folium.Marker(location=[lat, lon], popup=distance, icon=folium.Icon(color="darkblue", icon="plane")))
    geomap.add_child(fg_2)
    geomap.add_child(fg)
    geomap.add_child(fg_1)
    folium.TileLayer('openstreetmap').add_to(geomap)
    folium.TileLayer('Stamen Terrain').add_to(geomap)
    folium.LayerControl().add_to(geomap)
    geomap.save("filmmap.html")


def main():
    """
    Main function of the module. As of now, allows the user to enter their data and returns the result. 
    """
    print('Enter a year you would like to form a map for: ', end='')
    year = int(input())
    print('Now enter your location (format: lat, lon): ', end='')
    lat, lon = input().split(',')
    print("Generating your map, please wait...")
    locations = processing_locations(read_locations(year))
    for i in locations:
        if not isinstance(i[-1], list):
            coords = i[-1]
            try:
                coords = i[-1]
                distance = haversine(lat, lon, coords[0], coords[1])
                i.append(distance)
            except:
                "'NoneType' object is not subscriptable"
    result = []
    for i in range(len(locations)):
        if not isinstance(locations[i][-1], list):
            result.append(locations[i])
    output = sort_locations(result)
    print(output)
    create_map(output, lat, lon)
    print("Your map is ready, check it at filmmap.html")
