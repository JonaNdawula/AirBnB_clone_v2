#!/usr/bin/python3

"""
A script that starts a
Flask web application
listening on port 5000
"""

from flask import Flask

myApp = Flask(__name__)


@myApp.route('/', strict_slashes=False)
def hello_hbnb_index():
    """
    Displays the message
    Hello HBNB!
    """
    return 'Hello HBNB!'


@myApp.route('/', strict_slashes=False)
def display_hbnb():
    """
    Displays the message
    Hello HBNB!
    """
    return 'HBNB'


@myApp.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """
    Displays the text
    C
    """
    text = text.replace('_', ' ')
    return f'C {text}'


if __name__ == '__main__':
    myApp.run(host='0.0.0.0', port='5000')
