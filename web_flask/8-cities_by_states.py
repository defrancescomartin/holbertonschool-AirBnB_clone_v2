#!/usr/bin/python3
"""Flask app for HBNB"""
from os import getenv
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
ip = '0.0.0.0'
port = 5000


@app.teardown_appcontext
def teardown_db(exception):
    """Close databas session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
       Displays the list of the Cities in the database with their states.
    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host=ip, port=port)