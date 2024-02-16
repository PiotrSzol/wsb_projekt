from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import Stolik, Danie, Kontakt, db
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
    result = Stolik.query.filter(Stolik.czy_zarezerwowany == True).all()
    return render_template('zarezerwowany_stolik.html', result=result)


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
