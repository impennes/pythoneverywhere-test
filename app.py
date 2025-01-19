from flask import Flask, redirect, url_for
from datetime import datetime

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return 'Üdv a Sulipy üzenőfalán!'


@app.route('/course/〈int:number〉')
def course(number):
    return f'Ez a {number}. kurzus adatlapja!'


@app.route('/uzenofal')
def message_board():
    # átirányítás másik függvényre
    # return redirect('/')
    return redirect(url_for('home'))


@app.route('/contact')
def contact():
    return f'Jelentkezés a kurzusokra: info@sulipy.hu'


@app.route('/time')
def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    return 'A pontos idő: ' + current_time


if __name__ == '__main__':
    app.run()

