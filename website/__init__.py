from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'zxctruedeadinsideghoulsfzxc'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    from .views import views
    from .models import User


    app.register_blueprint(views, url_prefix='/')

    
    return app