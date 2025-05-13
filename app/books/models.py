from app.app import db

class Book(db.Model):
    __tablename__ = 'Books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String)
    genre = db.Column(db.String)
    mood = db.Column(db.String)
    length = db.Column(db.String)  # this will be thin, avarage, thick in the form
    status = db.Column(db.String)  # this will have reading, finished, dnf options
    user_id = db.Column(db.Integer, db.ForeignKey('Users.ID'), nullable=False)
    cover_url = db.Column(db.String)  # the book cover image
    description = db.Column(db.Text)  # for small summary from google
