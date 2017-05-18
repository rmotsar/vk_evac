from pymongo import MongoClient

from settings import MONGO_SERVER, MONGO_PORT

client = MongoClient(MONGO_SERVER, MONGO_PORT)
db = client.vk
