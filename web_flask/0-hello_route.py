#!/usr/bin/python3

"""
A simple Flask web application that displays "Hello HBNB!" on the root route.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root route.

    Returns:
        str: The greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
