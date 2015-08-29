__author__ = 'khatcher'
from flask import url_for
import datetime
from mongoengine import *

class Event(EmbeddedDocument):
    created_at = DateTimeField(default=datetime.datetime.now, required=True)
    body = StringField(verbose_name="Event", required=True)

class Location(Document):
    point = GeoPointField()
    events = ListField(EmbeddedDocumentField('Event'))
    url = StringField(max_length=255, required=True)
    title = StringField(max_length=255, required=True)
    address = StringField(max_length=255, required=True)
    created_at = DateTimeField(default=datetime.datetime.now, required=True)
    scf_issues = ListField(StringField())

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.url})

    def __unicode__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['url'],
        'ordering': ['-created_at']
    }



