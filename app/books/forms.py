from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField, SelectField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[])
    status = SelectField('Status', choices=[ ('To Be Read', 'To Be Read'), ('Reading', 'Reading'), ('Read', 'Read'), ('DNF', 'DNF') ], default='To_read')
    genre = SelectField('Genre', validators=[DataRequired()], choices=[
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
        ('other', 'Other'),
        ('cozy_fantasy', 'Cozy Fantasy'),
        ('regency_romp', 'Regency Romp'),
        ('epic_quest', 'Epic Quest'),
        ('space_odyssey', 'Space Odyssey'),
        ('dark_academia', 'Dark Academia'),
        ('slice_of_life', 'Slice of Life'),
        ('mythical_retellings', 'Mythical Retellings'),
        ('haunted_mansion', 'Haunted Mansion Mystery'),
        ('fairytale_gone_wrong', 'Fairytale Gone Wrong'),
        ('gentle_classics', 'Gentle Classics'),
        ('time_travel', 'Time Travel Tangle'),
        ('bookish_misc', 'Bookish Miscellany')
    ])
    mood = SelectField('Mood', validators=[DataRequired()], choices=[
        ('lighthearted', 'Lighthearted'),
        ('emotional', 'Emotional'),
        ('adventurous', 'Adventurous'),
        ('dark', 'Dark'),
        ('inspirational', 'Inspirational'),
        ('romantic', 'Romantic'),
        ('mysterious', 'Mysterious'),
        ('funny', 'Funny'),
        ('wholesome', 'Wholesome'),
        ('gut_punching', 'Gut-Punching'),
        ('cozy', 'Cozy & Comforting'),
        ('bittersweet', 'Bittersweet'),
        ('spooky', 'Spooky & Strange'),
        ('swoonworthy', 'Swoonworthy'),
        ('page_turner', 'Can’t Put Down'),
        ('existential', 'Existential Crisis Fuel'),
        ('wanderlusty', 'Wanderlusty')
    ])

    length = SelectField('Length', choices=[
        ('thin', 'Thin (under 200 pages)'),
        ('average', 'Average (200–400 pages)'),
        ('thick', 'Thick (400+ pages)')
    ])

    submit = SubmitField('Add Book')
