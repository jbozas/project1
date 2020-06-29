import os
import requests
import sqlalchemy

from flask import Flask, session, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *

app = Flask(__name__)


# Tell Flask what SQLAlchemy databas to use.
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://rrcgpldedfwzsy:a327a7d195c293981f53baa91a8af5045c10ce642fd44b61ed87f2c77723e013@ec2-52-44-55-63.compute-1.amazonaws.com:5432/dc1scm7s3mgdqv"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

db.init_app(app)

# Set up database
engine = create_engine("postgres://rrcgpldedfwzsy:a327a7d195c293981f53baa91a8af5045c10ce642fd44b61ed87f2c77723e013@ec2-52-44-55-63.compute-1.amazonaws.com:5432/dc1scm7s3mgdqv")
db = scoped_session(sessionmaker(bind=engine))
connection = SQLAlchemy(app)




@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/api/<int:isbn>")
def api(isbn):
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "i8iZFHFqdnKzXDrfgTLQ", "isbns": "9781632168146"})
    book = res.json()
    # Make sure the book exists.
    if res is None:
        return render_template("error.html", message="No such book.")

    return render_template("book.html", book=book)

@app.route("/import")
def import_csv():
    exec(open('import.py').read())


def main():
    # Create tables based on each table definition in `models`
    connection.create_all()

if __name__ == "__main__":
    # Allows for command line interaction with Flask application
    with app.app_context():
        import_csv()