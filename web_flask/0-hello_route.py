#!/usr/bin/python3
"""
Script to start Flask app
"""

from flask import Flask

myApp = Flask(__name__)


@myApp.route('/', strict_slashes=False)
def hello_hbnb_index():
    """
    Returns Hello HBNB!
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    myApp.run(host='0.0.0.0', port='5000')
