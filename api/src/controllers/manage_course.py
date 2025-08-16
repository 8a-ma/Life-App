from flask import Blueprint, request, jsonify
from src.models import db, Courses

manage_course = Blueprint('manage_course', __name__, url_prefix='/course')

@manage_course.route('/<int:course_id>', methods=['GET'])
def get_course_by_id(course_id):
    # req_json = request.get_json(silent=True)
    record = Courses.query.filter(
        db.extract("id", Courses.id) == course_id
    ).all()

    return jsonify(record), 200

@manage_course.route('/', methods=['GET'])
def get_course():
    # req_json = request.get_json(silent=True)
    records = Courses.query.limit(10).all()

    response = [
        {
            'id': course.id,
            'name': course.name,
            'description': course.description,
            'status': course.status,
            'progress': course.progress
        }
        for course in records
    ]

    return jsonify(response), 200

@manage_course.route('/', methods=['POST'])
def post_course():
    req_json = request.get_json(silent=True)
    name = req_json['name']
    description = req_json['description']
    status = req_json['status']
    progress = int(req_json['progress'])

    new_course = Courses(name=name,
                         description=description,
                         status=status,
                         progress=progress
                         )
    
    db.session.add(new_course)
    db.session.commit()
    return jsonify(
        {
            'data': {
                'message': 'Event create successfully',
                'status': True,
                'id': new_course.id
            }
        }, 201
    )


@manage_course.route('/<int:course_id>', methods=['PATCH'])
def patch_course(course_id):
    req_json = request.get_json(silent=True)

    name = req_json['name']
    description = req_json['description']
    status = req_json['status']
    progress = int(req_json['progress'])

    course_entry = Courses.query.get(course_id)

    if course_entry:
        course_entry.name = name
        course_entry.description = description
        course_entry.status = status
        course_entry.progress = progress

        db.session.commit()

        return jsonify(
        {
            'data': {
                'message': 'Event update successfully',
                'status': True,
                'id': course_entry.id
            }
        }, 200
    )
    else:
        return jsonify(
        {
            'data': {
                'message': 'Id agenda not found',
                'status': False,
                'id': course_entry.id
            }
        }, 404
    )



@manage_course.route('/', methods=['DELETE'])
def delete_course():
    req_json = request.get_json(silent=True)

    id_ = int(req_json['id'])
    
    course_deleted = Courses.query.get(id_)

    if course_deleted:

        db.session.delete(course_deleted)
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
                'message': 'Id agenda not found',
                'status': False,
                'id': id_
            }
        }, 404
    )