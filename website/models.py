from flask_login import UserMixin
from flask_restful import fields
from . import db


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.String(4), unique=True)
    password = db.Column(db.String(100))
    list = db.relationship('List', backref='user')


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    deadline = db.Column(db.String(10))
    complete = db.Column(db.Boolean, default=False)
    user_group = db.Column(db.String, db.ForeignKey('user.group'))


UserFields = {
    'id': fields.Integer,
    'group': fields.String,
    'password': fields.String,
}
ListFields = {
    'id': fields.Integer,
    'text': fields.String,
    'deadline': fields.String,
    'complete': fields.Boolean,
    'group': fields.Integer
}
