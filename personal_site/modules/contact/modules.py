__author__ = 'khatcher'

from personal_site.core.db import db

class ContactMessage(db.Document):
    email = db.StringField()
    name = db.StringField()
    message = db.StringField()