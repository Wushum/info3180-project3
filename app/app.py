from flask import Flask

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# __init__.py ******

# app.config["SECRET_KEY"] = "Dont try guess"
# app.config['CSRF_ENABLED '] = False
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://wushum:winston@localhost/Wisher'
db = SQLAlchemy()
from app import views

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)
# app.config["SECRET_KEY"] = "ITSASECRET"
# app.config['CSRF_ENABLED '] = False
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config[
#     'SQLALCHEMY_DATABASE_URI'] = 'mysql://Rox116:fred116@localhost/Wishlist'
# db = SQLAlchemy(app)
# from app import views




# from app import app
# from flask import render_template, request, redirect, url_forfrom flask import Flask

# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)
