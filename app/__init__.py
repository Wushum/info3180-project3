import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/lab7'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://abvsxfjmsnzrmf:xQqm4QltLO3oPktilH-G9a17aC@ec2-54-83-36-90.compute-1.amazonaws.com:5432/dd92jb06bbucik"
db = SQLAlchemy(app)
db.create_all()

from app import views, models

# from flask import Flask
# #from flask.ext.sqlalchemy import SQLAlchemy
# #from flask.ext.login import LoginManager

# app = Flask(__name__)
# #app.config['SQLALCHEMY_DATABASE_URI'] = ''
# app.config.from_pyfile('config.py')

# # Initialize SQLAlchemy
# db = SQLAlchemy(app)

# # Initialize Login Manager
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "login"

# from app import views, models
