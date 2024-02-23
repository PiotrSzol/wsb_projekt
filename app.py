from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import Stolik, Danie, Kontakt, NaMiejscu, NaWynos, db
from operations import next_number, array_of_number

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/menu')
def menu():
    menu_items = ['Danie 1', 'Danie 2', 'Napój 1', 'Deser 1']
    return render_template('menu.html', menu_items=menu_items)


@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html')


@app.route('/wolny_stolik', methods=['GET', 'POST'])
def wolny_stolik():
    if request.method == 'POST':
        if request.form['action'] == 'delete':
            table_id = request.form['stolik_id']
            table_number = Stolik.query.get(table_id)
            db.session.delete(table_number)
            db.session.commit()
        if request.form['action'] == 'reserve':
            table_id = request.form['stolik_id']
            table = Stolik.query.get(table_id)
            table.czy_zarezerwowany = True
            db.session.commit()
    result = Stolik.query.filter(Stolik.czy_zarezerwowany == False).all()
    return render_template('wolny_stolik.html', result=result)


@app.route('/zarezerwowany_stolik', methods=['GET', 'POST'])
def zarezerwowany_stolik():
    if request.method == 'POST':
        if request.form['action'] == 'delete':
            table_id = request.form['stolik_id']
            table_number = Stolik.query.get(table_id)
            db.session.delete(table_number)
            db.session.commit()
        if request.form['action'] == 'reserve':
            table_id = request.form['stolik_id']
            table = Stolik.query.get(table_id)
            table.czy_zarezerwowany = False
            db.session.commit()
    result = Stolik.query.filter(Stolik.czy_zarezerwowany == True).all()
    return render_template('zarezerwowany_stolik.html', result=result)


@app.route('/wyswietl_na_miejscu', methods=['GET', 'POST'])
def wyswietl_na_miejscu():
    if request.method == 'POST':
        if request.form['action'] == 'delete':
            id = request.form['danie_na_wynos_id']
            number = NaMiejscu.query.get(id)
            db.session.delete(number)
            db.session.commit()
    result = NaMiejscu.query.all()
    return render_template('wyswietl_na_miejscu.html', result=result)


@app.route('/wyswietl_na_wynos', methods=['GET', 'POST'])
def wyswietl_na_wynos():
    if request.method == 'POST':
        if request.form['action'] == 'delete':
            id = request.form['danie_na_wynos_id']
            adres = NaWynos.query.get(id)
            db.session.delete(adres)
            db.session.commit()
    result = NaWynos.query.all()
    return render_template('wyswietl_na_wynos.html', result=result)


@app.route('/na_wynos', methods=['GET', "POST"])
def na_wynos():
    if request.method == 'POST':
        nazwa = request.form['nazwa']
        cena = request.form['cena']
        adres = request.form['adres']
        danie = NaWynos(nazwa=nazwa, cena=cena, adres=adres)
        db.session.add(danie)
        db.session.commit()

    return  render_template('na_wynos.html')


@app.route('/na_miejscu', methods=['GET', "POST"])
def na_miejscu():
    if request.method == 'POST':
        nazwa = request.form['nazwa']
        cena = request.form['cena']
        nr_stolika = request.form['nr_stolika']
        danie = NaMiejscu(nazwa=nazwa, cena=cena, nr_stolika=nr_stolika)
        db.session.add(danie)
        db.session.commit()

    return render_template('na_miejscu.html')


@app.route('/dodaj_stolik', methods=['GET', 'POST'])
def zarezerwuj_stolik():
    if request.method == 'POST':
        temp_array = array_of_number(Stolik)
        numer_stolika = next_number(temp_array)
        ilosc_osob = int(request.form['ilosc_osob'])

        nowy_stolik = Stolik(numer=numer_stolika, ilosc_miejsc=ilosc_osob)
        db.session.add(nowy_stolik)
        db.session.commit()

    return render_template('dodaj_stolik.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
