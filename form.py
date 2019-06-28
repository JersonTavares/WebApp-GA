from flask_wtf import Form
from wtforms import TextField, IntegerField, SubmitField, SelectField, PasswordField
from wtforms import validators, ValidationError

class loginForm(Form):
   user = TextField("User",[validators.Required("Please enter your name.")])
   password = PasswordField('Password', [validators.Required("Please enter your name.")])
   submit = SubmitField('Login')
