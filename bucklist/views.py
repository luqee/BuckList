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
