from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Length(min=3, max=20)
    ])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=6, max=20,  message='Password must be at least 6 and at most 20 characters long')
    ])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), Length(min=3, max=20)
    ])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=6, max=20, message='Password must be at least 6 and at most 20 characters long')
    ])
    submit = SubmitField('Log In')
