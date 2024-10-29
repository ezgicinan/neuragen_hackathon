# backend/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import Config
from flask.app import Flask

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    flask_bcrypt.init_app(app)

    # Register blueprints here when you add controllers
    # from .controllers.user_controller import user_bp
    # app.register_blueprint(user_bp)

    return app