__author__ = 'khatcher'
from flask_wtf import Form
from wtforms import StringField, \
    DateTimeField
from wtforms.validators import DataRequired

class LocationForm(Form):
    name = StringField('name', validators=[DataRequired()])
    latitude = StringField()
    longitude = StringField()
    url = StringField('URL', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    created_at = DateTimeField('created_at', validators=[DataRequired()])
