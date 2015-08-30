__author__ = 'khatcher'

from flask.ext.admin.contrib.mongoengine import ModelView
from personal_site.core.admin.models import PersonalSiteModelView
from personal_site import admin
from models import Post

class BlogAdmin(PersonalSiteModelView):
    pass

admin.add_view(BlogAdmin(Post))