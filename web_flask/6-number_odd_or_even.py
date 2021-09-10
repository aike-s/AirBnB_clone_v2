#!/usr/bin/python3
"""
Add /number_odd_or_even/<n> route
"""
from flask import Flask, render_template


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

@app.route('/number_template/<n>', strict_slashes=False)
def print_on_templante(n):
    if int(n):
        to_print = 'Number: {}'.format(n)
        return render_template('templates/5-number.html', number=to_print)

@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def print_on_templante(n):
    if int(n):
        if (n % 2) == 0:
            to_print = 'Number: {} is even'.format(n)
        else:
            to_print = 'Number: {} is odd'.format(n)

        return render_template('templates/5-number.html', number=to_print)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
