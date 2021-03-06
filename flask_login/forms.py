from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=7)])
    confirm_password = PasswordField(label="Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Length(min=2, max=15)])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=7)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
