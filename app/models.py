from . import db
from datetime import datetime

class Post(db.Model):
	__tablename__= 'posts'
	id = db.Column(db.Integer, primary_key = True)
	title =db.Column(db.String(64), unique=True)
	title_pic = db.Column(db.String(64), unique=True)
	body = db.Column(db.Text)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
