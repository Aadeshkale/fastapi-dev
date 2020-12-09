from mongoengine import *
import datetime


class Todo(Document):
    id = StringField(primary_key=True, required=True)
    todo_info = StringField(max_length=600, required=True)
    date_modified = DateTimeField(default=datetime.datetime.utcnow, required=True)
