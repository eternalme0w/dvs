from flask import Blueprint, render_template
import pendulum
from flask_login import current_user

from .static.sc.schedule import date_schedule, get_date

views = Blueprint('views', __name__)

@views.route('/')
def main():
    return render_template('index.html')

@views.route('/capacity')
def capacity():
    return render_template('capacity.html', page_class = 'capacity-page', page_title = 'capacity')

@views.route('/routes')
def routes():
    return render_template('routes.html', page_class = 'routes-page', page_title = 'routes')

@views.route('/schedule/today')
def schedule():

    today = pendulum.now()
    d = today.strftime("%d/%m/%Y")
    today_sc = date_schedule(1307, today)
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

@views.route('profile')
def profile():
    return  render_template('profile.html', group=current_user.group)

