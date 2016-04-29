from sqlalchemy import Column, Integer, String, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from app import db


class Item(db.Model):
    """WishList Item"""

    __tablename__ = "Item"
    package = "web 2"

    id = Column(Integer, primary_key=True)
    username = Column(
        String(100), ForeignKey("Profile.username"), nullable=False)
    url = Column(String(500))
    title = Column(String(100))
    description = Column(String(500))
    thumbnail = Column(String(100))

    def __init__(self, username=None, url=None, title=None, description=None, thumbnail=None):
        self.username = username
        self.url = url
        self.title = title
        self.description = description
        self.thumbnail = thumbnail