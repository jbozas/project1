import os
import requests


from flask import Flask, session, render_template, request
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from google import getGoogleData, getImage
from request import exists
from models import Book, Review

app = Flask(__name__)


# Tell Flask what SQLAlchemy databas to use.
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://rrcgpldedfwzsy:a327a7d195c293981f53baa91a8af5045c10ce642fd44b61ed87f2c77723e013@ec2-52-44-55-63.compute-1.amazonaws.com:5432/dc1scm7s3mgdqv"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()
db.init_app(app)


@app.route("/")
def index():
    return render_template("startPage.html")

@app.route("/books/<string:isbn>")
def books(isbn):
    book = Book.query.get(isbn)
    av_rngs, rcount = getGoogleData(isbn=isbn)

    comentarios = Review.query.filter_by(isbn=isbn).all()
    print(comentarios)

    return render_template("book.html", book=book, av_rngs=av_rngs, rcount=rcount, comentarios=comentarios)

@app.route('/comment/<string:isbn>', methods=["POST"])
def comment(isbn):
    comment = request.form.get("comment")
    review = Review(isbn=isbn, usuario=2, comments=comment, stars="3")
    db.session.add(review)
    db.session.commit()
    #book = Book(isbn=isbn, title=title, author=author, year=year)
    #db.session.add(book)
    #db.session.commit()
    return f"LLego{comment} with the book: {isbn}"


@app.route('/book', methods=["POST"])
def book():
    value = request.form.get("book")

    #Get results
    book_isbn = Book.query.get(value)
    books_author = Book.query.filter(Book.author.like(f"%{value}%")).all()
    books_title = Book.query.filter(Book.title.like(f"%{value}%")).all()

    print(f'By ISBN: {book_isbn} - by Author {books_author} - by Title {books_title}')

    return render_template("books.html", book_isbn=book_isbn, books_author=books_author, books_title=books_title)

"""Return a JSON with the ISBN book info."""
@app.route("/api/<string:isbn>")
def api(isbn):
    return exists(isbn)

def main():
      # Create tables based on each table definition in `models`
      db.create_all()

if __name__ == "__main__":
    # Allows for command line interaction with Flask application
    with app.app_context():
        app.run(debug=True)