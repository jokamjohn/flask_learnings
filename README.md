# Using Flask Components 

## Blueprints
I used this repo to learn about the flask BluePrints.

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