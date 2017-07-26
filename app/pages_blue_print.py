from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

# Defining a blueprint
pages = Blueprint('pages', __name__, template_folder='templates')


@pages.route('/', defaults={'page': 'index'})
@pages.route('/<page>')
def show(page):
    """
    Show a page if it exists with index.html as the default
    otherwise abort with a 404
    :param page:
    :return:
    """
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
