import os
import csv

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from models import Book
from google import getGoogleData


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://rrcgpldedfwzsy:a327a7d195c293981f53baa91a8af5045c10ce642fd44b61ed87f2c77723e013@ec2-52-44-55-63.compute-1.amazonaws.com:5432/dc1scm7s3mgdqv"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)

# Read the file, create the array and make the request to google
def readFile():
    v = []
    f = open("./storage/books.csv")
    isbns = [] 
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        book = Book(isbn=isbn, title=title, author=author, year=year)
        v.append(book)
        isbns.append(book.isbn)
    




def main():
    f = open("./storage/books.csv")
    reader = csv.reader(f)

    for isbn, title, author, year in reader:
        book = Book(isbn=isbn, title=title, author=author, year=year)
        db.session.add(book)
        print(f"Added book number {isbn} with title {title} .")
    print("There is no more books.") 
    db.session.commit()
    print("Proccess successful.")


if __name__ == "__main__":
    with app.app_context():
        main()