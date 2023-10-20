import argparse
from functools import wraps
from pprint import pprint
from bson.objectid import ObjectId

from pymongo import MongoClient


# client = MongoClient("mongodb://localhost:27017")
client = MongoClient("mongodb+srv://userhw08:567234@cluster0.unyspy8.mongodb.net/?retryWrites=true&w=majority")
db = client.web8

parser = argparse.ArgumentParser(description='Cats APP')
parser.add_argument('--action', help='Command: create, update, find, remove')
parser.add_argument('--id')
parser.add_argument('--name')
parser.add_argument('--age')
parser.add_argument('--features', nargs='+')

arguments = parser.parse_args()
my_arg = vars(arguments)

action = my_arg.get('action')
name = my_arg.get('name')
age = my_arg.get('age')
_id = my_arg.get('id')
features = my_arg.get('features')


class ExceptionValidation(Exception):
    pass


def validate(func):
    @wraps(func)
    def wrapper(*args):
        for el in args:
            if el is None:
                raise ExceptionValidation(f'Вхідні данні не валідні: {func.__name__}{args}')
        result = func(*args)
        return result

    return wrapper


def find_by_id(_id):
    result = db.cats.find_one({"_id": ObjectId(_id)})
    return result


@validate
def create(name: str, age: str, features: list):
    result = db.cats.insert_one({
        "name": name,
        "age": int(age),
        "features": features
    })
    return find_by_id(result.inserted_id)


@validate
def find():
    return db.cats.find()


@validate
def update(_id, name: str, age: str, features: list):
    r = db.cats.update_one({"_id": ObjectId(_id)}, {
        "$set": {
            "name": name,
            "age": int(age),
            "features": features
        }
    })
    pprint(r)
    return find_by_id(_id)


@validate
def remove(_id):
    r = db.cats.delete_one({"_id": ObjectId(_id)})
    return r


def main():
    try:
        match action:
            case 'create':
                r = create(name, age, features)
                pprint(r)
            case 'find':
                r = find()
                [pprint(el) for el in r]
            case 'update':
                r = update(_id, name, age, features)
                pprint(r)
            case 'remove':
                r = remove(_id)
                pprint(r)
            case _:
                pprint('Unknowns command')
    except ExceptionValidation as err:
        pprint(err)


if __name__ == '__main__':
    main()
    # print(find_by_id('6318d73f74bc292c95cdaa3d'))