from pymongo import MongoClient, GEOSPHERE
from bs4 import BeautifulSoup

db = MongoClient('localhost', 27017).hybridcommute
col = db.locations