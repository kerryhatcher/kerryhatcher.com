__author__ = 'kwhatcher'

from flask import Flask


from .core.admin import create_admin
admin = create_admin()



def create_app_base(config=None, test=False, admin_instance=None, **settings):
    app = Flask(__name__)
    return app


def create_app(config=None, test=False, admin_instance=None, **settings):
    app = create_app_base(
        config=config, test=test, admin_instance=admin_instance, **settings
    )
    app.config.from_pyfile('config.py')
    from .ext import configure_extensions
    configure_extensions(app, admin_instance or admin)
    return app

