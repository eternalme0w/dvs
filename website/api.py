from flask import request, redirect, url_for
from flask_restful import Resource, fields, marshal_with
from . import db
from .models import List, ListFields, User, UserFields

from .static.sc.schedule import date_schedule, get_date


class Schedule(Resource):
    def get(self):
        date = get_date([10, 12, 2022])
        d = date.strftime("%d/%m/%Y")
        today_sc = date_schedule(1307, date)
        return today_sc

