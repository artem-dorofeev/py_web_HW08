from connect import db
from mongoengine import *


class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=50)
    description = StringField()
    # meta = {'allow_inheritance': True}


class Quote(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField(max_length=150, required=True)
    # meta = {'allow_inheritance': True}

# from mongoengine import Document, StringField, BooleanField

class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    email_sent = BooleanField(default=False)