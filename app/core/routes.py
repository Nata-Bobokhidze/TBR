from flask import Blueprint, render_template
from flask_login import login_required, current_user

core = Blueprint('core', __name__, template_folder='templates')

@core.route('/')
def welcome():
    return render_template('core/welcome.html')

@core.route('/about')
def about():
    return render_template('core/about.html')

@core.route('/dashboard')
@login_required
def dashboard():
    return render_template('core/dashboard.html', user = current_user)