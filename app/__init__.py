#!/usr/bin/env python
import os
basedir = os.path.abspath(os.path.dirname(__file__))

from flask import Flask, request, render_template, redirect, url_for, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.moment import Moment

moment = Moment()
db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db.init_app(app)
moment.init_app(app)

from views.home import home as home_blueprint
app.register_blueprint(home_blueprint)

from views.post import post as post_blueprint
app.register_blueprint(post_blueprint)