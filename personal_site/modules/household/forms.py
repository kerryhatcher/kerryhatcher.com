__author__ = 'khatcher'

from flask.ext.mongoengine.wtf import model_form
from flask_wtf import Form
from .models import Account

AccountForm = model_form(Account, Form)

