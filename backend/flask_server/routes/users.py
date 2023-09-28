
from flask import Blueprint, session, request, make_response, jsonify
import json


users_blueprint = Blueprint(
    name='users', 
    import_name=__name__, 
    url_prefix='/users',
)


@users_blueprint.route('/get', methods=['GET'])
def get_user_info():
    user_id = session.get('user-id')
    print(user_id)

    return json.dumps({
        'user-id': user_id
    }), 200




