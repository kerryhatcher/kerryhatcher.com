__author__ = 'khatcher'
from mongoengine import connect
from os import environ
from flask_bootstrap import Bootstrap
from flask import current_app
from flask_admin import Admin


from flask.ext.security import \
    Security,\
    MongoEngineUserDatastore

from flask.ext.social import \
    Social, \
    MongoEngineConnectionDatastore, \
    login_failed


