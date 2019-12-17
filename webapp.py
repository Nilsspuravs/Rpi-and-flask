import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/cakess')
def cakess():
    return render_template('index1.html')

@app.route('/hello/lampa')
def hello(name):
    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')