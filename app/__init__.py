from flask import Flask, request, render_template, redirect, url_for, request

app = Flask(__name__)

from views.index import index as index_blueprint
app.register_blueprint(index_blueprint)
