__author__ = 'kwhatcher'


from flask.ext.wtf import Form
from wtforms import TextField, SubmitField, validators, TextAreaField

class ContactForm (Form):
    Name = TextField("Name",  [validators.Required("Name Required")])
    Email = TextField("Your Email",  [validators.Required("Email Required")])
    Message = TextAreaField("Message",  [validators.Required("Message Required")])
    submit = SubmitField("Send")