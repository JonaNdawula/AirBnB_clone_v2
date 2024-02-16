#!/usr/bin/python3
"""
A python script that
starts a flask web Application
and listens at port 5000
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
    Hello HBNB
    """
    return 'HBNB'


@myApp.route('/', strict_slashes=False)
def display_c(text):
    """
    Will display C <text>
    """
    text = text.replace('_', ' ')
    return f'C {tex}'


@myApp.route('/python', strict_slashes=False)
@myApp.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    """
    Will display Python
    followed by a text value
    """
    text = text.replace('_', ' ')
    return f'Python {text}'


if __name__ == '__main__':
    myApp.run(host='0.0.0.0', port='5000')
