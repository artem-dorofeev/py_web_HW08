from pymongo import MongoClient
from pymongo.server_api import ServerApi

# client = MongoClient(
#     "mongodb+srv://<username>:<password>@krabaton.5mlpr.gcp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
#     server_api=ServerApi('1')
# )

uri = "mongodb+srv://userhv08:567234@cluster0.unyspy8.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


db = client.book

result_one = db.cats.insert_one(
    {
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"],
    }
)

