from flask import Flask, render_template, jsonify, request
from models import Book


def exists(isbn):
    """Return details about a book."""

    # Make sure book exists.
    book = Book.query.get(isbn)

    #book = Book.query.filter(Book.isbn == isbn).first()  
    if book is None:
       return jsonify({"error": "Invalid book"}), 404

    # Get book data
    ## HERE IS MORE CODE - To show more info about the book

    #In progress

    return jsonify(
        {
            "isbn": book.isbn,
            "title": book.title,
            "author": book.author,
            "year": book.year
        })
    

