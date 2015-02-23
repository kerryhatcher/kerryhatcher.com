__author__ = 'kwhatcher'
from mongoengine import *


class Post(Document):
    url = StringField(primary_key=True, max_length=120, required=True)
    Title = StringField(required=True)
    Content = StringField(required=True)
    PostDate = DateTimeField()
    tags = ListField(StringField(max_length=30))


