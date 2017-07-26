from flask import Flask
from app.pages_blue_print import pages

# Initialize the application
app = Flask(__name__)

# Register the pages blue print
app.register_blueprint(pages)
