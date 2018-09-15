from pymongo import MongoClient, GEOSPHERE

db = MongoClient('localhost', 27017).hybridcommute
col = db.locations


def getNearest(type_: str, lon: float, lat: float):
    return col.find_one({
        'type': type_,
        'loc': {
            '$near': {
                '$geometry': {
                    'type': "Point",
                    'coordinates': [lon, lat]
                },
                '$maxDistance': 10000
            }
        }
    })

# print(getNearest('car_parking', -71.07916, 42.34840))
# print(getNearest('bicycle_rental', -71.07916, 42.34840))

def getInRange(type_: str, lon: float, lat: float, radius: float):
    return list(col.find({
        'type': type_,
        'loc': {
            '$geoWithin': {
                '$centerSphere': [[lon, lat], radius / (6378.1 * 1000)]
            }
        }
    }))

# print(getInRange('bicycle_rental', -71.077303, 42.349673, 20))