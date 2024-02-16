#!/usr/bin/python3

"""
This script starts a flask 
Application which listens on port
5000
"""

from flask import Flask

myApp = Flask(__name__)


@myApp.route('/', strict_slashes=False)
def hello_hbnb_index():
    """
    Will Display Hello HBNB!
    """
    return 'Hello HBNB!'

@myApp.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Will Display HBNB
    """
    return "HBNB"

if __name__ == '__main__':
    myApp.run(host='0.0.0.0', port=5000)
