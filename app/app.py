from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = 'mysecret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tbr.db'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from app.models import User
    @login_manager.user_loader
    def load_user(ID):
        return User.query.get(int(ID))

    from app.books.models import Book

    # import and register all blueprints
    from app.core.routes import core
    app.register_blueprint(core, url_prefix='/')

    from app.auth.routes import auth
    app.register_blueprint(auth, url_prefix='/')

    from app.books.routes import books
    app.register_blueprint(books, url_prefix='/books')

    from app.carousel.routes import carousel
    app.register_blueprint(carousel, url_prefix='/carousel')


    migrate = Migrate(app, db)


    return app
