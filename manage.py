from flask_script import Manager
from app import app

manager = Manager(app)

"""
To get a list of all command plus their descriptions use
python manage.py
"""


@manager.command
def routes():
    """
    Lists all the application routes
    """
    import urllib
    # This is a code snippet by Jonathan Tushman
    # Found at http://flask.pocoo.org/snippets/117/
    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)

    for line in sorted(output):
        print(line)


if __name__ == '__main__':
    manager.run()
