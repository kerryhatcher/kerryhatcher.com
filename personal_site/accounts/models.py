__author__ = 'khatcher'


from mongoengine import *


class Account(Document):
    url = StringField()
    Name = StringField(primary_key=True)
    user = StringField()
    password = DateTimeField()
    account_number = StringField()
