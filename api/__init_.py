from flask import Flask
from models.models import db
from controllers.manage_calendar import manage_calendar

def create_app(env):
    app = Flask(__name__)
    app.config.from_object(env)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    app.register_blueprint(manage_calendar)

    return app