#!/usr/bin/python3
"""script that starts a Flask web application """
from flask import Flask
from models import storage



app = Flask(__name__)


@app.teardown_appcontext
def close(exception):
    """Delete current session."""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    order_states = sorted(states, key=lambda state: state.name)
    
    return render_template('7-states_list.html', states=order_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)