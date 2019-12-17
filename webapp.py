import RPi.GPIO as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   17 : {'name' : 'GPIO 17', 'state' : GPIO.LOW},
   27 : {'name' : 'GPIO 27', 'state' : GPIO.LOW},
   22 : {'name' : 'GPIO 22', 'state' : GPIO.LOW}
   }

# Set each pin as an output and make it low:
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)


@app.route('/home')
def index():
    
    for pin in pins:
          pins[pin]['state'] = GPIO.input(pin)
   # Put the pin dictionary into the template data dictionary:
    templateData = {
      'pins' : pins
      }
    return render_template('index.html')


@app.route('/cakess')
def cakess():
    return render_template('index1.html')

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')