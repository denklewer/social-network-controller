from flask import Flask
from controller.UserController import user

app = Flask(__name__)
app.register_blueprint(user, url_prefix='/user')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
