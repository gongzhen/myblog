from flask import Blueprint, render_template, request, redirect, url_for
from ..models import Post
from .. import db

post = Blueprint('post', __name__)

# http://stackoverflow.com/questions/7974771/flask-blueprint-template-folder
@post.route('/post/<int:id>')
def pages(id):
	post = Post.query.get_or_404(id);
	return render_template('post.html', post=[post])

@post.route('/post/write')
def write():
	return render_template('post/write.html')

@post.route('/post/create', methods=['POST'])
def create():	
	title = request.form['title']
	title_pic = request.form['title_pic']
	body = request.form['body']
	
	print title
	print title_pic
	print body
	posts = Post(title=title, title_pic=title_pic, body=body)
	db.session.add(post)
	return redirect(url_for('pages', id=post.id))	

@post.route('/post/edit/<int:id>')
def edit(id):
	return redirect(url_for('post/edit.html'))		