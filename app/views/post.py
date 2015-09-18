from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Post
from app import models
from .. import db

post = Blueprint('post', __name__)

# http://stackoverflow.com/questions/7974771/flask-blueprint-template-folder
@post.route('/post/index', methods=['GET', 'POST'])
def index():
	return render_template('post/index.html')

@post.route('/post/page/<int:id>')
def page(id):
	post = models.Post.query.get_or_404(id);
	return render_template('post/post.html', post = post)

@post.route('/post/write')
def write():
	return render_template('post/write.html')

@post.route('/post/create', methods=['POST'])
def create():	
	title = request.form['title']
	title_pic = request.form['title_pic']
	body = request.form['body']
	post = Post(title=title, title_pic=title_pic, body=body)
	db.session.add(post)
	db.session.commit()
	return redirect(url_for('.page', id=post.id))	
	