#!/usr/bin/python3
"""
Add /hbnb route
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Print hello """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Print HBNB """
    return 'HBNB'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
