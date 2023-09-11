# from flask import Flask
# from flask_session import Session
# from flask_cors import CORS


# def create_app():
    
#     app = Flask(__name__)

#     # Configure session to use filesystem

#     app.secret_key = 'super secret key'
#     app.config['SESSION_TYPE'] = 'filesystem'
#     app.config['SESSION_FILE_DIR'] = 'database/flask_sessions'
#     app.config['SESSION_COOKIE_SAMESITE'] = "None"
#     app.config['SESSION_COOKIE_SECURE'] = True

#     CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}}, supports_credentials=True) 

#     Session(app)

#     # from routers.workbook_router import workbook_blueprint
#     # app.register_blueprint(workbook_blueprint, url_prefix='/workbook')

#     return app