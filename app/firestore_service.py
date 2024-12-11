import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime, date, time



project_id = 'proyecto-441322'
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': project_id,
})


db = firestore.client()


def get_users():
    return db.collection('users').get()


def get_user(user_id):
    return db.collection('users').document(user_id).get()


def user_put(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password})


def get_todos(user_id):
    return db.collection('users')\
        .document(user_id)\
        .collection('todos').get()


def put_todo(user_id, description):
    todos_collection_ref = db.collection('users').document(user_id).collection('todos')
    todos_collection_ref.add({'description': description, 'done': False})


def delete_todo(user_id, todo_id):
    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.delete()


def update_todo(user_id, todo_id, done):
    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.update({'done': done})


def _get_todo_ref(user_id, todo_id):
    return db.document('users/{}/todos/{}'.format(user_id, todo_id))

def get_reservations():
    reservations = db.collection('reservations').get()
    result = []
    for reservation in reservations:
        data = reservation.to_dict()
        data['id'] = reservation.id
        if 'hora' in data and isinstance(data['hora'], str):
            try:
                data['hora'] = datetime.strptime(data['hora'], '%H:%M:%S').time()
            except ValueError:
                pass
        if 'fecha' in data and isinstance(data['fecha'], str):
            try:
                data['fecha'] = datetime.strptime(data['fecha'], '%Y-%m-%d').date()
            except ValueError:
                pass
        result.append(data)
    return result


def create_reservation(reservation_data):
    if isinstance(reservation_data.get('fecha'), date):
        reservation_data['fecha'] = reservation_data['fecha'].isoformat()
    if isinstance(reservation_data.get('hora'), time):
        reservation_data['hora'] = reservation_data['hora'].strftime('%H:%M:%S')
    reservation_ref = db.collection('reservations').document(reservation_data['id_reserva'])
    reservation_ref.set(reservation_data)


def get_reservation(reservation_id):
    doc = db.collection('reservations').document(reservation_id).get()
    if doc.exists:
        return doc.to_dict()
    return None


def update_reservation(reservation_id, reservation_data):
    if 'fecha' in reservation_data and isinstance(reservation_data['fecha'], date):
        reservation_data['fecha'] = reservation_data['fecha'].isoformat()
    if 'hora' in reservation_data and isinstance(reservation_data['hora'], time):
        reservation_data['hora'] = reservation_data['hora'].strftime('%H:%M:%S')
    reservation_ref = db.collection('reservations').document(reservation_id)
    reservation_ref.update(reservation_data)


def delete_reservation(reservation_id):
    reservation_ref = db.collection('reservations').document(reservation_id)
    reservation_ref.delete()

