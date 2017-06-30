from flask import render_template, request, flash, session, redirect, url_for
from app import app, models, forms
from app import bucket
import pdb
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
                request.form['last_name'], request.form['email'],
                request.form['password'])
            reg = bucket.Application().register_user(user)
            if reg == 'Registered':
                flash('You have been successfully registered.')
                return redirect(url_for('login'))
            elif reg == 'Email exists':
                flash('User with the given Email already exists!.')
                return render_template('register.html', form=form)
            else:
                flash('Something went very wrong.')
                render_template('register.html', form=form)
    elif request.method == 'GET':
        return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Return and render login.html template if the method is GET.
    If the method is POST, the form form is validated and a Log is attempted.
    On successfull login the user is redirected to the home page.
    Else the user is redirected back to the home page.
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
                return redirect(url_for('home'))
            else:
                flash('Invalid User name or password')
                return render_template('login.html', form=form)
    elif request.method == 'GET':
        return render_template('login.html', form=form)


@app.route('/logout', methods=['GET'])
def logout():
    '''
    This logs the user out of the application
    '''
    if session.get('email', None) is not None:
        buck_app = bucket.Application()
        pdb.set_trace()
        res = buck_app.logout_user(session['email'])
        if res is True:
            email = session.pop(session['email'], None)
            flash(email + ' has been successfully logged out')
            return redirect(url_for('index'))
        else:
            return redirect('login')

# p bucket.Application()._signed_in_users
@app.route('/home')
def home():
    """Return and render home.html template."""
    if session.get('email', None) is not None:
        buck_app = bucket.Application()
        bucket_lists = buck_app.get_bucket_lists(session['email'])
        if bucket_lists == 'Not registered':
            return redirect(url_for('index'))
        elif isinstance(bucket_lists, list):
            return render_template('home.html', bucket_lists=bucket_lists)
    else:
        return redirect(url_for('index'))


@app.route('/createBuck', methods=['GET', 'POST'])
def create_bucket():
    """
    Return and render create_bucket.html template if GET
    If POST create the bucket list.
    """
    form = forms.CreateBucketForm()
    if request.method == 'POST':
        bucket_list = models.BucketList(request.form['name'],
        request.form['description'], request.form['date'],)
        buck_app = bucket.Application()
        res = buck_app.create_bucket_list(session['email'], bucket_list)
        if res == True:
            flash('BucketList created successfully')
            return redirect('home')
        else:
            flash('Something went wrong!!')
            return render_template('create_bucklist.html', form=form)
    elif request.method == 'GET':
        return render_template('create_bucklist.html', form=form)



@app.route('/removeBuck/<int:buck_id>')
def remove_bucket(buck_id):
    """ Removes a the user's bucketlist."""
    buck_app = bucket.Application()
    res = buck_app.remove_bucket_list(session['email'], buck_id)
    if res:
        flash('successfully deleted')
        return redirect(url_for('home'))
    else:
        flash('something went wrong')
        return redirect(url_for('home'))

@app.route('/viewBuck/<int:buck_id>')
def view_bucket(buck_id):
    """ Returns the page to view bucketlist items."""
    buck_app = bucket.Application()
    res = buck_app.view_bucket_list_items(session['email'], buck_id)
    if isinstance(res, list):
        return render_template('items.html', items=res, buck_id=buck_id)
    else:
        flash('something went wrong')
        return render_template('home.html')


@app.route('/createItem/<int:buck_id>', methods=['GET', 'POST'])
def create_item(buck_id):
    """
    Return and render create_item.html template if GET
    otherwise process item creation.
    """
    form = forms.CreateItemForm()
    if request.method == 'POST':
        item = models.BucketListItem(request.form['title'],
        request.form['description'], request.form['date'],)
        buck_app = bucket.Application()
        res = buck_app.create_bucket_list_item(session['email'], item, buck_id)
        if res == True:
            flash('Item  created successfully in BucketList')
            return redirect(url_for('view_bucket', buck_id=buck_id))
        else:
            flash('Something went wrong!!')
            return render_template('create_item.html', form=form)
    elif request.method == 'GET':
        return render_template('create_item.html', form=form, buck_id=buck_id)


@app.route('/removeItem/<int:buck_id>/<int:item_id>')
def remove_item(buck_id, item_id):
    """ remove Item and redirect to  """
    buck_app = bucket.Application()
    res = buck_app.remove_bucket_list_item(session['email'], buck_id, item_id)
    if res:
        flash('successfully deleted')
        return redirect(url_for('view_bucket', buck_id=buck_id))
    else:
        flash('something went wrong')
        return redirect(url_for('view_bucket', buck_id=buck_id))
