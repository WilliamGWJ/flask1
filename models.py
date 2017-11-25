from flask_sqlalchemy import SQLAlchemy
from main import app


db = SQLAlchemy(app)


class User(db.Model):
    """
    represents proected users
    """

    __tablename__ = 'users'
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<model user `{}`>".format(self.username)
