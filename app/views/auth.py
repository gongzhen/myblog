from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required, current_user
from ..forms import LoginForm
from app.model.models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username = form.username.data).first()
		print user
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			return redirect(request.args.get('next') or url_for('post.write'))
		flash('Invalid username or password.')
	return render_template('auth/login.html', form=form)

