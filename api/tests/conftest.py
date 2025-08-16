import pytest

from src import create_app
from src.models import db
from config import config

@pytest.fixture()
def app():
    env = config['test']
    app = create_app(env)

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture()
def client(app):
    return app.test_client()
    
