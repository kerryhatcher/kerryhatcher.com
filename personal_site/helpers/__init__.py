__author__ = 'kwhatcher'

from os import environ
import sys
import requests
import json

from flask import current_app

from postmark import PMMail

from flask.ext.pystmark import Pystmark, Message
from pystmark import ResponseError

from raygun4py import raygunprovider

raygun = raygunprovider.RaygunSender(environ.get('RAYGUN_APIKEY'))

#pystmark = Pystmark(current_app)

def check_recaptcha (response):
    RECAP_SECRET = environ.get('RECAP_SECRET')


    url = 'https://www.google.com/recaptcha/api/siteverify'
    payload = {'secret': RECAP_SECRET, 'response': response}
    r = requests.post(url, data=payload)
    rdata = json.loads(r.text)
    return rdata


def send_me_email(message):
    #m = Message(to='user@gmail.com', text='Welcome')
    #resp = pystmark.send(m)
    send_item_to_raygun(message)


def send_error_to_raygun():
        err = sys.exc_info()
        raygun.send(err[0], err[1], err[2])


def send_item_to_raygun(message):
        err = sys.exc_info()
        raygun.send(message)