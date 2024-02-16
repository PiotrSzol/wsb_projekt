from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Stolik(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numer = db.Column(db.Integer, unique=True)
    ilosc_miejsc = db.Column(db.Integer)
    czy_zarezerwowany = db.Column(db.Boolean, default=False)


class Danie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(100), nullable=False)
    opis = db.Column(db.String(255), nullable=True)
    cena = db.Column(db.Float, nullable=False)


class Kontakt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    telefon = db.Column(db.String(20), nullable=True)

