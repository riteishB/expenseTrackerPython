from pymongo import MongoClient
import config

client = MongoClient()
uri = "mongodb://" + config.MONGO_USER + ":" + \
    config.MONGO_PASSWORD + "@ds115022.mlab.com:15022/expense-tracker"
client = MongoClient(uri)
db = client['expense-tracker']
collection = db['expenses']


def getCollection():
    return collection
