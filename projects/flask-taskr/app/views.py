#views.py

from app import app, db
from flask import flash, redirect, render_template, request, session, url_for, g
from functools import wraps


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)

        else:
            flash("You need to login first")
            return redirect(url_for('users.login'))
    return wrap

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash('Error in the %s field - %s' % (getattr(form, field).label.text, error),'error')


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(403)
def internal_error(error):
    return render_template('403.html'), 403

@app.errorhandler(410)
def internal_error(error):
    return render_template('410.html'), 410

@app.route('/', defaults={'page':'index'})
def index(page):
    return(redirect(url_for('users.login')))








