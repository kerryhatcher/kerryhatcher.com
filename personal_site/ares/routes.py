__author__ = 'kwhatcher'
from flask import Blueprint
from flask import render_template
from flask import request

ares = Blueprint('ares', __name__,
                    template_folder='templates')


@ares.route('/')
def ares_root():
    return render_template('aresroot.html')