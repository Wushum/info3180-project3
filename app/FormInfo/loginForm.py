from flask.ext.wtf import Form
from wtforms import StringField, validators, PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):

    username = StringField(
        "username", [DataRequired("You must enter a username")])
    password = PasswordField(
        "password", [DataRequired("You must enter a password")])
Status API Training Shop Blog About
© 2016 GitHub, Inc. Terms Privacy Security Contact Help