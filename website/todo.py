from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import requests
from . import db
from .models import User

todo = Blueprint('todo', __name__)


@todo.route('/todo')
def login():
    response = requests.get('http://127.0.0.1:5004/get_list')
    return render_template('todo.html', res=response.json(), len=len(response.json()))

