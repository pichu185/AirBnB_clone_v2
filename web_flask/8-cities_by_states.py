#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def remove_sesh(self):
    """After each request you must remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """render html page with a list of states"""
    states = storage.all(State)
    return (render_template('7-states_list.html', states=states))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
