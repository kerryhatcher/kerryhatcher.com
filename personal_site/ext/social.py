__author__ = 'khatcher'

from flask.ext.social import \
    Social, \
    MongoEngineConnectionDatastore, \
    login_failed

from personal_site.modules.accounts.models import Connection


def init_app(app, db):
    social_ds = MongoEngineConnectionDatastore(db, Connection)
    app.social = Social(app, social_ds)
