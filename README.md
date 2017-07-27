# Using Flask Components 

## Blueprints
Blueprints are  sets of operations which can be registered on an application, even multiple times as 
described in the [documentation](http://flask.pocoo.org/docs/0.12/blueprints/)
I have set up a simple `pages` blueprint [here](app/blueprints/pages.py)

### Defining a Blueprint
Defining a blueprint is very straight as shown below.
Provide the name of the blueprint as the first argument

```angular2html
from flask import Blueprint, render_template, abort

# Defining a blueprint
pages = Blueprint('pages', __name__, template_folder='templates')
```

### Registering the Blueprint
In order to use the blueprint register it to the `Flask` application instance like so
```angular2html
from flask import Flask
from app.pages_blue_print import pages

# Initialize the application
app = Flask(__name__)

# Register the pages blue print
app.register_blueprint(pages)
```
### Error Handling
Blueprints handle errors the same way they are handled within
the main Flask application.
Lets take for example handling `404` errors, below is a snippet
from my `pages` blueprint

```angular2html
@pages.errorhandler(404)
def page_not_found(e):
    """
    Show this page for any 404 error.
    :param e:
    :return:
    """
    return render_template('pages/404.html')
```
### Building Urls
Building urls within a blueprint is the same as in the
Flask main application, just that you have to prefix
the blueprint `name` for every route method name. 
For example to point to the show route method in the pages
blueprint, you would do it like so
```angular2html
url_for('pages.show')
```

## Manager
When you install the [Flask-Script](http://flask-script.readthedocs.io/en/latest/) module,
it enables you write external scripts in `Flask`.

It exposes the `Manager` instance and `Command` class which one can use to add `Commands`
to the application command-line interface.

For example I am using it to make a command that shows
all the application routes just by running `python manage.py routes`

At the same time you can see all the available commands
by running `python manage.py`

I have added a command that lists all the application
routes. Run `python manage.py routes`

The output will look something like this
```angular2html
(venv) F:\Andela\apps\blueprint>python manage.py routes
pages.show                                         HEAD,GET,OPTIONS     /
pages.show                                         HEAD,GET,OPTIONS     /<page>
static                                             HEAD,GET,OPTIONS     /static/<path:filename>
```