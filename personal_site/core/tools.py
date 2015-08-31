__author__ = 'khatcher'
from Crypto.Cipher import AES
import base64
from os import environ
import requests
import json


def cryptdata(data, password):
    cipher = AES.new(password,AES.MODE_ECB)
    encoded = base64.b64encode(cipher.encrypt(data.rjust(32)))
    return encoded


def decryptdata(data, password):
    cipher = AES.new(password,AES.MODE_ECB)
    decoded = cipher.decrypt(base64.b64decode(data))
    return decoded


def check_recaptcha (response):
    RECAP_SECRET = environ.get('RECAP_SECRET')


    url = 'https://www.google.com/recaptcha/api/siteverify'
    payload = {'secret': RECAP_SECRET, 'response': response}
    r = requests.post(url, data=payload)
    rdata = json.loads(r.text)
    print rdata
    return rdata


def send_me_email(message):
    print(message)
    from mailgun2 import Mailgun
    mailer = Mailgun(environ.get('MAILGUN_KEY'), environ.get('MAILGUN_DOMAIN'))
    mailer.send_message(
        'contact_form@kerryhatcher.com',
        ['kwhatcher@gmail.com'],
        subject='Email from' + message.Name.data + "[" + message.Email.data + "]",
        text=message.Message.data
        )
    pass


def print_members(input):
    for item in input:
        print item