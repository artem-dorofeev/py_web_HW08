from pymongo import MongoClient
from pymongo.server_api import ServerApi
from mongoengine import *

import configparser


config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
# mongo_name = config.get('DB', 'mongo_name')
mongo_uri = config.get('DB', 'mongo_uri')

uri = f"mongodb+srv://{mongo_user}:{mongodb_pass}@{mongo_uri}"
# Create a new client and connect to the server


db = connect(host=uri, ssl=True, db="web8")

# Send a ping to confirm a successful connection
# try:
#     db.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

client = MongoClient(uri, server_api=ServerApi('1'))

