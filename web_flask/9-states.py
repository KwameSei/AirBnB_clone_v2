#!/usr/bin/python3
"""Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities():
    """Displaying a list of all city objects in the database storage"""

    states = storage.all("State")
    return render_template('8_cities_by_states.html', all_states=states)


@app.route('/states', strict_slashes=False)
def all_states():
    """Displaying a list of all state objects in the database storage"""

    states = storage.all("State")
    return render_template('9-states.html', all_states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session"""
    
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
