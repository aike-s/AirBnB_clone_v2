#!/usr/bin/python3
"""
Add /number/<n> route
"""
from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def print_text_c(text):
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/(<text>)', strict_slashes=False)
def print_text_python(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<n>', strict_slashes=False)
def print_int(n):
    if int(n):
        return '{} is a number'.format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
