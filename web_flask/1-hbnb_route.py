#!/usr/bin/python3
"""
A Flask web application with routes to display greetings.
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
