import logging
from flask import Blueprint, jsonify, request
from app.firestore_service import get_reservations, create_reservation, get_reservation,update_reservation, delete_reservation
from app.firestore_service import get_todos, put_todo, update_todo, delete_todo
from app.firestore_service import get_users, user_put

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

api_bp = Blueprint('api', __name__)

# @api_bp.route('/clients', methods=['GET'])
# def get_clients_endpoint():
#     clients = get_clients()
#     clients_list = [client.to_dict() for client in clients]
#     logging.info(f"Sending clients data: {clients_list}")
#     return jsonify(clients_list)

# @api_bp.route('/clients', methods=['POST'])
# def create_client_endpoint():
#     client_data = request.get_json()
#     logging.info(f"Received client data: {client_data}")
#     create_client(client_data)
#     return jsonify({"message": "Cliente creado con éxito"}), 201

# @api_bp.route('/clients/<client_id>', methods=['GET'])
# def get_client_endpoint(client_id):
#     client = get_client(client_id)
#     client_data = client.to_dict()
#     logging.info(f"Sending client data: {client_data}")
#     return jsonify(client_data)

# @api_bp.route('/clients/<client_id>', methods=['PUT'])
# def update_client_endpoint(client_id):
#     client_data = request.get_json()
#     logging.info(f"Received update data for client {client_id}: {client_data}")
#     update_client(client_id, client_data)
#     return jsonify({"message": "Cliente actualizado con éxito"})

# @api_bp.route('/clients/<client_id>', methods=['DELETE'])
# def delete_client_endpoint(client_id):
#     logging.info(f"Deleting client with ID: {client_id}")
#     delete_client(client_id)
#     return jsonify({"message": "Cliente eliminado con éxito"})

@api_bp.route('/todos', methods=['GET'])
def get_todos_endpoint():
    user_id = request.args.get('user_id')
    todos = get_todos(user_id)
    todos_list = [todo.to_dict() for todo in todos]
    logging.info(f"Sending todos data for user {user_id}: {todos_list}")
    return jsonify(todos_list)

@api_bp.route('/todos', methods=['POST'])
def create_todo_endpoint():
    user_id = request.json.get('user_id')
    description = request.json.get('description')
    logging.info(f"Received todo data: user_id={user_id}, description={description}")
    put_todo(user_id, description)
    return jsonify({"message": "Tarea creada con éxito"}), 201

@api_bp.route('/todos/<todo_id>', methods=['PUT'])
def update_todo_endpoint(todo_id):
    user_id = request.json.get('user_id')
    done = request.json.get('done')
    logging.info(f"Received update data for todo {todo_id}: user_id={user_id}, done={done}")
    update_todo(user_id, todo_id, done)
    return jsonify({"message": "Tarea actualizada con éxito"})

@api_bp.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todo_endpoint(todo_id):
    user_id = request.json.get('user_id')
    logging.info(f"Deleting todo with ID: {todo_id} for user {user_id}")
    delete_todo(user_id, todo_id)
    return jsonify({"message": "Tarea eliminada con éxito"})

@api_bp.route('/users', methods=['GET'])
def get_users_endpoint():
    users = get_users()
    users_list = [user.to_dict() for user in users]
    logging.info(f"Sending users data: {users_list}")
    return jsonify(users_list)

@api_bp.route('/users', methods=['POST'])
def create_user_endpoint():
    user_data = request.get_json()
    logging.info(f"Received user data: {user_data}")
    user_put(user_data)
    return jsonify({"message": "Usuario creado con éxito"}), 201


# Obtener todas las reservaciones
@api_bp.route('/reservations', methods=['GET'])
def get_reservations_endpoint():
    reservations = get_reservations()
    reservations_list = [reservation.to_dict() for reservation in reservations]
    logging.info(f"Sending reservations data: {reservations_list}")
    return jsonify(reservations_list)

# Crear una nueva reservación
@api_bp.route('/reservations', methods=['POST'])
def create_reservation_endpoint():
    reservation_data = request.json
    logging.info(f"Received reservation data: {reservation_data}")
    create_reservation(reservation_data)
    return jsonify({"message": "Reserva creada con éxito"}), 201

# Actualizar una reservación existente
@api_bp.route('/reservations/<reservation_id>', methods=['PUT'])
def update_reservation_endpoint(reservation_id):
    updated_data = request.json
    logging.info(f"Updating reservation {reservation_id} with data: {updated_data}")
    update_reservation(reservation_id, updated_data)
    return jsonify({"message": "Reserva actualizada con éxito"})

# Eliminar una reservación
@api_bp.route('/reservations/<reservation_id>', methods=['DELETE'])
def delete_reservation_endpoint(reservation_id):
    logging.info(f"Deleting reservation with ID: {reservation_id}")
    delete_reservation(reservation_id)
    return jsonify({"message": "Reserva eliminada con éxito"})

# Endpoint para crear una reserva
@api_bp.route('/reservations', methods=['POST'])
def create_reservation_endpoint():
    reservation_data = request.json
    logging.info(f"Received reservation data: {reservation_data}")
    
    # Llamamos a la función para guardar la reserva en la base de datos
    create_reservation(reservation_data)
    
    return jsonify({"message": "Reserva creada con éxito"}), 201



