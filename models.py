from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Stolik(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numer = db.Column(db.Integer, unique=True)
    ilosc_miejsc = db.Column(db.Integer)
    czy_zarezerwowany = db.Column(db.Boolean, default=False)

    def __init__(self, numer, ilosc_miejsc, czy_zarezerwowany=False):
        self.numer = numer
        self.ilosc_miejsc = ilosc_miejsc
        self.czy_zarezerwowany = czy_zarezerwowany


class Danie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(100), nullable=False)
    cena = db.Column(db.Float, nullable=False)

    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena


class NaWynos(Danie):
    id = db.Column(db.Integer, db.ForeignKey('danie.id'), primary_key=True)
    adres = db.Column(db.Integer())

    def __init__(self, nazwa, cena, adres):
        super().__init__(nazwa, cena)
        self.adres = adres


class NaMiejscu(Danie):
    id = db.Column(db.Integer, db.ForeignKey('danie.id'), primary_key=True)
    nr_stolika = db.Column(db.Integer)

    def __init__(self, nazwa, cena, nr_stolika):
        super().__init__(nazwa, cena)
        self.nr_stolika = nr_stolika


class Kontakt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    telefon = db.Column(db.String(20), nullable=True)
