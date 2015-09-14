from flask import Blueprint, render_template, abort, redirect, url_for, request

home = Blueprint('home', __name__)

@home.route('/')
def index():
    return render_template('home/index.html')

@home.route('/about')
def about():
    return render_template('home/about.html')

@home.route('/projects')
def projects():
    return render_template('home/projects.html')

@home.route('/resume')
def resume():
    return render_template('home/resume.html')

@home.route('/contacts')
def contacts():
    return render_template('home/contacts.html')


