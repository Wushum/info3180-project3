from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from app import db


class Profile(db.Model):
    """Model for a User profile"""
    __tablename__ = 'Profile'

    id = Column(Integer, primary_key=True)
    item = relationship('Item', lazy='joined')
    password = Column(String(100))
    email = Column(String(100))
    username = Column(
        String(100), nullable=False, primary_key=True, index=True)

    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = password
        self.email = email

    def validate(self):
        user = Profile.query.filter_by(username=self.username).first()
        if user == None:
            return False
        if user.password == self.password:
            return True
        else:
            return False