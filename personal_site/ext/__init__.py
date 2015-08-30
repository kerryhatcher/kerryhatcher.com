__author__ = 'khatcher'

from personal_site.core.db import db
from personal_site.core.admin import configure_admin

from . import (security,
               bootstrap,
               social,
               blueprints,
               menu)


def configure_extensions(app, admin):
    #db.init_app(app)
    security.init_app(app, db)
    bootstrap.init_app(app)
    social.init_app(app, db)
    configure_admin(app, admin)
    blueprints.load_from_folder(app)
    menu.init_app(app)


