from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = "book"
    isbn = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    year = db.Column(db.String, nullable=False)
    """
    #review_count = db.Column(db.Integer, nullable=True)
    #average_score = db.Column(db.Float, nullable=True)

    def __addAtr__(self, avg_sc, rev_coun):
        review_count = db.Column(db.Integer, nullable=True)
        average_score = db.Column(db.Float, nullable=True)
    """

class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String, nullable=False)
    #flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
    password = db.Column(db.String, nullable=False)