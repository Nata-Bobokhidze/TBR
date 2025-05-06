from flask import Blueprint, render_template, redirect, url_for
from flask_login import logout_user, login_user
from app.app import db
from .forms import LoginForm, SignupForm
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = generate_password_hash(form.password.data)

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('auth/signup.html', form=form)

    # return '<h1>Sign Up</h1>'

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('core.dashboard'))
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.welcome'))
