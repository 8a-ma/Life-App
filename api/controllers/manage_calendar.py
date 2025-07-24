from flask import Blueprint, request, jsonify
from models.models import db, YearAgenda

from datetime import date, datetime

manage_calendar = Blueprint('manage_calendar', __name__, url_prefix='/calendar')

@manage_calendar.route('/', methods=['GET'])
def get_agenda():
    req_json = request.get_json(silent=True)
    year_ = int(req_json['year'])
    # month = req_json['month']

    records = YearAgenda.query.filter(
        db.extract("year", YearAgenda.date) == year_
    ).all()

    results = [
        {
            'id' : record.id,
            'date' : record.date.strftime('%d-%m-%Y'),
            'title': record.title,
            'description': record.description,
        }
        for record in records
    ]

    return jsonify(results), 200

@manage_calendar.route('/', methods=['POST'])
def post_agenda():
    req_json = request.get_json(silent=True)
        
    date_ = date.today()
    title = req_json['title']
    description = req_json['description']

    new_agenda = YearAgenda(date=date_, title=title, description=description)

    db.session.add(new_agenda)
    db.session.commit()

    return jsonify(
        {
            'data': {
                'message': 'Event create successfully',
                'status': True,
                'id': new_agenda.id
            }
        }, 201
    )

@manage_calendar.route('/', methods=['PATCH'])
def patch_agenda():
    req_json = request.get_json(silent=True)

    id_ = int(req_json['id'])

    date_ = req_json['date']
    title = req_json['title']
    description = req_json['description']

    agenda_entry = YearAgenda.query.get(id_)

    if agenda_entry:
        agenda_entry.date = datetime.strptime(date_, '%Y-%m-%d')
        agenda_entry.title = title
        agenda_entry.description = description

        db.session.commit()

        return jsonify(
        {
            'data': {
                'message': 'Event update successfully',
                'status': True,
                'id': agenda_entry.id
            }
        }, 200
    )
    else:
        return jsonify(
        {
            'data': {
                'message': 'Id agenda not found',
                'status': False,
                'id': agenda_entry.id
            }
        }, 404
    )

@manage_calendar.route('/', methods=['DELETE'])
def delete_agenda():
    req_json = request.get_json(silent=True)

    id_ = int(req_json['id'])
    
    agenda_deleted = YearAgenda.query.get(id_)

    if agenda_deleted:

        db.session.delete(agenda_deleted)
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