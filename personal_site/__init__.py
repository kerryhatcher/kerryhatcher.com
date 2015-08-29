__author__ = 'kwhatcher'

#python standard imports
import sys
import logging

from os import environ



#addon imports
from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session
from flask_bootstrap import Bootstrap
from mongoengine import connect

from raygun4py import raygunprovider

from flask.ext.security import \
    Security,\
    MongoEngineUserDatastore

from flask.ext.social import \
    Social, \
    MongoEngineConnectionDatastore, \
    login_failed

from flask.ext.social.utils import get_connection_values_from_oauth_response
from flask_admin import Admin


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    db = connect(host=app.config['DB_HOST'], ssl=True, ssl_cert_reqs=False)
    admin = Admin(app, name='microblog', template_mode='bootstrap3')
    Bootstrap(app)

    from personal_site.site import models

    security_ds = MongoEngineUserDatastore(db, models.User, models.Role)
    social_ds = MongoEngineConnectionDatastore(db, models.Connection)


    app.security = Security(app, security_ds)
    app.social = Social(app, social_ds)

    #Application Imports
    from site import site
    from personal_site.blog.routes import blog
    from personal_site.contact.routes import contact
    from ares.routes import ares
    from accounts import accounts
    from blight import blight
    app.register_blueprint(site, url_prefix='/')
    app.register_blueprint(blog, url_prefix='/blog')
    app.register_blueprint(contact, url_prefix='/contact')
    app.register_blueprint(ares, url_prefix='/radio')
    app.register_blueprint(accounts, url_prefix='/accounts')
    app.register_blueprint(blight, url_prefix='/blight')


    @login_failed.connect_via(app)
    def on_login_failed(sender, provider, oauth_response):
        print(oauth_response)
        app.logger.debug('Social Login Failed via %s; '
                         '&oauth_response=%s' % (provider.name, oauth_response))

        # Save the oauth response in the session so we can make the connection
        # later after the user possibly registers
        session['failed_login_connection'] = \
            get_connection_values_from_oauth_response(provider, oauth_response)

        raise SocialLoginError(provider)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(SocialLoginError)
    def social_login_error(error):
        return redirect(
            url_for('register', provider_id=error.provider.id, login_failed=1))

    return app

logger = logging.getLogger("mylogger")

rgHandler = raygunprovider.RaygunHandler(environ.get('RAYGUN_APIKEY'))
raygun = raygunprovider.RaygunSender(environ.get('RAYGUN_APIKEY'))
logger.addHandler(rgHandler)


def log_exception(exc_type, exc_value, exc_traceback):
    print "Logging: %s" % exc_value
    logger.error("A python error occurred", exc_info = (exc_type, exc_value, exc_traceback))

sys.excepthook = log_exception


class SocialLoginError(Exception):
    def __init__(self, provider):
        self.provider = provider




