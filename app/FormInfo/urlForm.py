from flask.ext.wtf import Form
from wtforms import StringField, validators, PasswordField
from wtforms.validators import DataRequired, URL


class UrlForm(Form):
    url = StringField(
        "url", [DataRequired("You must entera URL"), URL(False, "Enter a valid URL")])
   
   
   