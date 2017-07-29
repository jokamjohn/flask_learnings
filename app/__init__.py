from flask import Flask
from flask_moment import Moment

from app.blueprints.pages import pages

# Initialize the application
app = Flask(__name__)

# Initialize Flask-Moment
moment = Moment(app)

# Register the pages blue print
app.register_blueprint(pages)

# Load the app views
from app import views
