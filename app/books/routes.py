from flask import Blueprint, render_template, redirect, url_for, flash
from sqlalchemy.exc import SQLAlchemyError

from books.forms import BookForm
from .models import Book
from app.app import db
from flask_login import current_user, login_required

books = Blueprint('books', __name__, template_folder='templates')

@books.route('/library')
@login_required
def library():
    books = Book.query.filter_by(user_id=current_user.ID).all()
    return render_template('books/library.html', books=books)


@books.route('/addbook', methods=['GET', 'POST'])
def addbook():
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(
            title=form.title.data,
            author=form.author.data,
            genre=form.genre.data,
            status=form.status.data,
            user_id=current_user.ID,
            mood=form.mood.data,
            length=form.length.data,
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