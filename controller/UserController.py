from service.UserService import UserService
from flask import Blueprint, request, jsonify, make_response
from util.JSONEncoder import JSONEncoder
from flask_cors import CORS

userService = UserService()
JSONEncoder = JSONEncoder()
user = Blueprint('user', __name__)
CORS(user)


@user.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data is None or "email" not in data or "password" not in data:
        return make_response(jsonify(
            {
                "status": "error",
                "reason": "request is invalid"
            }
        ), 400)
    result = userService.login(data['email'], data['password'])
    if not result:
        return make_response(jsonify(
            {
                "status": "error",
                "reason": "wrong username or password"
            }
        ), 400)
    return JSONEncoder.encode(result), 200


@user.route('/current', methods=['POST'])
def current():
    data = request.get_json()
    if data is None or "email" not in data:
        return make_response(jsonify(
            {
                "status": "error",
                "reason": "request is invalid"
            }
        ), 400)

    result = userService.get_user(data['email'])
    if not result:
        return make_response(jsonify(
            {
                "status": "error",
                "reason": "wrong username or password current"
            }
        ), 400)
    return JSONEncoder.encode(result), 200


@user.route('/', methods=['PUT'])
def updateUser():
    data = request.get_json()
    if data is None or "email" not in data:
        return make_response(jsonify(
            {
                "status": "error",
                "reason": "request is invalid"
            }
        ), 400)

    result = userService.update_user(data)
    if not result:
        return make_response(jsonify(
            {
                "status": "error",
                "reason": "wrong username or password"
            }
        ), 400)
    return JSONEncoder.encode(result), 200

@user.route('/', methods=['POST'])
def insertUser():
    data = request.get_json()
    if data is None or "email" not in data:
        return make_response(jsonify(
            {
                "status": "error",
                "reason": "request is invalid"
            }
        ), 400)

    result = userService.insert_user(data)
    if not result:
        return make_response(jsonify(
            {
                "status": "error",
                "reason": "wrong username or password"
            }
        ), 400)
    return JSONEncoder.encode(result), 200

@user.route('/GetTeam', methods=['POST'])

def getteam():
    data = request.get_json()
    if data is None or "email" not in data:
        return make_response(jsonify(
            {
                "status": "error",
                "reason":"request team is invalid"
            }
        ),400)
    result = userService.get_team(data['email'])
    if not result:
        return make_response(jsonify(
            {
                "status": "error",
                "reason" : "get team was not correct"
            }
        ),400)
    return JSONEncoder.encode(result)

