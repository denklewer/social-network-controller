from service.MusicService import MusicService
from flask import Blueprint, request, jsonify, make_response
from util.JSONEncoder import JSONEncoder
from flask_cors import CORS


musicService = MusicService()
JSONEncoder = JSONEncoder()
music = Blueprint('music', __name__)
CORS(music)


@music.route('/music', methods=['POST'])
def insert_music(music_data):
    music_service = MusicService()
    return music_service.insert_music(music_data);

@music.route('/load', methods=['POST'])
def load_music():
    data = request.get_json()
    if data is None or "email" not in data:
        return make_response(jsonify(
            {
                "status": "error",
                "reason": "invalid user"
            }
        ), 400)
    result = musicService.load_music(data['email'])
    if not result:
        return make_response(jsonify(
            {
                "status": "error",
                "reason": "music load was not correct"
            }
        ), 400)
    return JSONEncoder.encode(result)
