from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    # genre = SelectField('Genre')
    status = SelectField('Status', choices=[('to_read', 'To Read'), ('reading', 'Reading'), ('read', 'Read')])
    genre = SelectField('Genre', choices=[
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-Fiction'),
        ('fantasy', 'Fantasy'),
        ('sci-fi', 'Science Fiction'),
        ('romance', 'Romance'),
        ('mystery', 'Mystery'),
        ('thriller', 'Thriller'),
        ('historical', 'Historical Fiction'),
        ('memoir', 'Memoir'),
        ('biography', 'Biography'),
        ('self_help', 'Self-Help'),
        ('poetry', 'Poetry'),
        ('other', 'Other')
    ])
    mood = SelectField('Mood', choices=[
        ('lighthearted', 'Lighthearted'),
        ('emotional', 'Emotional'),
        ('adventurous', 'Adventurous'),
        ('dark', 'Dark'),
        ('inspirational', 'Inspirational'),
        ('romantic', 'Romantic'),
        ('mysterious', 'Mysterious'),
        ('funny', 'Funny')
    ])

    length = SelectField('Length', choices=[
        ('thin', 'Thin (under 200 pages)'),
        ('average', 'Average (200–400 pages)'),
        ('thick', 'Thick (400+ pages)')
    ])

    submit = SubmitField('Add Book')
