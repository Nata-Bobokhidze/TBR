from app.app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'Users'
    ID = db.Column(db.Integer, primary_key = True )
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    username =  db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False, unique = True)
    # email = db.Column(db.String, nullable = True)
    password = db.Column(db.String, nullable = False)

    books = db.relationship('Book', backref='owner', lazy=True)

    def __repr__(self):
        return f'User: {self.username}'

    def get_id(self):
        return self.ID