from flask import Blueprint, make_response, session, request, jsonify
import pandas as pd
import sqlite3
from uuid import uuid4
import bcrypt
from datetime import datetime
import os
import json

# user roles                # FIXME make user roles constants
USER = 1
ADMIN = 2

# status
ERROR = -1
FAILED = 0
SUCCESS = 1



auth_blueprint = Blueprint(
    name='auth',
    import_name=__name__,
    url_prefix='/auth',
)


@auth_blueprint.route('/register', methods=['POST'])
def register_user():
    try:
        data: dict = request.get_json()
        first_name: str = data.get('first_name')
        last_name: str = data.get('last_name')
        email: str = data.get('email')
        password: str = data.get('password')

        assert (first_name and last_name and email and password)
        
        
        # path generated relative to auth.py and not app.py
        path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+'/db/dev.db'
        con = sqlite3.connect(path)

        sql_query = f"""
        --sql
        SELECT EXISTS(SELECT 1 FROM users WHERE email = ?) AS email_already_in_use
        ;
        """
        df = pd.read_sql_query(sql=sql_query, con=con, params=(email, ))
        email_already_in_use = (df['email_already_in_use'].values[0] == 1)
        
        
        if email_already_in_use:
            con.close()
            response = make_response(jsonify({
                'status': FAILED,
                'message': 'Email already in use'
            }), 200)
            return response
        
        salt = bcrypt.gensalt(rounds=12)
        pw_enc = password.encode('utf-8')                       # FIXME make encoding setting
        pw_hash = bcrypt.hashpw(password=pw_enc, salt=salt)
        

        now = datetime.now()         #.strftime('%Y-%m-%d %H:%M:%S')
        user_data = {
            'user_id': [uuid4().hex],
            'first_name': [first_name],
            'last_name': [last_name],
            'email': [email],
            'password': [pw_hash.decode('utf-8')],
            'user_role': [USER],
            'created_at': [now],
            'updated_at': [now]
        }

        
        new_user = pd.DataFrame(user_data)
        new_user.to_sql(name='users', con=con, if_exists='append', index=False)
        con.close()

        response = jsonify({
            'status': SUCCESS,
            'message': 'User was added successfully.'
        }), 200
        return response
    
    except Exception as e:
        response = make_response(jsonify('Error with register. '), 400)
        return response

# sql_query = f"""
# --sql
# INSERT INTO users (user_id, first_name, last_name, email, password, user_role, created_at, updated_at) 
# VALUES (?,?,?,?,?,?,?,?)
# ;
# """


@auth_blueprint.route('/login', methods=['POST'])
def login_user():
    try: 
        data: dict = request.get_json()
        email: str = data.get('email')
        password: str = data.get('password')

        if not (email and password):
            response = jsonify({
                'status': FAILED, 
                'message': 'Missing payload.'
            }), 400 # BadRequest
            return response
        
        path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+'/db/dev.db'
        with sqlite3.connect(path) as con:
            sql_query = f"""
            --sql
            SELECT EXISTS(SELECT 1 FROM users WHERE email = ?) AS email_exists
            ;
            """
            
            result = pd.read_sql_query(sql_query, con, params=(email,))
            emailExists = (result['email_exists'].values[0] == 1)
            
            if not emailExists:
                response = jsonify({
                    'status': FAILED,
                    'message': 'Email not found.'
                }), 404 # NotFound
                return response

            sql_query = f"""
            --sql
            SELECT 
                [user_id],
                -- [first_name],
                -- [last_name],
                -- [email],
                [password]
            FROM users
            WHERE email = ?
            ;
            """
            result = pd.read_sql_query(sql_query, con, params=(email,))
            user_data = result.values.ravel().tolist()
            pw_hash: str = user_data.pop(-1)
            authorized = bcrypt.checkpw(password=password.encode('utf-8'), hashed_password=pw_hash.encode('utf-8'))
            
            # user_data = {
            #     'user_id': user_data[0],
            #     'first_name': user_data[1],
            #     'last_name': user_data[2],
            #     'email': user_data[3],
            #     'authorized': authorized
            # }

            if not authorized:
                response = jsonify({
                    'status': FAILED,
                    'message': 'Incorrect password.',
                    'authorized': authorized
                }), 401 # Unauthorized
                return response
            

            # bind user id to live session
            session['user-id'] = user_data[0]

            response = jsonify({
                'status': SUCCESS,
                'message': 'Login success.',
                'authorized': authorized
            }), 200 # OK
            return response
                
    except Exception:
        response = jsonify({'status': ERROR,
                            'message': 'Unexpected error occurred.'}), 500
        return response


@auth_blueprint.route('/logout', methods=['GET'])
def logout_user():
    pass

