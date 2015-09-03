from flask import Blueprint, render_template, abort, redirect, url_for, request
from jinja2 import TemplateNotFound
from . import home
import json, datetime

@home.route('/')
def index():
    return render_template('index.html')

@home.route('/about')
def about():
    return render_template('about.html')

@home.route('/projects')
def projects():
    return render_template('projects.html')

@home.route('/resume')
def resume():
    return render_template('resume.html')

@home.route('/contacts')
def contacts():
    return render_template('contacts.html')
