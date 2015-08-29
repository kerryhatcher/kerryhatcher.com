__author__ = 'khatcher'

from flask import Blueprint
from flask import render_template

accounts = Blueprint('accounts', __name__,
                    template_folder='templates')



@accounts.route('/')
def ares_root():
    return render_template('accounts/root.html')