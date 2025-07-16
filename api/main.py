from flask import Flask
from flask import jsonify
from config import config


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(env)

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