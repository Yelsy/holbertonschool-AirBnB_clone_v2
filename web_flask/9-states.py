#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def storage_close(self):
    """close the sesion"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """ show list of states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template("7-states_list.html", states=sorted_states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """ show the list of cities with the given id """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template("9-states.html",
                           states=storage.all(State).get(f'State.{id}'))


if __name__ == '__main__':
    """ start the web app """
    app.run(host='0.0.0.0', port=5000)
