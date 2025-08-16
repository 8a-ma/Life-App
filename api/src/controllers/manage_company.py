from flask import Blueprint, request, jsonify
from src.models import db, Companys


companies = Blueprint('companies', __name__, url_prefix='/companies')

@companies.route('/', methods=['GET'])
def get_companies():
    records = Companys.query.all()

    response = [
        {
            'id': record.id,
            'name': record.name,
            'cargo': record.cargo,

        }
        for record in records
    ]
    return jsonify(response), 200

# def get_company_by_id('/<int:company_id>', methods=['GET'])

@companies.route('/', methods=['POST'])
def post_companie():
    data = request.get_json(silent=True)

    new_companie = Companys(
            name=data['name'],
            cargo = data['cargo'],
        )
    
    db.session.add(new_companie)
    db.session.commit()

    return jsonify(
        {
            'data': {
                'message': 'Event create successfully',
                'status': True,
                'id': new_companie.id
            }
        }, 201
    )

@companies.route('/<int:company_id>', methods=['PATCH'])
def update_company(company_id):
    company = Companys.query.get(company_id)
    data = request.get_json(silent=True)
    
    if company:
        company.name = data['name']
        company.cargo = data['cargo']

        db.session.commit()
        return jsonify(
                {
                    'data': {
                        'message': 'Event update successfully',
                        'status': True,
                        'id': company.id
                    }
                }, 200
            )
    else:
        return jsonify(
            {
                'data': {
                    'message': 'Id note not found',
                    'status': False,
                    'id': company.id
                }
            }, 404
        )
    
@companies.route('/', methods=['DELETE'])
def delete_note():
    req_json = request.get_json(silent=True)

    id_ = int(req_json['id'])
    
    companie_deleted = Companys.query.get(id_)

    if companie_deleted:

        db.session.delete(companie_deleted)
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

