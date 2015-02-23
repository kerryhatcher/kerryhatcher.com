__author__ = 'kwhatcher'

from os import environ

from flask import Blueprint
from flask import render_template
from flask import request
from flask import flash

from forms import ContactForm
from personal_site.helpers import check_recaptcha
from personal_site.helpers import send_me_email

contact = Blueprint('contact', __name__,
                    template_folder='templates')


@contact.route('/', methods=('GET', 'POST'))
def contact_home():
    form = ContactForm()
    if request.method == 'POST':
        recap = check_recaptcha(request.form['g-recaptcha-response'])
        if recap['success']:
            print "It worked"
            flash("It worked")
            send_me_email(form.Message.data)
        else:
            flash("reCaptcha status:" + str(recap['success']))
            return render_template('contactbase.html', form=form)
        return render_template('contactsubmit.html', contactor=form.Name.data)

    if request.method == 'GET':
        return render_template('contactbase.html', form=form)


