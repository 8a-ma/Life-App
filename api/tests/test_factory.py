from src.__init__ import create_app
from config import config

def test_config():
    assert not create_app().testing
    assert create_app(config['test']).testing