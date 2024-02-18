#!/usr/bin/python3
"""
A Python script
that starts a flask application
"""

from flask import Flask
from flask import render_template
from models import *
from models import storage

myApp = Flask(__name__)


@myApp.route('/list_of_cities_by_states', strict_slashes=False)
def list_of_cities_by_states():
    """
    Will display states and
    cities in alphabetical order
    """
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@myApp.teardown_appcontext
def database_teardown(exception):
    """
    Will close storage
    after teardown
    """
    storage.close()


if __name__ == '__main__':
    myApp.run(host='0.0.0.0', port='5000')
