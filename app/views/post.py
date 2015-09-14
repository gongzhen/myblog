from flask import Blueprint, render_template

post = Blueprint('post', __name__)

# http://stackoverflow.com/questions/7974771/flask-blueprint-template-folder
@post.route('/post/1')
def pages():
	return render_template('post/1.html')

@post.route('/post/write')
def write():
	return render_template('post/write.html')	