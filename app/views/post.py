from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from ..models import Post
from app import models
from app.markdown import markdown
from .. import db

post = Blueprint('post', __name__)

# http://stackoverflow.com/questions/7974771/flask-blueprint-template-folder
@post.route('/post/index', methods=['GET', 'POST'])
def index():
	return render_template('post/index.html')

@post.route('/post/<int:id>')
def page(id):
	post = models.Post.query.get_or_404(id);
	html = markdown.render(post.body) 
	return render_template('post/post.html', post=post, html = html)

@post.route('/post/write')
def write():
	return render_template('post/write.html')

@post.route('/post/create', methods=['POST'])
def create():	
	title = request.form['title']
	title_pic = request.form['title_pic']
	body = request.form['body']
	timestamp = datetime.utcnow()
	post = Post(title=title, title_pic=title_pic, body=body, timestamp=timestamp)
	db.session.add(post)
	db.session.commit()
	return redirect(url_for('.page', id=post.id))	

@post.route('/post/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
	post = models.Post.query.get_or_404(id)
	return render_template('post/edit.html', post=post)

@post.route('/post/update/<int:id>', methods=['POST'])
def update_post(id):
	post = models.Post.query.get_or_404(id)
	post.title = request.form['title']
	post.title_pic = request.form['title_pic']
	post.body = request.form['body']	
	post.timestamp = datetime.utcnow()	
	db.session.add(post)
	return redirect(url_for('.page', id = post.id))	

	