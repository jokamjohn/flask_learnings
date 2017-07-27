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


@pages.errorhandler(404)
def page_not_found(e):
    """
    Show this page for any 404 error.
    :param e:
    :return:
    """
    return render_template('pages/404.html')
