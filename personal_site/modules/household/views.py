__author__ = 'khatcher'

from os import environ

from flask.views import MethodView
from flask import render_template
from flask import abort
from personal_site.core.tools import cryptdata, decryptdata
from models import Account

class DetailView(MethodView):

    def get_context(self, slug):
        try:
            account = Account.objects.get(url=slug)
        except:
            abort(404)

        account.password = decryptdata(account.password, environ.get('CRYPT_PASS'))
        account.user = decryptdata(account.user, environ.get('CRYPT_PASS'))

        context = {
            "account": account,
            "slug": slug
        }
        return context

    def get(self, slug):
        context = self.get_context(slug)
        return render_template('household/detail.html', **context)