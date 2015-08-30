__author__ = 'khatcher'

from os import environ
from flask.ext.mongoengine import MongoEngine
from mongoengine import connect

connect(host=environ.get('MONGO_HOST'), ssl=True, ssl_cert_reqs=False)

db = MongoEngine()

