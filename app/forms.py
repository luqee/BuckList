from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired, Email


class RegisterForm(Form):
	first_name = StringField('First Name',
	 	validators=[DataRequired('Please provide your first name')])
	last_name = StringField('Last Name',
		validators=[DataRequired('Please provide your last name')])
	email = StringField('Email',
		validators=[DataRequired('Please enter your email'), Email()])
	password = PasswordField('Password',
		validators=[DataRequired('Please enter a password')])
	submit = SubmitField('Register')

class LoginForm(Form):
	email = StringField('Email',
	 validators=[DataRequired('Please enter your email'), Email()])
	password = PasswordField('Password',
	 validators=[DataRequired('Please enter a password')])
	submit = SubmitField('Sign in')

class CreateBucketForm(Form):
	name = StringField('Name',
	 	validators=[DataRequired('Please provide your Bucketlist\'s name')])
	description = StringField('Description',
		validators=[DataRequired('Please provide your description')])
	date = StringField('Date',
		validators=[DataRequired('Please provide the date')])
	submit = SubmitField('Create')

class CreateItemForm(Form):
	title = StringField('Title',
	 	validators=[DataRequired('Please provide your Bucketlist Item name')])
	description = StringField('Description',
		validators=[DataRequired('Please provide your description')])
	date = StringField('Date',
		validators=[DataRequired('Please provide the date')])
	submit = SubmitField('Create Item')
