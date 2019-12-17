import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)




@app.route('/lampa')
def index():
    return render_template('page.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')