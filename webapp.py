from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

    if __name__ == '__name__':
        app.run(debug=True, host='0.0.0.0')
