from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from .models import User, List

auth = Blueprint("auth", __name__)

groups = ['0301',	'0301',	'0302',	'0303',	'0304',	'0305',	'0306',	'0307',	'0308',	'0361',	'0362',	'0363',	'0370',	'0371',	'0372',	'0373',	'0374',	'0375',	'0381',	'0382',	'0383',	'0391',	'0392',	'0395',	'1300',	'1301',	'1302',	'1303',	'1304',	'1305',	'1306',	'1307',	'1308',	'1361',	'1362',	'1363',	'1370',	'1371',	'1373',	'1374',	'1375',	'1376',	'1381',	'1383',	'1384',	'1391',	'1392',	'1395',	'2300',	'2301',	'2302',	'2303',	'2304',	'2305',	'2306',	'2307',	'2308',	'2309',	'2310',	'2311',	'2361',	'2362',	'2363',	'2364',	'2370',	'2371',	'2372',	'2373',	'2374',	'2375',	'2376',	'2381',	'2382',	'2383',	'2384',	'2391',	'2392',	'2395',	'7300',	'7301',	'7302',	'7303',	'7304',	'7307',	'7308',	'7309',	'7371',	'7373',	'7374',	'7381',	'7385',	'7391',	'7395',	'8300',	'8301',	'8302',	'8303',	'8304',	'8305',	'8306',	'8307',	'8308',	'8309',	'8310',	'8361',	'8362',	'8371',	'8373',	'8374',	'8376',	'8385',	'8387',	'8391',	'8395',	'9301',	'9302',	'9303',	'9304',	'9305',	'9306',	'9307',	'9308',	'9309',	'9361',	'9362',	'9363',	'9370',	'9371',	'9372',	'9373',	'9374',	'9375',	'9381',	'9382',	'9383',	'9391',	'9392']

@auth.route('/')
def login():
    if current_user.is_authenticated:
        return redirect(url_for("views.main"))
    return render_template('login.html')


@auth.route('/', methods=['POST'])
def login_post():
    group = request.form.get('group')
    password = request.form.get('password')
    user = User.query.filter_by(group=group).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user)
    return redirect(url_for('views.main'))


@auth.route('/signup')
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("views.main"))
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    group = request.form.get('group')
    password = request.form.get('password')

    user = User.query.filter_by(group=group).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    if group not in groups:
        flash('this group is not exist')

    new_user = User(group=group, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))