
import os
from dotenv import load_dotenv

# extensions/
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from .extensions import db, bcrypt

# models/
from project.models.user import User
# from project.models.laundry import LaundryBooking

# blueprints/
# from .api.routes import ...




def create_app():
    app = Flask(__name__)

    # Register settings
    dotenv_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+'/.env'
    load_dotenv(dotenv_path=dotenv_path)
    app_settings = os.getenv('APP_SETTINGS')        # adjust settings in .env
    app.config.from_object(app_settings)


    mount_extensions(app=app)
    # register_blueprints(app=app)
    # register_error_handlers(app=app)
    return app


def mount_extensions(app:Flask):
    ''''''
    db.init_app(app)
    bcrypt.init_app(app)


def register_blueprints(app:Flask):
    '''Register Blueprints'''
    # app.register_blueprint(...)


def register_error_handlers(app:Flask):
    '''Register Error Handlers'''
    # app.register_error_handler('Some Exception', 'Error handler')


app = create_app()

