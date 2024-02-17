#!/usr/bin/python3
"""
A python script that starts a
Flask web application usin port
5000
"""

from flask import Flask
from flask import render_template

myApp = Flask(__name__)


@myApp.route('/', strict_slashes=False)
def hello_hbnb_index():
    """
    will display
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
    will display
    C <text>
    """
    text = text.replace('_', ' ')
    return f'C {text}'


@myApp.route('/python', strict_slashes=False)
@myApp.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    """
    will display python followed by
    a text value
    """
    text = text.replace('_', ' ')
    return f'Python {text}'


@myApp.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    will display a number
    if n is an integer
    """
    return f'{n} is a number'


@myApp.route('/number_template/<int:n>', strict_slashes=False)
def display_number_and_template(n):
    """
    will display an HTML page
    if n is an integer
    """
    return render_template('5-number.html', n=n)


@myApp.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def check_odd_or_even(n):
    """
    will display an HTML page
    if n is an integer
    """
    if n % 2 == 0:
        even_number = 'even'
    else:
        even_number = 'odd'

    return render_template('6-number_odd_or_even.html', n=n,
                           even_number=even_number)

if __name__ == '__main__':
    myApp.run(host='0.0.0.0', port='5000')
