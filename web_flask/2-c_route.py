#!/usr/bin/python3
"""Module that starts a Flask web application"""
from flask import Flask
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


if __name__ == '__main__':
    app.run(host=ip, port=port)
