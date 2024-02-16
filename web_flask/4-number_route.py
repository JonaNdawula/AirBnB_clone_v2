#!/usr/bin/python3
"""
A Python script that starts
a Flask web application
and listens on port 5000
"""

from flask import Flask

myApp = Flask(__name__)


@myApp.route('/', strict_slashes=False)
def hello_hbnb_index():
    """
    Will display
    Hello HBNB!
    """
    return 'Hello HBNB!'


@myApp.route('/', strict_slashes=False)
def display_hbnb():
    """
    will display
    HBNB
    """
    return 'HBNB'


@myApp.route('/', strict_slashes=False)
def display_c(text):
    """
    Will display
    C <text>
    """
    text = text.replace('_', ' ')
    return f'C {text}'


@myApp.route('/python', strict_slashes=False)
@myApp.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    """
    Will display Python followed by
    a text value
    """
    text = text.replace('_', ' ')
    return f'Python {text}'


@myApp.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    Will display a number
    if n is an integer
    """
    return f'{n} is a number'


if __name__ == '__main__':
    myApp.run(host='0.0.0.0', port='5000')
