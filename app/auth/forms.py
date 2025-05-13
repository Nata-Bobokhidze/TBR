from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class SignupForm(FlaskForm):
    name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=50)])
    surname = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=50)])
    username = StringField('Username', validators = [DataRequired(), Length(min=3, max=20)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=6, max=20, message='Password must be at least 6 and at most 20 characters long')])

    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')