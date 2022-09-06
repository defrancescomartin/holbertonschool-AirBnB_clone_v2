#!/usr/bin/python3
"""Module that starts a Flask web application"""
from os import stat
from flask import Flask, render_template
from models import storage
from models import state
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False
ip = '0.0.0.0'
port = 5000


@app.teardown_appcontext
def tear_db(exception):
    """Closing DB"""
    storage.close()


@app.route('/states_list')
def states_list():
    """Displaying list of states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host=ip, port=port)
