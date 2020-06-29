from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = "book"
    isbn = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.String, nullable=False)


class Usuario(db.Model):    
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String, nullable=False)
    #flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
    password = db.Column(db.String, nullable=False)