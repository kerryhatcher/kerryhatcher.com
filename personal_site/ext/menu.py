__author__ = 'khatcher'

from flask_menu import Menu


def init_app(app):
    app.menu = Menu(app=app)

