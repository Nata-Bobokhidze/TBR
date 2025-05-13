from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.app import db
from app.books.models import Book
import random

carousel = Blueprint('carousel', __name__, template_folder='templates/carousel')

@carousel.route('/carousel', methods=['GET'])
@login_required
def carousel_start():
    return render_template('carousel_start.html')


@carousel.route('/start-reading/<int:book_id>')
@login_required
def start_reading(book_id):
    book = Book.query.filter_by(id=book_id, user_id=current_user.ID).first()
    if book:
        book.status = 'reading'
        db.session.commit()
        flash(f"You’ve started reading {book.title}!", 'success')
    return redirect(url_for('core.dashboard'))

@carousel.route('/wheel', methods=['GET','POST'])
@login_required
def wheel():
    if Book.query.filter_by(user_id=current_user.ID).count() == 0:
        flash("You need to add books to your library before spinning!", "info")
        return redirect(url_for('books.library'))

    GENRE_CHOICES = [
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
    ]

    MOOD_CHOICES = [
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
    ]

    LENGTH_CHOICES = [
        ('thin', 'Thin (under 200 pages)'),
        ('average', 'Average (200–400 pages)'),
        ('thick', 'Thick (400+ pages)')
    ]

    if request.method == 'GET':
        return render_template('filter_form.html',
                               genres=GENRE_CHOICES,
                               moods=MOOD_CHOICES, lengths=LENGTH_CHOICES)


    genre = request.form.get('genre')
    mood = request.form.get('mood')
    length = request.form.get('length')
    author = request.form.get('author', '').strip().lower()

    books = Book.query.filter_by(user_id=current_user.ID, status='To Be Read')
    eligible = books.count()
    if eligible == 0:
        flash("No books are eligible for spinning. Either read them all or DNF", "info")
        return redirect(url_for('books.library'))
    # print("Eligible statuses:", [b.status for b in books.all()])

    if genre:
        books = books.filter(Book.genre == genre)
    if mood:
        books = books.filter(Book.mood == mood)
    if length:
        books = books.filter(Book.length == length)
    if author:
        books = books.filter(Book.author.ilike(f'%{author}%'))

    books = books.all()

    if not books:
        flash("No books matched your filter. Try again!", "warning")
        return redirect(url_for('carousel.wheel'))

    if len(books) == 1:
        book = books[0]
        flash(f"Only one match: {book.title}", "info")
        return redirect(url_for('carousel.start_reading', book_id=book.id))

    random.shuffle(books)

    books_data = [
        {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'genre': book.genre,
            'mood': book.mood,
            'length': book.length,
            'description': book.description
        }
        for book in books
    ]

    return render_template('carousel_wheel.html', books=books_data)

