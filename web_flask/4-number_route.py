#!/usr/bin/python3
"""Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displaying Hello HBNB!"""

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """Displaying HBNB"""

    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_page(text):
    """Displaying HBNB"""

    text = text.replace("_", " ")

    return "C {}".format(text)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_page(text="is cool"):
    """Displaying content based on url"""

    text = text.replace("_", " ")

    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_page(n):
    """Displaying Number"""

    return "{}".format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
