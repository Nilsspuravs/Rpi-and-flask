from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/russia')
def russia():
    return 'Yummy Russian Svetlanas!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')