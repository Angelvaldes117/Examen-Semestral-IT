import unittest
import logging
from flask import request, make_response, redirect, render_template, session, url_for, flash, jsonify
from flask_login import login_required, current_user

from app import create_app
from app.forms import TodoForm, DeleteTodoForm, UpdateTodoForm, ReservationForm, DeleteReservationForm, UpdateReservationForm
from app.firestore_service import get_todos, update_todo, put_todo, delete_todo, get_users, user_put, get_reservations, create_reservation, get_reservation, update_reservation, delete_reservation
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = create_app()

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('hello'))
    else:
        return redirect(url_for('auth.login'))

@app.route('/hello', methods=['GET', 'POST'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id
    todo_form = TodoForm()
    delete_form = DeleteTodoForm()
    update_form = UpdateTodoForm()

    context = {
        'user_ip': user_ip,
        'todos': get_todos(user_id=username),
        'username': username,
        'todo_form': todo_form,
        'delete_form': delete_form,
        'update_form': update_form
    }

    if todo_form.validate_on_submit():
        put_todo(user_id=username, description=todo_form.description.data)
        flash('Tu tarea se creó con éxito!')
        return redirect(url_for('hello'))

    return render_template('hello.html', **context)

@app.route('/todos/delete/<todo_id>', methods=['POST'])
@login_required
def delete_todo_route(todo_id):
    user_id = current_user.id
    delete_todo(user_id=user_id, todo_id=todo_id)
    flash('Tarea eliminada con éxito')
    return redirect(url_for('hello'))

@app.route('/todos/update/<todo_id>', methods=['POST'])
@login_required
def update_todo_route(todo_id):
    user_id = current_user.id
    done = request.form.get('done', type=bool)
    logger.info(f"Updating todo: user_id={user_id}, todo_id={todo_id}, done={done}")
    update_todo(user_id=user_id, todo_id=todo_id, done=done)
    flash('Tarea actualizada con éxito')
    return redirect(url_for('hello'))

@app.route('/reservations', methods=['GET', 'POST'])
@login_required
def reservations():
    reservation_form = ReservationForm()
    delete_form = DeleteReservationForm()

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'create':
            if reservation_form.validate_on_submit():
                reservation_data = {
                    'id_reserva': reservation_form.id_reserva.data,
                    'nombre_usuario': reservation_form.nombre_usuario.data,
                    'fecha': reservation_form.fecha.data,
                    'hora': reservation_form.hora.data,
                    'duracion': reservation_form.duracion.data,
                    'detalles': reservation_form.detalles.data
                }
                logger.info(f"Creating reservation: {reservation_data}")
                create_reservation(reservation_data)
                flash('Reserva creada con éxito', 'success')

        elif action == 'update':
            reservation_id = request.form.get('id_reserva')
            if reservation_id:
                updated_data = {
                    'nombre_usuario': reservation_form.nombre_usuario.data,
                    'fecha': reservation_form.fecha.data,
                    'hora': reservation_form.hora.data,
                    'duracion': reservation_form.duracion.data,
                    'detalles': reservation_form.detalles.data
                }
                logger.info(f"Updating reservation ID={reservation_id} with {updated_data}")
                update_reservation(reservation_id, updated_data)
                flash('Reserva actualizada con éxito', 'success')
        

        elif action == 'delete':
            reservation_id = request.form.get('reservation_id')
            if reservation_id:
                logger.info(f"Deleting reservation ID={reservation_id}")
                delete_reservation(reservation_id)
                flash('Reserva eliminada con éxito', 'success')

    # Obtener todas las reservaciones para mostrar en la página
    reservations = get_reservations()

    context = {
        'reservations': reservations,
        'reservation_form': reservation_form,
        'delete_form': delete_form
    }
    return render_template('reservations.html', **context)




@app.route('/lugares')
@login_required
def lugares():
    # Aquí puedes agregar la lógica que necesites, por ejemplo, obtener datos de lugares
    # o simplemente retornar una página de solo visualización.
    return render_template('upa.html')



@app.route('/json/todos', methods=['GET'])
@login_required
def json_todos():
    user_id = current_user.id
    todos = get_todos(user_id)
    todos_list = [todo.to_dict() for todo in todos]
    return render_template('json_view.html', data=todos_list, title="Tareas JSON")

@app.route('/json/users', methods=['GET'])
@login_required
def json_users():
    users = get_users()
    users_list = [user.to_dict() for user in users]
    return render_template('json_view.html', data=users_list, title="Usuarios JSON")

@app.route('/register_user', methods=['POST'])
@login_required
def register_user():
    user_data = request.get_json()
    logger.info(f"Received user data: {user_data}")
    user_put(user_data)
    return jsonify({"message": "Usuario creado con éxito"}), 201






