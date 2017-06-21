from flask import render_template, request
from app import app, models, forms
from app import bucket
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
    form = forms.RegisterForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('register.html', form = form)
        else:
            # fname = request.form['last_name']
            # fname = request.form['first_name']
            # lname = request.form['last_name']
            # email = request.form['email']
            # password = request.form['password']
            user = models.User()
            user.f_name = request.form['first_name']
            user.l_name = request.form['last_name']
            user.email = request.form['email']
            user.password = request.form['password']
            # user = models.User(request.form['first_name'], request.form['last_name'],request.form['email'], request.form['password'])
            return user.l_name
            if bucket.Application.register_user(user):
                return render_template('home.html')
    elif request.method == 'GET':
        return render_template('register.html', form = form)

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
