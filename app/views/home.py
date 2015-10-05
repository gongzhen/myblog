from flask import Blueprint, render_template, abort, redirect, url_for, request
from app.model import models
from app.model.models import Post
from .. import db

home = Blueprint('home', __name__)

@home.route('/')
def index():
	posts = models.Post.query.all()
	return render_template('home/index.html', posts = posts)

@home.route('/about')
def about():
    return render_template('home/about.html')

@home.route('/projects')
def projects():
    return render_template('home/projects.html')

@home.route('/contacts')
def contacts():
    return render_template('home/contacts.html')


