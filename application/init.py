from flask import Flask
from flask_login import LoginManager
from application.models import db, User
from api import api  # Import the API instance only

login_manager = LoginManager()
login_manager.login_view = 'login' # type: ignore

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.debug = True

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        import application.controllers  # routes
        api.init_app(app)  # Initialize Flask-Restful here

    return app
