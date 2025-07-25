from flask import Blueprint, request, jsonify
from models.models import db, Courses_Notes

from datetime import date


notes_course = Blueprint('note_course', __name__, url_prefix='/notes_course')

@notes_course.route('/', methods=['GET'])
def get_notes():
    records = Courses_Notes.query.limit(10).all()

    response = [
        {
            'id': note.id,
            'title': note.title,
            'description': note.description,
            'created_at': note.created_at,
        }
        for note in records
    ]

    return jsonify(response), 200


@notes_course.route('/<int:note_id>', methods=['GET'])
def get_note_by_id(note_id):
    record = Courses_Notes.query.filter(
        db.extract("id", Courses_Notes.id) == note_id
    ).all()
    return jsonify(record), 200

@notes_course.route('/', methods=['POST'])
def post_note():
    req_json = request.get_json(silent=True)

    date_create = date.today()
    title = req_json['title']
    description = req_json['description']
    course_id = req_json['course_id']

    new_note = Courses_Notes(
            course_id=course_id,
            title=title,
            description=description,
            create_at=date_create
        )
    
    db.session.add(new_note)
    db.session.commit()

    return jsonify(
        {
            'data': {
                'message': 'Event create successfully',
                'status': True,
                'id': new_note.id
            }
        }, 201
    )

@notes_course.route('/<int:note_id>', methods=['PATCH'])
def patch_note(note_id):
    req_json = request.get_json(silent=True)
    

    title = req_json['title']
    description = req_json['description']

    notes_entry = Courses_Notes.query.get(note_id)

    if notes_entry:
        notes_entry.title = title
        notes_entry.description = description

        db.session.commit()


        return jsonify(
            {
                'data': {
                    'message': 'Event update successfully',
                    'status': True,
                    'id': notes_entry.id
                }
            }, 200
        )
    else:
        return jsonify(
            {
                'data': {
                    'message': 'Id note not found',
                    'status': False,
                    'id': notes_entry.id
                }
            }, 404
        )


@notes_course.route('/', methods=['DELETE'])
def delete_note():
    req_json = request.get_json(silent=True)

    id_ = int(req_json['id'])
    
    notes_deleted = Courses_Notes.query.get(id_)

    if notes_deleted:

        db.session.delete(notes_deleted)
        db.session.commit()

        return jsonify(
            {
                'data': {
                    'message': 'Event deleted successfully',
                    'status': True,
                    'id': id_
                }
            }, 200
        )
    else:
        return jsonify(
        {
            'data': {
                'message': 'Id not found',
                'status': False,
                'id': id_
            }
        }, 404
    )
