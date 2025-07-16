from os import path

class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG=True
    # SQLALCHEMY_DATABASE_URI = 
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'dev': DevelopmentConfig,
}