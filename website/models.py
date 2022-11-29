from flask_login import UserMixin
from . import db

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.String(4), unique=True)
    password = db.Column(db.String(100))

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    deadline = db.Column(db.String(10))
    complete = db.Column(db.Boolean)
