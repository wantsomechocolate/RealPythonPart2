#views.py

from app import db
from flask import Blueprint, flash, redirect, render_template, request, session, url_for, g
from app.views import login_required, flash_errors
#from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy
from forms import RegisterForm, LoginForm
from app.models import User
from sqlalchemy.exc import IntegrityError


mod=Blueprint('users',__name__, url_prefix='/users',
              template_folder='templates',static_folder='static')



@mod.route('/logout/')
@login_required
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    session.pop('user_name', None)
    flash('You are logged out. Bye. :(')
    return redirect(url_for('.login'))


@mod.route('/', methods=['GET', 'POST'])
def login():

    error=None

    try:
        if session['logged_in']== True:
            return redirect(url_for('tasks'))
    except KeyError:
    
        if request.method == 'POST':
            u=User.query.filter_by(name=request.form['name'], password=request.form['password']).first()
            
            if u is None:
                error='Invalid username or password'
                flash(error)

            else:
                session['logged_in'] = True
                session['user_id'] = u.id
                session['user_name'] = u.name
                flash('You are logged in. Go Crazy.')
                return redirect(url_for('tasks.tasks'))
    return render_template('users/login.html',form=LoginForm(request.form),error=None)



@mod.route('/register/', methods=['GET','POST'])
def register():

    error=None
    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        new_user = User(
            form.name.data,
            form.email.data,
            form.password.data,
            )
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Thanks for registering. Please login.')
            return redirect(url_for('login'))
        except IntegrityError:
            error = 'Oh no! That username and/or email already exists. Please try again.'
            flash(error)
            return render_template('/users/register.html', form = form , error = None)

    else:
        flash_errors(form)

    return render_template('users/register.html', form=form, error=None)


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








