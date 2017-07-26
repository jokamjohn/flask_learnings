# Using Flask Components 

## Blueprints
Blueprints are  sets of operations which can be registered on an application, even multiple times as 
described in the [documentation](http://flask.pocoo.org/docs/0.12/blueprints/)
I have set up a simple `pages` blueprint [here](app/pages_blue_print.py)

Which I then registered to the `Flask` application instance like so
```angular2html
from flask import Flask
from app.pages_blue_print import pages

# Initialize the application
app = Flask(__name__)

# Register the pages blue print
app.register_blueprint(pages)
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