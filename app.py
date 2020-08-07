"""Main module for running the Flask app.

Responsible for initializing the data and setting up the Flask app.
"""
from flask import Flask, request, render_template

from api import (
    cache,
    fortune_manager,
)


# The main Flask app
app = Flask(__name__)

# Initialize the list of quotes
fortune_manager.load_fortunes()



@app.route('/fortune/get')
def get_random_fortune():
    return {'fortune': fortune_manager.get_fortune()}


@app.route('/fortune/update', methods = ['POST'])
def update_fortune():
    """Based from the given fortune, update with the updated one the user gave."""
    data = request.json

    old_fortune = data['old_fortune']
    new_fortune = data['new_fortune']
    return {'fortune': fortune_manager.update_fortune(old_fortune, new_fortune)}


@app.route('/fortune/get_all')
def get_all_fortunes():
    """A simple endpoint for gathering all fortunes."""
    return {'fortune': cache.get("fortunes")}


##########
# Front-end endpoints start here. Ideally, this is separated from the
# fortunes data management API.
##########
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/open_cookie')
def open_fortune():
    """Renders the picked fortune.

    TODO: Ideally, the picked quote should only be persisted in the front-end
    in a cookie or we customize a POST request to use the value from the jinja2
    variable. This can may be done with jQuery. Unfortunately, because of time
    constraints, this will have to do. Since the server is the one persisting
    the fortune, the app can only be useful for one person.
    """
    picked_fortune = fortune_manager.get_fortune()
    cache.put("picked_fortune", picked_fortune)
    return render_template('open_cookie.html',
            fortune=picked_fortune)


@app.route('/edit_cookie')
def edit_fortune():
    """Allows the user to edit the picked fortune.
    """
    picked_fortune = cache.get("picked_fortune")
    return render_template('edit_cookie.html',
            fortune=picked_fortune)


@app.route('/fool')
def bot_thanks():
    return render_template('bot_thanks.html')


@app.route('/heartfelt_thanks', methods=['GET', 'POST'])
def heartfelt_thanks():
    """The final stage when the user edits the given fortune."""

    # Updates the list with the user-given fortune
    if request.method == 'POST':
        old_fortune = cache.get("picked_fortune")
        new_fortune = request.form["new_fortune"]
        fortune_manager.update_fortune(old_fortune, new_fortune)

    return render_template('participatory_thanks.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
