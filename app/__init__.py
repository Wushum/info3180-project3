from flask import Flask

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config["SECRET_KEY"] = "Dont try guess"
app.config['CSRF_ENABLED '] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://wushum:winston@localhost/Wisher'
db = SQLAlchemy(app)
from app import views