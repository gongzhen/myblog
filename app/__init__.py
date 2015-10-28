from flask import Flask, request, render_template, redirect, url_for, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.moment import Moment
from flask.ext.misaka import Misaka
from .momentjs import momentjs
from flask.ext.login import LoginManager
from config import config

moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	db.init_app(app)
	moment.init_app(app)
	Misaka(app)
	login_manager.init_app(app)
	app.jinja_env.globals['momentjs'] = momentjs

	from views.home import home as home_blueprint
	app.register_blueprint(home_blueprint)

	from views.post import post as post_blueprint
	app.register_blueprint(post_blueprint)

	from views.auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	return app

