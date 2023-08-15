#!/usr/bin/python3
"""
A Flask web application with routes to display differents funtions
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


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the '/hbnb' route.

    Returns:
        str: The message "HBNB".
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def custom_message(text):
    """
    Route handler for the '/c/<text>' route.

    Args:
        text (str): The text variable extracted from the URL.

    Returns:
        str: The message "C " followed by the value of the text variable
             with underscores replaced by spaces.
    """
    return "C " + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_message(text):
    """
    Route handler for the '/python/<text>' route.

    Args:
        text (str): The text variable extracted from the URL.

    Returns:
        str: The message "Python " followed by the value of the text variable
             with underscores replaced by spaces.
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_check(n):
    """
    Route handler for the '/number/<n>' route.

    Args:
        n (int): The integer value extracted from the URL.

    Returns:
        str: The message "{n} is a number".
    """
    return f"{n} is a number"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
