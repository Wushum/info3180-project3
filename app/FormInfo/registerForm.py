from flask.ext.wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from LoginForm import LoginForm
from ..Models.Profile import Profile
from ..Validators.DuplicateUser import DuplicateUser


class RegisterForm(Form):
    username = StringField("username", [DataRequired(
        "You must enter a username"), DuplicateUser("This username is taken")])
    password = PasswordField(
        "password", [DataRequired("You must enter a password")])
    retype_password = PasswordField(
        "retype-password", [EqualTo('password', "Password must match")])
    email = StringField("email", [DataRequired(
        "Email has to have a value"), Email("Enter a valid email address here")])