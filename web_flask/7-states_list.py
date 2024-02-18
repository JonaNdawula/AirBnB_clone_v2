#!/usr/bin/python3
"""
python script that
starts a Flask application
"""

from models import *
from models import storage
from flask import Flask
from flask import render_template

myApp = Flask(__name__)


@myApp.route('/states_list', strict_slashes=False)
def list_of_states():
    """
    will display an HTML page
    with list of ordered states
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@myApp.teardown_appcontext
def database_teardown(exception):
    """
    will close the storage
    on a teardown
    """
    storage.close()

if __name__ == '__main__':
    myApp.run(host='0.0.0.0', port='5000')
