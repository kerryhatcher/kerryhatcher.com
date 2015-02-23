__author__ = 'kwhatcher'


from flask.ext.wtf import Form
from wtforms import TextField, SubmitField, validators, TextAreaField

class NewPostForm (Form):
    URI = TextField("URI",  [validators.Required("URI Required")])
    Title = TextField("Title",  [validators.Required("Title Required")])
    Content = TextAreaField("Content",  [validators.Required("Content Required")])
