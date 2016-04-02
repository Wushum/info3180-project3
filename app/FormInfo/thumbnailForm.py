from flask.ext.wtf import Form
from wtforms import StringField, validators, PasswordField
from wtforms.validators import DataRequired, URL
from UrlForm import UrlForm


class ThumbnailForm(UrlForm):
    title = StringField("title", [DataRequired("There has to be a title")])
    description = StringField("description", [DataRequired(
        "There must be a description")])