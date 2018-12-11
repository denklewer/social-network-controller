import os
from flask import Flask
from controller.UserController import user
from controller.MusicController import music

app = Flask(__name__)
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(music, url_prefix='/music')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
