from flask import request, redirect, url_for
from flask_restful import Resource, fields, marshal_with
from . import db
from .models import List, ListFields, User, UserFields

class ToList(Resource):
    @marshal_with(ListFields)
    def get(self):
        list = List.query.all()
        return list



