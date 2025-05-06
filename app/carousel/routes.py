from flask import Blueprint, render_template

carousel = Blueprint('carousel', __name__, template_folder='templates')

@carousel.route('/carousel')
def setup():
    return render_template('carousel/setup.html')