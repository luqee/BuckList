from flask import render_template, request, flash, session, redirect
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
            user = models.User(request.form['first_name'],
                request.form['last_name'],request.form['email'],
                request.form['password'])
            app = bucket.Application()
            if app.register_user(user):
                return redirect(url_for('login'))
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
            app = bucket.Application()
            if app.login_user(email, password):
                session['email'] = email
                flash('You were successfully logged in')
                return redirect('home.html')
            else:
                flash('Invalid User name or password')
                return render_template('login.html', form=form)
    elif request.method == 'GET':
        return render_template('login.html', form=form)


@app.route('/logout', methods=['GET'])
def logout():
    app = bucket.Application()
    app.logout_user(session['email'])
    session.pop(sesion['email'], None)
    return redirect(url_for('index'))


@app.route('/home')
def home():
    """
    Return and render home.html template.
    """
    if session('email', None) == None:
        flash('You need to log in first')
        return redirect(url_for('login'))
    else:
        app = bucket.Application()
        bucket_lists = app.get_bucket_lists(session['email'])
        return render_template('home.html', bucket_lists=bucket_lists)


@app.route('/createBuck', methods=['GET', 'POST'])
def create_bucket():
    """
    Return and render team.html template.
    """
    form = forms.CreateBucketForm()
    if request.method == 'POST':
        bucket_list = models.BucketList(request.form['name'], request.form['description'], request.form['date'],)
        app = bucket.Application()
        res = app.create_bucket_list(session['email'], bucket_list)
        if res == True:
            flash('BucketList created successfully')
            return render_template('home.html')
        else:
            flash('Something went wrong!!')
            return render_template('create_bucklist.html', form=form)
    elif request.method == 'GET':
        return render_template('create_bucklist.html', form=form)



@app.route('/removeBuck/<int:buck_id>')
def remove_bucket(buck_id):
    """
    Return and render team.html template.
    """
    app = bucket.Application()
    res = app.remove_bucket_list(sesion['email'], buck_id)
    if res:
        flash('successfully deleted')
        return render_template('home.html')
    else:
        flash('something went wrong')
        return render_template('home.html')

@app.route('/viewBuck/<int:buck_id>')
def view_bucket(buck_id):
    """
    Return and render team.html template.
    """
    app = bucket.Application()
    res = app.view_bucket_list_items(sesion['email'], buck_id)
    if isinstance(res, list):
        return render_template('items.html', items=res, buck_id=buck_id)
    else:
        flash('something went wrong')
        return render_template('home.html')


@app.route('/createItem/<int:buck_id>', methods=['GET', 'POST'])
def create_item():
    """
    Return and render team.html template.
    """
    form = forms.CreateItemForm()
    if request.method == 'POST':
        item = models.BucketListItem(request.form['title'], request.form['description'], request.form['date'],)
        app = bucket.Application()
        res = app.create_bucket_list_item(session['email'], item, buck_id)
        if res == True:
            flash('Item  created successfully in BucketList')
            return render_template('home.html')
        else:
            flash('Something went wrong!!')
            return render_template('create_item.html')
    elif request.method == 'GET':
        return render_template('create_item.html')


@app.route('/removeItem/<int:buck_id>/<int:item_id>')
def remove_item():
    """
    Return and render team.html template.
    """
    app = bucket.Application()
    res = app.remove_bucket_list_item(sesion['email'], buck_id, item_id)
    if res:
        flash('successfully deleted')
        return redirect(url_for('view_bucket', buck_id=buck_id))
    else:
        flash('something went wrong')
        return redirect(url_for('view_bucket', buck_id=buck_id))
