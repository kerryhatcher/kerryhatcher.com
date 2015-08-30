from os import environ
import os

# Create dummy secrey key so we can use sessions
SECRET_KEY = environ.get('SECRET_KEY')

# Create in-memory database
##DATABASE_FILE = 'sample_db.sqlite'
##SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
##SQLALCHEMY_ECHO = True

# Flask-Security config
##SECURITY_URL_PREFIX = "/admin"
##SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
##SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"

# Flask-Security URLs, overridden because they don't put a / at the end
##SECURITY_LOGIN_URL = "/login/"
##SECURITY_LOGOUT_URL = "/logout/"
##SECURITY_REGISTER_URL = "/register/"

##SECURITY_POST_LOGIN_VIEW = "/admin/"
##SECURITY_POST_LOGOUT_VIEW = "/admin/"
##SECURITY_POST_REGISTER_VIEW = "/admin/"

# Flask-Security features
##SECURITY_REGISTERABLE = True
##SECURITY_SEND_REGISTER_EMAIL = False


SOCIAL_GOOGLE = {
    'consumer_key': environ.get('GOOGLE_KEY'),
    'consumer_secret': environ.get('GOOGLE_SECRET')
}





MONGODB_SETTINGS = {
    'db': 'project1',
    'host': environ.get('MONGO_HOST')
}

ADMIN = {'name': 'Hatch Admin', 'url': '/admin'}

"""
Blueprints are modules, you don't need to install
just develop or download and drop in your modules folder
by default it is in ./modules, you can change if needed
"""
BLUEPRINTS_PATH = 'modules'
BLUEPRINTS_OBJECT_NAME = 'module'


"""
Not needed by flask, but those root folders are used
by FLask-Admin file manager
"""
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'mediafiles')
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
ROOT_DIR = os.path.abspath(os.path.join(PROJECT_ROOT, '..'))
