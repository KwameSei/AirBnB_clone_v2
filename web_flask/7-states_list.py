#!/usr/bin/python3
"""Flask web application"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """Displaying a list of all state objects in the database storage"""

    states = storage.all("State")
    return render_template('7-states_list.html', all_states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
