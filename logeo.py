import os
import csv

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from models import Usuario
from google import getGoogleData


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://rrcgpldedfwzsy:a327a7d195c293981f53baa91a8af5045c10ce642fd44b61ed87f2c77723e013@ec2-52-44-55-63.compute-1.amazonaws.com:5432/dc1scm7s3mgdqv"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)


def no_authent():
    user = Usuario(usuario="anonimo", password="")
    db.session.add(user)
    db.session.commit()
    return user.id
