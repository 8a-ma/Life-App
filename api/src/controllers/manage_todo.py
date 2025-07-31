from flask import Blueprint, request, jsonify
from models.models import db, DailyToDo


from datetime import date, datetime

manage_to_do = Blueprint('manage_to_do', __name__, url_prefix='/to_do')

@manage_to_do.route('/', methods=['GET'])
def get_todo():
    records = DailyToDo.query.all()
    response = [{
        'id': todo.id,
        'title': todo.title,
        'date_start': todo.date_start,
        'date_finish': todo.date_finish if todo.date_finish else None,
        'completed': todo.completed
    } for todo in records]

    return jsonify(response), 200

@manage_to_do.route('/', methods=['POST'])
def create_todo():
    req_json = request.get_json()

    new_todo = DailyToDo(
        title = req_json['title'],
        date_start = datetime.strptime(req_json['date_start'], '%Y-%m-%d'),
        date_finish = datetime.strptime(req_json['date_finish'], '%Y-%m-%d') if 'date_finish' in req_json else None,
        completed = req_json['completed'],
    )

    if new_todo:

        db.session.add(new_todo)
        db.session.commit()

        return jsonify(
            {
                'data': {
                    'message': 'Event create successfully',
                    'status': True,
                    'id': new_todo.id
                }
            }, 201
        )
    else:
        return jsonify(
        {
            'data': {
                'message': 'Id agenda not found',
                'status': False,
            }
        }, 404
    )

@manage_to_do.route('/<int:todo_id>/', methods=['PATCH'])
def patch_todo(todo_id):
    req_json = request.get_json(silent=True)

    todo_entry = DailyToDo.query.get(todo_id)

    if todo_id:
        todo_entry.title = req_json['title']
        todo_entry.date_start = datetime.strptime(req_json['date_start'], '%Y-%m-%d')
        todo_entry.date_finish = datetime.strptime(req_json['date_finish'], '%Y-%m-%d') if 'date_finish' in req_json else None
        todo_entry.completed = req_json['completed']

        db.session.commit()

        return jsonify(
            {
                'data': {
                    'message': 'Event update successfully',
                    'status': True,
                    'id': todo_entry.id
                }
            }, 200
        )
    else:
        return jsonify(
            {
                'data': {
                    'message': 'Id agenda not found',
                    'status': False,
                    'id': todo_entry.id
                }
            }, 200
        )