from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required, current_user
from ..forms import LoginForm, EditProfileForm
from app.model.models import User
from .. import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username = form.username.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			return redirect(request.args.get('next') or url_for('post.write'))
		flash('Invalid username or password.')
	return render_template('auth/login.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('home.index'))

@auth.route('/user/<username>')
def user(username):
	user = User.query.filter_by(username=username).first_or_404()
	return render_template('auth/user.html', user=user)	


@auth.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
	form = EditProfileForm()
	return render_template('auth/edit_profile.html', form=form)	
