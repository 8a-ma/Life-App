from flask import Flask, request
from flask import jsonify
from config import config
from models import db


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(env)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app


env = config['dev']
app = create_app(env)


@app.route('/calendar', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
def data():
    pass

@app.route('/to-do', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
def data():
    pass


@app.route('/courses_list', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
def data():
    pass
@app.route('/course/<course_id>', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
def data():
    pass


@app.route('/notes', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
def data():
    pass


@app.route('/projects_list', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
def data():
    pass
@app.route('/project/<project_id>', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
def data():
    pass


@app.route('/works_list', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
def data():
    pass
@app.route('/work/<work_id>', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
def data():
    pass



if __name__ == '__main__':
    app.run()