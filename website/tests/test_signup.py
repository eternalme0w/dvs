from werkzeug.security import generate_password_hash, check_password_hash

from main import app
from website.models import User
from website import db


def test_sugnup():
    client = app.test_client()
    group = "pytest5"
    password = "passwordhard"
    new_user = User(group=group, password=generate_password_hash(password, method='sha256'))
    with app.app_context():
        db.session.add(new_user)
        db.session.commit()

    with app.app_context():
        user = User.query.filter_by(group=group).first()
    if check_password_hash(user.password, password):
        success = True
    assert success == True





