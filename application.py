import os
import requests


from flask import Flask, session, render_template, request
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from google import getGoogleData, getImage
from request import exists
from models import Book, Review, Usuario
from logeo import no_authent, get_session, create_user, verify_user, get_sessionUser


app = Flask(__name__)


# Tell Flask what SQLAlchemy databas to use.
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://rrcgpldedfwzsy:a327a7d195c293981f53baa91a8af5045c10ce642fd44b61ed87f2c77723e013@ec2-52-44-55-63.compute-1.amazonaws.com:5432/dc1scm7s3mgdqv"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()
db.init_app(app)
current_session=None

@app.route("/")
def index():
    print('Estoy testeando')
    if current_session is not None:
        return render_template("startPage.html", curr_sess=current_session)
    else:
        return render_template("user.html")

@app.route("/logout")
def logout():
    global current_session
    current_session=None
    return index()

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/user_log", methods=["POST"])
def user_log():
    global current_session
    username = request.form.get("username")
    password = request.form.get("password")
    user = verify_user(username, password)
    print(f"El resultado de la verificación: {user}")
    if user:
        current_session = get_sessionUser(username)
    return index()

@app.route("/register")
def register():
    #if(username is not None and password is not None):
     #  user_creation(username, password)
    return render_template("register.html")

@app.route("/user_creation", methods=["POST"])
def user_creation():
    global current_session
    username = request.form.get("username")
    password = request.form.get("password")
    user = create_user(username, password)
    current_session = user
    return index()

@app.route("/anonymus")
def anonymus():
    global current_session
    user_id = no_authent()
    current_session = get_session(user_id)

    return render_template("startPage.html", curr_sess=current_session)

@app.route("/books/<string:isbn>")
def books(isbn):
    book = Book.query.get(isbn)
    av_rngs, rcount = getGoogleData(isbn=isbn)

    comentarios = Review.query.filter_by(isbn=isbn).all()

    allow_comment=True
    user_comment = Review.query.get((isbn, current_session.id))
    if(user_comment):
        allow_comment=False

    return render_template("book.html", book=book, av_rngs=av_rngs, rcount=rcount, comentarios=comentarios, curr_sess=current_session, allow_comment=allow_comment)

@app.route('/comment/<string:isbn>', methods=["POST"])
def comment(isbn):
    comment = request.form.get("comment")
    review = Review(isbn=isbn, usuario=current_session.id, comments=comment, stars="3")
    db.session.add(review)
    db.session.commit()
    return books(isbn)


@app.route('/book', methods=["POST"])
def book():
    value = request.form.get("book")

    #Get results
    book_isbn = Book.query.get(value)
    books_author = Book.query.filter(Book.author.like(f"%{value}%")).all()
    books_title = Book.query.filter(Book.title.like(f"%{value}%")).all()

    return render_template("books.html", book_isbn=book_isbn, books_author=books_author, books_title=books_title, curr_sess=current_session)

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
