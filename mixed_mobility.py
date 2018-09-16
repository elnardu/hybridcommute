import googlemaps
from datetime import datetime
import urllib.request

gmaps = googlemaps.Client(key='AIzaSyDJtJibdQ9EsWs5LtdKmfCehFwk3LxJEms')

now = datetime.now()

"""allow for additional parameters here
maxwalk = 1
maxbike = 3
maxdrive = 5

use weather, etc. to minimize outside travel
use data from the car
fuel level

def has_parking(location):
    
"""
# print(gmaps.place(gmaps.geocode(start)[0]["place_id"])["result"]["url"])

def get_latlong(location):
    return gmaps.geocode(location)[0]["geometry"]["location"]

def get_routes_times(initial, final, ilist, flist, transit_mode_1, transit_mode_2, transit_mode_3):
    routes = []
    times = []
    for initial_station in ilist:
        og_route = [gmaps.directions(origin=initial, destination=initial_station, mode=transit_mode_1)]
        for final_station in flist:
            route = og_route.copy()
            route.append(gmaps.directions(origin=initial_station, destination=final_station, mode=transit_mode_2))
            route.append(gmaps.directions(origin=final_station, destination=final, mode=transit_mode_3))
            routes.append((initial_station, final_station, route))
            # routes.append(route)
    for route in routes:
        time = 0
        for leg in route[2]:
            print(leg)
            time += leg[0]['legs'][0]['duration']['value']
        times.append(time // 60)
    return (routes, times)

def get_places_nearby(latlong, subway):
    if subway:
        places = gmaps.places_nearby(location=latlong, rank_by="distance", type='subway_station')["results"]
    else:
        places = gmaps.places_nearby(location=latlong, rank_by="distance", type='train_station')["results"]
    if len(places) > 5:
        places = places[:5]
    idx = 0
    while idx < len(places):
        places[idx] = places[idx]["geometry"]["location"]
        idx += 1
    return places

start = "College of Lake County, Grayslake"
# end = "Shedd Aquarium, Chicago"

# initial = get_latlong(start)
# final = get_latlong(end)
# print(initial)

# ilist = get_places_nearby(initial)
# flist = get_places_nearby(final)

# main_routes, main_times = get_routes_times(initial, final, ilist, flist, 'driving', 'transit', 'walking')

# print(main_times)
# print(main_routes[main_times.index(min(main_times))], min(main_times))

# initial = get_latlong(start)
# print(initial)

def calc(initial, final, subway=True, reverse=False):
    # final = get_latlong(end)
    print(initial)
    print(final)

    ilist = get_places_nearby(initial, subway)
    flist = get_places_nearby(final, subway)

    if not reverse:
        main_routes, main_times = get_routes_times(initial, final, ilist, flist, 'driving', 'transit', 'walking')
    else:
        main_routes, main_times = get_routes_times(initial, final, ilist, flist, 'walking', 'transit', 'driving')
        

    # print(main_times)
    # print(main_routes[main_times.index(min(main_times))])
    return main_routes[main_times.index(min(main_times))]

__all__ = ['calc']