from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app.app import db

class User(db.Model, UserMixin):
    __tablename__ = 'Users'
    ID = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=True)
    password = db.Column(db.String, nullable=False)

    books = db.relationship('Book', backref='owner', lazy=True)

    def __repr__(self):
        return f'User: {self.username}, Role: {self.role}, Description: {self.description}'

    def get_id(self):
        return self.ID