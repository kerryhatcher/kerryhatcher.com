__author__ = 'kwhatcher'

from os import environ

from flask import Flask
from flask import render_template

from flask_bootstrap import Bootstrap

from mongoengine import connect

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

@app.route('/')
def hello_world():
    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404