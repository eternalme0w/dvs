from flask import Blueprint, render_template, request, redirect, url_for, flash
import pendulum
import requests
from .static.sc.schedule import date_schedule, get_date
from . import db
from .models import List, ListFields, User, UserFields

from flask_login import current_user

views = Blueprint('views', __name__)


@views.route('/')
def main():
    return render_template('index.html')


@views.route('/capacity')
def capacity():
    return render_template('capacity.html', page_class = 'capacity-page', page_title = 'capacity')


@views.route('/todo')
def todo():
    user = User.query.filter(User.group == current_user.group).first()
    response = user.list
    # response = List.query.all()
    return render_template('todo.html', page_class = 'todo-page', page_title = 'todo', res=response, len=len(response))
        

@views.route('/post_task', methods=['POST'])
def post_task():
    text_task = request.form.get('text')
    deadline = request.form.get('deadline')
    group = current_user.group
    task_check = List.query.filter_by(text=text_task, deadline=deadline, user_group=group).first()
    if task_check:
        flash('Check the list, such task already exists')
        return redirect(url_for('views.todo'))

    task = List(text=text_task, deadline=deadline,user_group=group)

    db.session.add(task)
    db.session.commit()
    return redirect(url_for('views.todo'))


@views.route('/del_task', methods=['POST'])
def del_task():
    k = int(request.form.get('id'))
    task = List.query.filter_by(id=k).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('views.todo'))


@views.route('/compl_task', methods=['POST'])
def compl_task():
    k = int(request.form.get('id'))
    task = List.query.filter_by(id=k).first()
    task.complete = True
    db.session.commit()
    return redirect(url_for('views.todo'))


@views.route('/encompl_task', methods=['POST'])
def encompl_task():
    k = int(request.form.get('id'))
    task = List.query.filter_by(id=k).first()
    task.complete = False
    db.session.commit()
    return redirect(url_for('views.todo'))


@views.route('/schedule/today')
def schedule():
    group = current_user.group
    today = pendulum.now()
    d = today.strftime("%d/%m/%Y")
    today_sc = date_schedule(group, today)
    return render_template('schedule.html',
        page_class = 'schedule-page', page_title = 'schedule',
         sc_date = d, sc = today_sc, current_date = today, pendulum = pendulum)


@views.route('/schedule/date/<n>/<m>/<y>')
def scdate(n, m, y):

    date = get_date([int(n), int(m), int(y)])
    d = date.strftime("%d/%m/%Y")
    today_sc = date_schedule(1307, date)
    return render_template('schedule.html',
        page_class = 'schedule-page', page_title = 'schedule', 
        sc_date = d, sc = today_sc, current_date = date, pendulum = pendulum)



