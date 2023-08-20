#!/usr/bin/python3
"""Module for hello route"""
from flask import Flask, abort, render_template


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


@app.route('/number/<n>', strict_slashes=False)
def number_route(n):
    """The number route, displays only integers"""
    try:
        n = int(n)
    except ValueError:
        abort(404)

    output = str(n) + ' is a number'
    return output


@app.route('/number_template/<n>', strict_slashes=False)
def number_template_route(n):
    """The number_template route, renders html template"""
    try:
        n = int(n)
    except ValueError:
        abort(404)

    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run()
