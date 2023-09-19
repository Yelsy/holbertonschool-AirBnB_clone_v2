#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ returns a string depending on the text of thevargument """
    newText = text.replace('_', ' ')
    return f"C {newText}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """ returns a string depending on the text of thevargument """
    newText = text.replace('_', ' ')
    return f"Python {newText}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if n is an integer."""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if <n> is an integer."""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
