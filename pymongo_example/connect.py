from pymongo import MongoClient
from pymongo.server_api import ServerApi


# uri = "mongodb+srv://userhw08:567234@cluster0.unyspy8.mongodb.net/?retryWrites=true&w=majority"
uri = "mongodb+srv://userhw08:567234@cluster0.unyspy8.mongodb.net/"


# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


db = client.web8


result = db.privat.find()
print("17 ok")

if __name__ == '__main__':
    print(result)
    # for i in result:
    #     print(i)

