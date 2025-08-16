from flask import Flask
from src.models import db
from controllers.manage_calendar import manage_calendar
from controllers.manage_company import companies
from controllers.manage_course_notes import notes_course
from controllers.manage_course import manage_course
from controllers.manage_notes import notes
from controllers.manage_project import manage_project
from controllers.manage_todo import manage_to_do
from controllers.manage_work_journal import work_journal

def create_app(env):
    app = Flask(__name__)
    app.config.from_object(env)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    app.register_blueprint(manage_calendar)
    app.register_blueprint(companies)
    app.register_blueprint(notes_course)
    app.register_blueprint(manage_course)
    app.register_blueprint(notes)
    app.register_blueprint(manage_project)
    app.register_blueprint(manage_to_do)
    app.register_blueprint(work_journal)

    return app