from app.app import db
from app.models import User
from .forms import LoginForm, SignupForm
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import logout_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form  = SignupForm()
    if form.validate_on_submit():
        name =  form.name.data
        surname = form.surname.data
        username = form.username.data
        email = form.email.data
        password = generate_password_hash(form.password.data)

        new_user = User(name = name, surname = surname, username = username, email = email, password = password)
        if User.query.filter_by(username = username).first():
            flash('Username is already taken. Please do not be sad and choose another one!', 'info')
            return render_template("auth/signup.html", form=form)
        if User.query.filter_by(email = email).first():
            flash('User with this email is already registered.', 'info')
            return render_template("auth/signup.html", form=form)

        db.session.add(new_user)
        db.session.commit()
        flash('Account created! Please log in now!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', form=form)

@auth.route('login', methods = ['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username = username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash(f'Welcome back {user.username}!', 'success')
            return redirect(url_for('core.dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password.', 'danger')
            return redirect(url_for('auth.login'))
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out!', 'success')
    return redirect(url_for('core.welcome'))
