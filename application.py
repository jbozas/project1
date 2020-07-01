import os
import requests


from flask import Flask, session, render_template, request
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from request import exists

app = Flask(__name__)


# Tell Flask what SQLAlchemy databas to use.
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://rrcgpldedfwzsy:a327a7d195c293981f53baa91a8af5045c10ce642fd44b61ed87f2c77723e013@ec2-52-44-55-63.compute-1.amazonaws.com:5432/dc1scm7s3mgdqv"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()
db.init_app(app)


@app.route("/")
def index():
    return render_template("startPage.html")

"""Return a JSON with the ISBN book info."""
@app.route("/api/<string:isbn>")
def api(isbn):
    return exists(isbn)
    
"""Import csv and google data to load it into the db"""
@app.route("/import")
def import_csv():
    exec(open('import.py').read())

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    if name is None:
       return render_template("hello.html")
    else:
        return f"Hello, {name}!"
    return render_template("hello.html")

def main():
      # Create tables based on each table definition in `models`
      db.create_all()

if __name__ == "__main__":
    # Allows for command line interaction with Flask application
    with app.app_context():
        main()