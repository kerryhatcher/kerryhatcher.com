__author__ = 'khatcher'

from mongoengine import *
from flask.ext.security import UserMixin, RoleMixin

class Role(Document, RoleMixin):
    name = StringField(max_length=80, unique=True)
    description = StringField(max_length=255)

class User(Document, UserMixin):
    email = StringField(unique=True, max_length=255)
    password = StringField(required=True, max_length=120)
    active = BooleanField(default=True)
    remember_token = StringField(max_length=255)
    full_name=StringField(max_length=255)
    display_name = StringField(max_length=255)
    authentication_token = StringField(max_length=255)
    roles = ListField(ReferenceField(Role), default=[])

    @property
    def connections(self):
        return Connection.objects(user_id=str(self.id))

class Connection(Document):
    user_id = ObjectIdField()
    provider_id = StringField(max_length=255)
    provider_user_id = StringField(max_length=255)
    access_token = StringField(max_length=255)
    secret = StringField(max_length=255)
    display_name = DictField()
    full_name = DictField()
    profile_url = StringField(max_length=512)
    image_url = StringField(max_length=512)
    rank = IntField(default=1)

    @property
    def user(self):
        return User.objects(id=self.user_id).first()


