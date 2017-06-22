from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
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
