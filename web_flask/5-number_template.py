#!/usr/bin/python3
"""Module that starts a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False
ip = '0.0.0.0'
port = 5000


@app.route('/')
def hello():
    """Function that returns Hello"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbn():
    """Fucntion that returns HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def elc(text):
    """Function thant display C followed by text"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python')
@app.route('/python/<text>')
def py_rout(text='is cool'):
    """Returns text with python path"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def num(n):
    """Retruns n is a number if is an int"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def num_template(n):
    """Return an html for an int"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host=ip, port=port)
