#!/usr/bin/python3
"""
python script that starts
a flask Application
"""

from flask import Flask
from flask import render_template
from models import *
from models import storage

myApp = Flask(__name__)


@myApp.route('/hbnb_filters', strict_slashes=False)
def app_filters():
    """
    will display an HTML page
    """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@myApp.teardown_appcontext
def database_teardown(exception):
    """
    Will close the storage
    after teardown
    """
    storage.close()


if __name__ == '__main__':
    myApp.run(host='0.0.0.0', port='5000')
