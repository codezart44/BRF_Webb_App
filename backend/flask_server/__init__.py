

from flask import Flask
# from flask_session import Session
from flask_cors import CORS


# import blueprints/
from routes.test import test_blueprint
from routes.auth import auth_blueprint
from routes.users import users_blueprint

# import error handlers/




def create_app():
    app = Flask(__name__)

    # app.secret_key = 'blah'
    # app.config['SESSION_TYPE'] = 'filesystem'
    # app.config['SESSION_FILE_DIR'] = 'database/flask_sessions'

    # Session(app)
    # config settings here for CORS
    CORS(app)

    register_blureprints(app=app)
    register_error_handlers(app=app)

    return app


def register_blureprints(app: Flask):
    '''Register Blueprints'''
    app.register_blueprint(test_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(users_blueprint)


def register_error_handlers(app: Flask):
    '''Register Error Handlers'''
    # app.register_error_handler()


app = create_app()