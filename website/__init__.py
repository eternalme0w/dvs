from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'zxctruedeadinsideghoulsfzxc'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    #api = Api(app)
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .models import User
    # from .todo_api import GetList, DeleteTask, PostTask, PutComplete

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    # api.add_resource(GetList, '/get_list')
    # api.add_resource(DeleteTask, '/delete_task/<int:k>')
    # api.add_resource(PutComplete, '/put_complete/<int:k>')

    
    return app