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

## Dates and Time
It is always tricky to manage dates and times for an application that
is used across the world due to the different time zones.
But well with Flask-Moment all is well catered for. 
`Flask-Moment` uses the [Momentjs](http://momentjs.com/) javascript lib to 
format dates and times in the browser according to the user`s locale.

All you have to do is set the date and time to [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) and
`Flask-Moment` will handle the rest.

## Setup
As any other `Flask` extension use pip to install
the extension by running `pip install flask-moment
`  and after initialize the module with the app as so:

```apple js
from flask import Flask
from flask_moment import Moment

app = Flask(__name__)

moment = Moment(app)
```
At this point `moment` is available to all templates.
All we need to do now is pass a UTC `datetime` to any view,
we use `current_time` as the variable holding the `datetime`
```apple js
from app import app
from datetime import datetime
from flask import render_template


@app.route('/date')
def date_time():
    return render_template('time.html', current_time=datetime.utcnow())
```
### The template
All we have to do now is add a reference to [Jquery](http://code.jquery.com/) since 
`Momentjs` depends on it. Flask-Moment also provides a way of
adding a reference to the [MomentJs](http://momentjs.com/) Javascript lib.
```apple js
{#Jquery#}
<script src="http://code.jquery.com/jquery-3.2.1.min.js"
        integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
        crossorigin="anonymous"></script>

{#Moments JS scripts#}
{{ moment.include_moment() }}
```

We can now display the date and time in the user's locale
on the page.
```apple js
<p>The date is <strong>{{ moment(current_time).format('LLL') }}</strong></p>

<p>It has been <strong>{{ moment(current_time).fromNow(refresh=True) }}</strong></p>
```
For more info about the format and fromNow methods check out 
the Momentjs [Official Documentation](http://momentjs.com/)

#### Output
```apple js
The date is July 29, 2017 5:18 PM

It has been 21 minutes ago
``` 