from flask import Blueprint, request, jsonify
from src.models import db, Projects

from datetime import date

manage_project = Blueprint('manage_project', __name__, url_prefix='/projects')

@manage_project.route('/', methods=['GET'])
def get_projects():
    records = Projects.query.limit(10).all()

    response = [
        {
            'id': project.id,
            'title': project.title,
            'description': project.description,
            'create_at': project.create_at,
            'status': project.status
        }
        for project in records
    ]

    return jsonify(response), 200


@manage_project.route('/<int:project_id>', methods=['GET'])
def get_project_by_id(project_id):
    # req_json = request.get_json(silent=True)
    record = Projects.query.filter(
        db.extract("id", Projects.id) == project_id
    ).all()

    return jsonify(record), 200

@manage_project.route('/', methods=['POST'])
def post_project():
    req_json = request.get_json(silent=True)
    title = req_json['title']
    description = req_json['description']
    status = req_json['status']
    create_at = date.today()

    new_project = Projects(title=title,
                         description=description,
                         create_at=create_at,
                         status=status,
                         )
    
    db.session.add(new_project)
    db.session.commit()
    return jsonify(
        {
            'data': {
                'message': 'Event create successfully',
                'status': True,
                'id': new_project.id
            }
        }, 201
    )

@manage_project.route('/<int:course_id>', methods=['PATCH'])
def patch_project(course_id):
    req_json = request.get_json(silent=True)

    title = req_json['title']
    description = req_json['description']
    status = req_json['status']

    project_entry = Projects.query.get(course_id)

    if project_entry:
        project_entry.title = title
        project_entry.description = description
        project_entry.status = status

        db.session.commit()

        return jsonify(
        {
            'data': {
                'message': 'Event update successfully',
                'status': True,
                'id': project_entry.id
            }
        }, 200
    )
    else:
        return jsonify(
        {
            'data': {
                'message': 'Id agenda not found',
                'status': False,
                'id': project_entry.id
            }
        }, 404
    )

@manage_project.route('/', methods=['DELETE'])
def delete_project():
    req_json = request.get_json(silent=True)

    id_ = int(req_json['id'])
    
    project_deleted = Projects.query.get(id_)

    if project_deleted:

        db.session.delete(project_deleted)
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