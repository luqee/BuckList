from flask import render_template, request, flash
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


@app.route('/about')
def about():
    """
    Return and render about.html template.
    """
    return render_template('about.html')


@app.route('/team')
def team():
    """
    Return and render team.html template.
    """
    return render_template('team.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Return and render register.html template.
    """
    form = forms.RegisterForm()
    if request.method == 'POST':
        if form.validate() is False:
            flash('All fields are required.')
            return render_template('register.html', form=form)
        else:
            # fname = request.form['last_name']
            # fname = request.form['first_name']
            # lname = request.form['last_name']
            # email = request.form['email']
            # password = request.form['password']
            # user = models.User()
            # user.f_name = request.form['first_name']
            # user.l_name = request.form['last_name']
            # user.email = request.form['email']
            # user.password = request.form['password']
            user = models.User(request.form['first_name'],
                request.form['last_name'],request.form['email'],
                request.form['password'])
            app = bucket.Application()
            if app.register_user(user):
                return render_template('login.html', form=form)
    elif request.method == 'GET':
        return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Return and render login.html template.
    """
    form = forms.LoginForm()
    if request.method == 'POST':
        if form.validate() is False:
            flash('All fields are required.')
            return render_template('login.html', form=form)
        else:
            email = request.form['email']
            password = request.form['password']
            # user = models.User()
            # user.email = request.form['email']
            # user.password = request.form['password']
            app = bucket.Application()
            # return app.login_user(email, password)
            if app.login_user(email, password):
                return render_template('home.html')
            else:
                return 'Not able'
    elif request.method == 'GET':
        return render_template('login.html', form=form)


@app.route('/home', methods=['GET', 'POST'])
def home():
    """
    Return and render home.html template.
    """

    return render_template('home.html')
