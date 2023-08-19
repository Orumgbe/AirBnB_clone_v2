#!/usr/bin/python3
"""Module for hello route"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """The hello url route"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run()
