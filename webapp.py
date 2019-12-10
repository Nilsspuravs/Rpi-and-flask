from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/russia')
def index():
    return 'Russia is big country,ruled by russians!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')