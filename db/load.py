from pymongo import MongoClient, GEOSPHERE
from bs4 import BeautifulSoup

db = MongoClient('localhost', 27017).hybridcommute
col = db.locations

col.create_index([('loc', GEOSPHERE), ('type', 1)])
col.create_index('id', unique=True)

with open('map.xml', 'r') as f:
    soup = BeautifulSoup(f, "lxml")

def matchNodesWithTag(tag):
    if tag.name == 'node':
        for child in tag.children:
            if child.name == 'tag':
                return True

    return False

def getNodesByKV(nodes, key, value):
    res = []
    for node in nodes:
        for child in node.find_all('tag'):
            if child['k'] == key and child['v'] == value:
               res.append(node)
    return res

def processNodes(nodes, typeValue):
    res = []
    for node in nodes:
        res.append({
            'id': node['id'],
            'loc': [
                float(node['lon']),
                float(node['lat'])
            ],
            'type': typeValue
        })
    return res

def loadNodes(col, nodes, key, value, typeValue):
    try:
        res = col.insert_many(processNodes(getNodesByKV(nodes, key, value), typeValue))
    except Exception as bwe:
        print(bwe.details)
    print(typeValue, len(res.inserted_ids))

f = soup.find_all(matchNodesWithTag)
loadNodes(col, f, 'amenity', 'parking', 'car_parking')
loadNodes(col, f, 'amenity', 'bicycle_rental', 'bicycle_rental')
loadNodes(col, f, 'station', 'subway', 'subway')