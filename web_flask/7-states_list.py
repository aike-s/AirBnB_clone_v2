#!/usr/bin/python3
"""
Starts a Flask web application
"""
from os import name
from typing_extensions import OrderedDict
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def diplay_page():
    sorted_states = dict(sorted(storage.all('State'), name))
    return render_template('7-states_list.html', tittle="States",
                            states=sorted_states)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
