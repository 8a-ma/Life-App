from os import path
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent

class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(ROOT_DIR, 'storage', 'database.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(ROOT_DIR, 'storage', 'database.sqlite3') # 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True


config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
}