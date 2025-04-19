from flask import Flask
from flask_login import LoginManager
from application.models import db, User

login_manager = LoginManager()
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.debug = True

    db.init_app(app)
    login_manager.init_app(app)

    # Import routes here after initializing everything
    with app.app_context():
        import application.controllers  # Don't use 'import *'
    
    return app
