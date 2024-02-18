#!/usr/bin/python3
"""
A python script
that starts a Flask application
"""

from flask import Flask
from flask import render_template
from models import *
from models import storage

myApp = Flask(__name__)


@myApp.route('/states', strict_slashes=False)
@myApp.route('/states/<state_id>', strict_slashes=False)
def list_states(state_id=None):
    """
    will display states and
    and cities in alphabetical order
    """
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@myApp.teardown_appcontext
def database_teardown(exception):
    """
    Will close the storage
    on teardown
    """
    storage.close()


if __name__ == '__main__':
    myApp.run(host='0.0.0.0', port='5000')
