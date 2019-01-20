from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class RegistrationForm(FlaskForm):
    username = StringField('Username')
    
    submit = SubmitField('Sign Up')