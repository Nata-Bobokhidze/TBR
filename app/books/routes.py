from flask import Blueprint, render_template, redirect, url_for, flash, request
import requests
from sqlalchemy.exc import SQLAlchemyError

from app.books.forms import BookForm
from .models import Book
from app.app import db
from flask_login import current_user, login_required

books = Blueprint('books', __name__, template_folder='templates')


def get_book_data(title):
    url = f'https://www.googleapis.com/books/v1/volumes?q=intitle:{title}'
    response = requests.get(url)
    data = response.json()

    if 'items' in data:
        info = data['items'][0]['volumeInfo']
        return {
            'title': info.get('title'),
            'author': ', '.join(info.get('authors', [])),
            'cover_url': info.get('imageLinks', {}).get('thumbnail'),
            'description': info.get('description', '')
        }
    return None

@books.route('/library')
@login_required
def library():
    books = Book.query.filter_by(user_id=current_user.ID).all()
    return render_template('books/library.html', books=books)


@books.route('/addbook', methods=['GET', 'POST'])
def addbook():
    form = BookForm()
    if form.validate_on_submit():
        book_data = get_book_data(form.title.data)

        new_book = Book(
            title=form.title.data,
            author=form.author.data,
            genre=form.genre.data,
            status=form.status.data,
            user_id=current_user.ID,
            mood=form.mood.data,
            length=form.length.data,
            cover_url=book_data['cover_url'] if book_data else None,
            description=book_data['description'] if book_data else None
        )

        try:
            db.session.add(new_book)
            db.session.commit()
            flash('Book added successfully!', 'success')
            return redirect(url_for('books.library'))
        except SQLAlchemyError:
            db.session.rollback()
            flash('An error occurred while adding the book.', 'error')

    return render_template('books/addbook.html', form=form)

@books.route('/update_status/<int:book_id>', methods=['POST'])
@login_required
def update_status(book_id):
    new_status = request.form.get('status')
    book = Book.query.get(book_id)

    book.status = new_status
    db.session.commit()
    flash(f"Updated reading status to {new_status}!", "success")
    return redirect(url_for('books.library'))

@books.route('/delete_book/<int:book_id>', methods=['POST'])
@login_required
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)


    db.session.delete(book)
    db.session.commit()
    flash("Book deleted.", "success")
    return redirect(url_for('books.library'))

