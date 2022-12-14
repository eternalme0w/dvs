from flask import request
from flask_restful import Resource, marshal_with
from . import db
from .models import List, ListFields


class GetList(Resource):
    @marshal_with(ListFields)
    def get(self):
        list = List.query.all()
        return list, 201

class PostTask(Resource):
    @marshal_with(ListFields)
    def post(self):
        data = request.json
        task = List(text=data["text"], deadline=data["deadline"])
        db.session.add(task)
        db.session.commit()
        return ("succesfully posted a new task")

class DeleteTask(Resource):
    @marshal_with(ListFields)
    def delete(self,k):
        task = List.query.filter_by(id=k).first()
        db.session.delete(task)
        db.session.commit()
        return task, 203

class PutComplete(Resource):
    @marshal_with(ListFields)
    def put(self, k):
        task = List.query.filter_by(id=k).first()
        data = request.json
        task.complete = data["complete"]
        db.session.commit()
        return task, 204

