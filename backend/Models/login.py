from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length,Email

class LoginForm(FlaskForm):
    email = EmailField(name='Email', validators=[DataRequired(), Email()])
    password = PasswordField(name='Password', validators=[DataRequired(), Length(min=6)])
    loginbutton = SubmitField(name='Login')