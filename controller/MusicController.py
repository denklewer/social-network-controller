from flask import Flask, app

from service.MusicService import MusicService


@app.route('/music', methods=['POST'])
def insert_music(music_data):
    music_service = MusicService()
    return music_service.insert_music(music_data);