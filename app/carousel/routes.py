from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.app import db
from app.books.models import Book
import random

carousel = Blueprint('carousel', __name__, template_folder='templates/carousel')

# @carousel.route('/carousel')
# def carousel():
#     return render_template('carousel/carousel_start.html')

@carousel.route('/carousel', methods=['GET'])
@login_required
def carousel_start():
    return render_template('carousel_start.html')


@carousel.route('/filter', methods=['GET', 'POST'])
@login_required
def filter_form():
    if Book.query.filter_by(user_id=current_user.ID).count() == 0:
        flash("You need to add books to your library before spinning!", "info")
        return redirect(url_for('books.my_library'))

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
        ('other', 'Other')
    ]

    MOOD_CHOICES = [
        ('lighthearted', 'Lighthearted'),
        ('emotional', 'Emotional'),
        ('adventurous', 'Adventurous'),
        ('dark', 'Dark'),
        ('inspirational', 'Inspirational'),
        ('romantic', 'Romantic'),
        ('mysterious', 'Mysterious'),
        ('funny', 'Funny')
    ]

    LENGTH_CHOICES = [
        ('thin', 'Thin (under 200 pages)'),
        ('average', 'Average (200–400 pages)'),
        ('thick', 'Thick (400+ pages)')
    ]
    if request.method == 'POST':
        genre = request.form.get('genre')
        mood = request.form.get('mood')
        length = request.form.get('length')
        author = request.form.get('author', '').strip().lower()

        books = Book.query.filter_by(user_id=current_user.ID)

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
            flash("No books matched your filter. Try adjusting your criteria!", "warning")
            return redirect(url_for('carousel.filter_form'))

        random.shuffle(books)
        return render_template('carousel_start.html', books=books)

    return render_template('filter_form.html', genres=GENRE_CHOICES, moods=MOOD_CHOICES, lengths=LENGTH_CHOICES)


@carousel.route('/start-reading/<int:book_id>')
@login_required
def start_reading(book_id):
    book = Book.query.filter_by(id=book_id, user_id=current_user.ID).first()
    if book:
        book.status = 'reading'
        db.session.commit()
        flash(f"You’ve started reading {book.title}!", 'success')
    return redirect(url_for('core.dashboard'))

@carousel.route('/wheel', methods=['POST'])
@login_required
def wheel():
    if Book.query.filter_by(user_id=current_user.ID).count() == 0:
        flash("You need to add books to your library before spinning!", "info")
        return redirect(url_for('books.my_library'))

    genre = request.form.get('genre')
    mood = request.form.get('mood')
    length = request.form.get('length')
    author = request.form.get('author', '').strip().lower()

    books = Book.query.filter_by(user_id=current_user.ID)
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
        return redirect(url_for('carousel.filter_form'))

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
        }
        for book in books
    ]

    return render_template('carousel_wheel.html', books=books_data)

