
from flask.ext.security.forms import RegisterForm, Required
from flask.ext.security import Security as Security
from flask.ext.security import MongoEngineUserDatastore
from wtforms import TextField
from personal_site.modules.accounts.models import Role, User
from personal_site.core.templates import render_template
from personal_site import admin
from flask_admin import helpers as admin_helpers



def init_app(app, db):
    app.security = Security(app, MongoEngineUserDatastore(db, User, Role),)

