__author__ = 'khatcher'


from flask import (Blueprint,
                   request,
                   redirect,
                   url_for,
                   render_template,
                   session,
                   current_app,
                   flash)
from flask.ext.security import (LoginForm, current_user, login_required, login_user)
import admin
from .forms import RegisterForm

from flask.ext.social.utils import get_provider_or_404
from flask.ext.social.views import connect_handler


from .forms import RegisterForm
from .models import User

#import personal_site.modules.accounts.register

module = Blueprint('accounts', __name__, template_folder='templates', url_prefix='/user')



@module.route('/login')
def login():
    if current_user.is_authenticated():
        return redirect(request.referrer or '/')

    return render_template('login.html', form=LoginForm())


@module.route('/register', methods=['GET', 'POST'])
@module.route('/register/<provider_id>', methods=['GET', 'POST'])
def register(provider_id=None):
    if current_user.is_authenticated():
        return redirect(request.referrer or '/')

    form = RegisterForm()

    if provider_id:
        provider = get_provider_or_404(provider_id)
        connection_values = session.get('failed_login_connection', None)
    else:
        provider = None
        connection_values = None

    if form.validate_on_submit():
        ds = current_app.security.datastore
        user = ds.create_user(email=form.email.data, password=form.password.data)
        ds.commit()

        # See if there was an attempted social login prior to registering
        # and if so use the provider connect_handler to save a connection
        connection_values = session.pop('failed_login_connection', None)

        if connection_values:
            connection_values['user_id'] = user.id
            connect_handler(connection_values, provider)

        if login_user(user):
            ds.commit()
            flash('Account created successfully', 'info')
            return redirect(url_for('accounts.profile'))

        return render_template('thanks.html', user=user)

    login_failed = int(request.args.get('login_failed', 0))

    return render_template('register.html',
                           form=form,
                           provider=provider,
                           login_failed=login_failed,
                           connection_values=connection_values)

@module.route('/profile')
@login_required
def profile():
    return render_template('profile.html',
        google_conn=current_app.social.google.get_connection())
