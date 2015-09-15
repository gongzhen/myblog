from flask import Blueprint, render_template, redirect, url_for

post = Blueprint('post', __name__)

# http://stackoverflow.com/questions/7974771/flask-blueprint-template-folder
@post.route('/post/<int:id>')
def pages(id):
	post = Post.at(id).getone();
	return render_template('post.html', post=post)

@post.route('/post/write')
def write():
	return render_template('post/write.html')

@post.route('/post/create', methods=['POST'])
def create():
	return redirect(url_for('post', id=1))	

@post.route('/post/edit/<int:id>')
def edit(id):
	return redirect(url_for('post/edit.html'))		