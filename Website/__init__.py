from flask import Flask
from.views import views #Blueprint
from.auth import auth   #Blueprint

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'FinStarter Project'

    app.register_blueprint(views, url_prefix= '/')
    app.register_blueprint(auth, url_prefix= '/')

    
    return app