from flask import Blueprint, request, jsonify
from models.models import db, WorkJournal

from datetime import date, datetime

work_journal = Blueprint('work_journal', __name__, url_prefix='/work_journal')

@work_journal.route('/', methods=['GET'])
def get_work_journals():
    records = WorkJournal.query.limit(10).all()

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

@work_journal.route('/<int:work_journal_id>', methods=['GET'])
def get_journal_by_id(work_journal_id):
    record = WorkJournal.query.filter(
        db.extract("id", WorkJournal.id) == work_journal_id
    ).all()
    return jsonify(record), 200

@work_journal.route('/', methods=['POST'])
def create_work_journal():
    data = request.get_json(silent=True)
    new_journal = WorkJournal(
        id_company=data['id_company'],
        title=data['title'],
        created_at=date.today(),
        description=data['description']
    )
    db.session.add(new_journal)
    db.session.commit()
    return jsonify(
        {
            'data': {
                'message': 'Event create successfully',
                'status': True,
                'id': new_journal.id
            }
        }, 201
    )

@work_journal.route('/<int:work_journal_id>', methods=['PATCH'])
def update_work_journal(work_journal_id):
    data = request.get_json(silent=True)
    
    
    journal_entry = WorkJournal.query.get(work_journal_id)
    if journal_entry:
        journal_entry.id_company = data['id_company']
        journal_entry.title = data['title']
        journal_entry.description = data['description']

        db.session.commit()
        return jsonify(
            {
                'data': {
                    'message': 'Event update successfully',
                    'status': True,
                    'id': journal_entry.id
                }
            }, 200
        )
    else:
        return jsonify(
            {
                'data': {
                    'message': 'Id note not found',
                    'status': False,
                    'id': journal_entry.id
                }
            }, 404
        )
    
@work_journal.route('/', methods=['DELETE'])
def delete_work_journal():
    req = request.get_json(silent=True)
    journal = WorkJournal.query.get(req['id'])
    
    if journal:
        db.session.delete(journal)
        db.session.commit()

        return jsonify(
            {
                'data': {
                    'message': 'Event deleted successfully',
                    'status': True,
                    'id': req['id']
                }
            }, 200
        )
    else:
        return jsonify(
        {
            'data': {
                'message': 'Id not found',
                'status': False,
                'id': req['id']
            }
        }, 404
    )
