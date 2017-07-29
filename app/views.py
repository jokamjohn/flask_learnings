from app import app
from datetime import datetime
from flask import render_template


@app.route('/date')
def date_time():
    """
    This route passes the UTC current date and time to the time template
    Which is then formatted by Flask-Moment according to the user's
    locale.
    :return:
    """
    return render_template('time.html', current_time=datetime.utcnow())
