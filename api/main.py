from flask import Flask
from flask import jsonify

def create_app():
    app = Flask(__name__)
    return app

app = create_app()


@app.route('/', methods=['GET'])
def get_data():
    response = {
        'data':{
            'message': 'success'
        }
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)