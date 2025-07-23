from flask import Flask, request
from flask import jsonify
from config import config
from models import db, YearAgenda

from datetime import date, datetime


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(env)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app


env = config['dev']
app = create_app(env)


@app.route('/calendar', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def manage_calendar():
    if request.method == 'GET':
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

    
    elif request.method == 'POST':
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



    elif request.method == 'PATCH':
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


    elif request.method == 'DELETE':
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


    else:
        response = {
            'data': {
                'messege': 'Error method not found',
                'status': False
            }
        }
        return jsonify(response, 404)

# @app.route('/to-do', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
# def data():
#     if request.method == 'GET':
#         pass
    
#     elif request.method == 'POST':
#         pass

#     elif request.method == 'UPDATE':
#         pass

#     elif request.method == 'DELETE':
#         pass

#     else:
#         response = {
#             'data': {
#                 'messege': 'Error'
#             }
#         }
#         return jsonify(response)


# @app.route('/courses_list', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
# def data():
#     if request.method == 'GET':
#         pass
    
#     elif request.method == 'POST':
#         pass

#     elif request.method == 'UPDATE':
#         pass

#     elif request.method == 'DELETE':
#         pass

#     else:
#         response = {
#             'data': {
#                 'messege': 'Error'
#             }
#         }
#         return jsonify(response)
# @app.route('/course/<course_id>', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
# def data():
#     if request.method == 'GET':
#         pass
    
#     elif request.method == 'POST':
#         pass

#     elif request.method == 'UPDATE':
#         pass

#     elif request.method == 'DELETE':
#         pass

#     else:
#         response = {
#             'data': {
#                 'messege': 'Error'
#             }
#         }
#         return jsonify(response)


# @app.route('/notes', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
# def data():
#     if request.method == 'GET':
#         pass
    
#     elif request.method == 'POST':
#         pass

#     elif request.method == 'UPDATE':
#         pass

#     elif request.method == 'DELETE':
#         pass

#     else:
#         response = {
#             'data': {
#                 'messege': 'Error'
#             }
#         }
#         return jsonify(response)


# @app.route('/projects_list', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
# def data():
#     if request.method == 'GET':
#         pass
    
#     elif request.method == 'POST':
#         pass

#     elif request.method == 'UPDATE':
#         pass

#     elif request.method == 'DELETE':
#         pass

#     else:
#         response = {
#             'data': {
#                 'messege': 'Error'
#             }
#         }
#         return jsonify(response)
# @app.route('/project/<project_id>', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
# def data():
#     if request.method == 'GET':
#         pass
    
#     elif request.method == 'POST':
#         pass

#     elif request.method == 'UPDATE':
#         pass

#     elif request.method == 'DELETE':
#         pass

#     else:
#         response = {
#             'data': {
#                 'messege': 'Error'
#             }
#         }
#         return jsonify(response)


# @app.route('/works_list', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
# def data():
#     if request.method == 'GET':
#         pass
    
#     elif request.method == 'POST':
#         pass

#     elif request.method == 'UPDATE':
#         pass

#     elif request.method == 'DELETE':
#         pass

#     else:
#         response = {
#             'data': {
#                 'messege': 'Error'
#             }
#         }
#         return jsonify(response)
# @app.route('/work/<work_id>', methods=['GET', 'POST', 'UPDATE', 'DELETE'])
# def data():
#     if request.method == 'GET':
#         pass
    
#     elif request.method == 'POST':
#         pass

#     elif request.method == 'UPDATE':
#         pass

#     elif request.method == 'DELETE':
#         pass

#     else:
#         response = {
#             'data': {
#                 'messege': 'Error'
#             }
#         }
#         return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True)