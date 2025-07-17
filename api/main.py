from flask import Flask
from flask import jsonify
from config import config
from models import db


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(env)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app


env = config['dev']
app = create_app(env)


@app.route('/', methods=['GET'])
def get_data():
    response = {
        'data':{
            'message': 'success'
        }
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run()