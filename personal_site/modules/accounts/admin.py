__author__ = 'khatcher'

# coding : utf -8
from wtforms.fields import TextField
from wtforms.widgets import PasswordInput
from flask.ext.admin.contrib.mongoengine import ModelView
from personal_site.core.admin.models import PersonalSiteModelView
from personal_site import admin
from .models import Role, User, Connection



class UserAdmin(PersonalSiteModelView):
    pass

class RoleAdmin(PersonalSiteModelView):
    roles_accepted = ('admin', )
    column_list = ('name', 'description')


class ConnectionAdmin(PersonalSiteModelView):
    roles_accepted = ('admin',)


admin.add_view(UserAdmin(User))
admin.add_view(RoleAdmin(Role))
admin.add_view(ConnectionAdmin(Connection))
