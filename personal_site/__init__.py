__author__ = 'kwhatcher'

from os import environ
import sys, logging, os

from flask import Flask
from flask import render_template

from flask_bootstrap import Bootstrap

from mongoengine import connect

from raygun4py import raygunprovider

from personal_site.blog.routes import blog
from personal_site.contact.routes import contact
from ares.routes import ares

app = Flask(__name__)



app.register_blueprint(blog, url_prefix='/blog')
app.register_blueprint(contact, url_prefix='/contact')
app.register_blueprint(ares, url_prefix='/radio')

Bootstrap(app)
connect('sdf', host=environ.get('MONGOLAB_URI'))

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')


logger = logging.getLogger("mylogger")

rgHandler = raygunprovider.RaygunHandler(environ.get('RAYGUN_APIKEY'))
raygun = raygunprovider.RaygunSender(environ.get('RAYGUN_APIKEY'))
logger.addHandler(rgHandler)

def log_exception(exc_type, exc_value, exc_traceback):
    print "Logging: %s" % exc_value
    logger.error("A python error occurred", exc_info = (exc_type, exc_value, exc_traceback))

sys.excepthook = log_exception

@app.route('/')
def hello_world():
    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
        send_error_to_raygun()
        return '500 error: ' + error.args[0]

def send_error_to_raygun():
        err = sys.exc_info()
        raygun.send(err[0], err[1], err[2])