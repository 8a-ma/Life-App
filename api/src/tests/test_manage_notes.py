# import pytest
# from flaskr.models.models import db, Notes
# from flaskr.controllers.manage_notes import notes
# from datetime import date


# @pytest.fixture
# def init_db():
#     # Add sample data to the database
#     note1 = Notes(title='Test Note 1', description='Description 1', created_at=date.today())
#     note2 = Notes(title='Test Note 2', description='Description 2', created_at=date.today())
#     db.session.add(note1)
#     db.session.add(note2)
#     db.session.commit()

# def test_get_notes(client, init_db):
#     response = client.get('/notes/')
#     assert response.status_code == 200
#     data = response.get_json()
#     assert len(data) == 2
#     assert data[0]['title'] == 'Test Note 1'
#     assert data[1]['title'] == 'Test Note 2'

# def test_get_note_by_id(client, init_db):
#     response = client.get('/notes/1')
#     assert response.status_code == 200
#     data = response.get_json()
#     assert len(data) == 1
#     assert data[0]['title'] == 'Test Note 1'

# def test_post_note(client):
#     response = client.post('/notes/', json={
#         'title': 'New Note',
#         'description': 'New Description',
#         'created_at': date.today()
#     })
#     assert response.status_code == 201
#     data = response.get_json()
#     assert data['data']['message'] == 'Event create successfully'
#     assert data['data']['status'] is True

# def test_patch_note(client, init_db):
#     response = client.patch('/notes/1', json={
#         'title': 'Updated Note',
#         'description': 'Updated Description'
#     })
#     assert response.status_code == 200
#     data = response.get_json()
#     assert data['data']['message'] == 'Event update successfully'
#     assert data['data']['status'] is True
#     # Verify the update
#     response = client.get('/notes/1')
#     updated_data = response.get_json()
#     assert updated_data[0]['title'] == 'Updated Note'

# def test_delete_note(client, init_db):
#     response = client.delete('/notes/', json={'id': 3})
#     assert response.status_code == 200
#     data = response.get_json()
#     assert data['data']['message'] == 'Event deleted successfully'
#     assert data['data']['status'] is True
#     # Verify deletion
#     response = client.get('/notes/3')
#     assert response.status_code == 200
#     assert len(response.get_json()) == 0  # Note should be deleted

# def test_delete_nonexistent_note(client):
#     response = client.delete('/notes/', json={'id': 999})  # Nonexistent ID
#     assert response.status_code == 404
#     data = response.get_json()
#     assert data['data']['message'] == 'Id not found'
#     assert data['data']['status'] is False