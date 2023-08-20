#!/usr/bin/python3
"""Module for hello route"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """The hello url route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """The url /hbnb route"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """The C route, displays C along with text"""
    output = 'C ' + text.replace('_', ' ')
    return output


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is_cool"):
    """The python route, displays python along with text"""
    output = 'Python ' + text.replace('_', ' ')
    return output


if __name__ == "__main__":
    app.run()
