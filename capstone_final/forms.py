from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, PasswordField, IntegerField, DecimalField, SubmitField
from wtforms.validators import  DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[ DataRequired(), Email()])
    password = PasswordField('Password', validators=[ DataRequired() ])
    submit = SubmitField('Sign In')


class RegisterForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    username = StringField('Username', validators =[ DataRequired() ])
    gender = StringField('Gender')
    email = StringField('Email', validators=[ DataRequired(), Email() ])
    password = StringField('Password', validators=[ DataRequired() ])
    confirm_password = PasswordField('Confirm Password', validators=[ DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class VenueForm(FlaskForm):
    name = StringField('Restaurants Name', validators=[ DataRequired() ])
    city = StringField('City', validators=[ DataRequired() ])
    state = StringField('State', validators=[ DataRequired() ])
    location = StringField('Location', validators=[ DataRequired()])
    male = IntegerField('Male %')
    female = IntegerField('Female %')
    other = IntegerField('Other %')
    image = StringField('Image URL')
    submit = SubmitField('Submit')

class UpdateForm(FlaskForm):

    male = IntegerField('Male %')
    female = IntegerField('Female %')
    other = IntegerField('Other %')
    submit = SubmitField('Submit')


