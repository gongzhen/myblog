from flask import Flask, request, render_template, redirect, url_for, request

app = Flask(__name__)

from views.home import home as home_blueprint
app.register_blueprint(home_blueprint)

from views.post import post as post_blueprint
app.register_blueprint(post_blueprint)