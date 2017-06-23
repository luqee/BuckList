from flask import render_template, request, flash, session
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
    if request.method == 'POST':
        app = bucket.Application()
        res = app.view_bucket_list_items(sesion['email'], buck_id)
        if isinstance(res, list):
            flash('successfully deleted')
            return render_template('items.html', items=res, buck_id = buck_id)
        else:
            flash('something went wrong')
            return render_template('home.html')
    elif request.method == 'GET':
        return render_template('items.html')


@app.route('/removeItem/<int:buck_id>')
def remove_item(request):
    """
    Return and render team.html template.
    """
    if request.method == 'POST':
        app = bucket.Application()
        res = app.remove_bucket_list_item(sesion['email'], request.args.get('buck_id'), request.args.get('item_id'))
        if res:
            flash('successfully deleted')
            return render_template('items.html', items=res, buck_id = buck_id)
        else:
            flash('something went wrong')
            return render_template('home.html')
    elif request.method == 'GET':
        return render_template('items.html')

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
                session['user_email'] = email
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
    app = bucket.Application()
    buckets = app.get_bucket_list(session['email'])
    if isinstance(buckets, list) and len(buckets) > 0:
        return render_template('home.html', buckets=buckets)
    else:
        flash('error')
        return render_template('home.html')


@app.route('/createBuck', methods=['GET', 'POST'])
def create_bucket():
    """
    Return and render team.html template.
    """
    form = forms.CreateBucketForm()
    if request.method == 'POST':
        bucketlist = models.BucketList(request.form['name'], request.form['description'], request.form['date'],)
        app = bucket.Application()
        res = app.create_bucket_list(session['email'], bucket)
        if res == True:
            flash('BucketList created successfully')
            return render_template('home.html')
        else:
            flash('Something went wrong!!')
            return render_template('create_bucklist.html', form=form)
    elif request.method == 'GET':
        return render_template('create_bucklist.html', form=form)


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
