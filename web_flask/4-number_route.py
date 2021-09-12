#!/usr/bin/python3
"""
Add /number/<n> route
"""
from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Print hello """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Print HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def print_text_c(text):
    """ Print variable text """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/(<text>)', strict_slashes=False)
def print_text_python(text='is cool'):
    """ Print variable text with default string """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def print_int(n):
    """ Print num only if it's int """
    return '{} is a number'.format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
