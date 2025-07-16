from flask import Flask
from flask import jsonify

def create_app(enviroment):
    app = Flask(__name__)
    return app

app = create_app()