
from flask import Blueprint, make_response, request


test_blueprint = Blueprint(
    name='test',
    import_name=__name__,
    url_prefix='/test'
)


@test_blueprint.route('/ping', methods=['GET'])
def ping():
    response = make_response('pong', 200)
    return response

@test_blueprint.route('/echo', methods=['POST'])
def echo():
    try:
        # raise KeyError
        content:list = request.get_json()['content']
        response = make_response(content, 200)
        return response
    except KeyError:
        response = make_response(f'KeyError', 400)
        return response

@test_blueprint.route('/echo/<int:user_id>', methods=['GET'])
def echo_param(user_id:int):
    try:
        response = make_response(str(user_id), 200)
        return response
    except Exception:
        response = make_response(f'Error', 400)
        return response