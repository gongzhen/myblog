from flask import Flask, request, render_template, redirect, url_for, request

app = Flask(__name__)

from views.home import home as home_blueprint
app.register_blueprint(home_blueprint)
