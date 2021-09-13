#!/usr/bin/python3
"""
Add /number_odd_or_even/<n> route
"""
from flask import Flask, render_template


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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def print_text_python(text='is cool'):
    """ Print variable text with default string """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def print_int(n):
    """ Print num only if it's int """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def print_on_templante(n):
    """ Render template only if num is int """
    to_print = 'Number: {}'.format(n)
    return render_template('5-number.html', number=to_print)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def print_on_templante_even_or_odd(n):
    """ Render template only if num is int with even/odd """
    if (n % 2) == 0:
        to_print = 'Number: {} is even'.format(n)
    else:
        to_print = 'Number: {} is odd'.format(n)

    return render_template('6-number_odd_or_even.html', number=to_print)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
