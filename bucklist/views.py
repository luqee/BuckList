from flask import render_template
from app import app

"""
This module defines the routes to be used by the flask application instance.
"""

@app.route('/')
def index():
    """
    Return and render index.html template.
    """
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Return and render register.html template.
    """
    return render_template('register.html')

@app.route('/login')
def login():
    """
    Return and render login.html template.
    """
    return render_template('login.html')

@app.route('/home')
def home():
    """
    Return and render home.html template.
    """
    return render_template('home.html')
