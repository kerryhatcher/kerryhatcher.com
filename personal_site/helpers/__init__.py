__author__ = 'kwhatcher'

from os import environ
import requests
import json

from postmark import PMMail

def check_recaptcha (response):
    RECAP_SECRET = environ.get('RECAP_SECRET')


    url = 'https://www.google.com/recaptcha/api/siteverify'
    payload = {'secret': RECAP_SECRET, 'response': response}
    r = requests.post(url, data=payload)
    rdata = json.loads(r.text)
    return rdata


def send_me_email(message):
    message = PMMail(api_key = environ.get('POSTMARK_API_TOKEN'),
                     subject = "Hello from Postmark",
                     sender = "mail.bot@kerryhatcher.com",
                     to = "kwhatcher@gmail.com",
                     text_body = message,
                     tag = "hello")

    message.send()