# import pytest
# from src import create_app
# from config import config

# from src.models.models import db
# from src.controllers.manage_calendar import manage_calendar
# from src.controllers.manage_company import companies
# from src.controllers.manage_course_notes import notes_course
# from src.controllers.manage_course import manage_course
# from src.controllers.manage_notes import notes
# from src.controllers.manage_project import manage_project
# from src.controllers.manage_todo import manage_to_do
# from src.controllers.manage_work_journal import work_journal

# @pytest.fixture()
# def app():
#     env = config['test']
#     app = create_app(env)

#     with app.app_context():
#         db.init_app(app)
#         db.create_all()


#     app.register_blueprint(manage_calendar)
#     app.register_blueprint(companies)
#     app.register_blueprint(notes_course)
#     app.register_blueprint(manage_course)
#     app.register_blueprint(notes)
#     app.register_blueprint(manage_project)
#     app.register_blueprint(manage_to_do)
#     app.register_blueprint(work_journal)

#     yield app

#     with app.app_context():
#         db.drop_all()

# @pytest.fixture()
# def client(app):
#     return app.test_client()

# @pytest.fixture()
# def runner(app):
#     return app.test_cli_runner()