from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, DateField, TimeField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email  

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class TodoForm(FlaskForm):
    description = StringField('Descripción', validators=[DataRequired()])
    submit = SubmitField('Crear')

class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Borrar')

class UpdateTodoForm(FlaskForm):
    submit = SubmitField('Actualizar')


class ReservationForm(FlaskForm):
    id_reserva = StringField('ID Reserva', validators=[DataRequired()])
    nombre_usuario = StringField('Nombre del Usuario', validators=[DataRequired()])
    fecha = DateField('Fecha', format='%Y-%m-%d', validators=[DataRequired()])
    hora = TimeField('Hora', validators=[DataRequired()])  # Este campo devuelve un objeto datetime.time
    duracion = IntegerField('Duración (en minutos)', validators=[DataRequired()])
    detalles = TextAreaField('Detalles')
    submit = SubmitField('Guardar')

class UpdateReservationForm(FlaskForm):
    nombre_usuario = StringField('Nombre del Usuario', validators=[DataRequired()])
    fecha = DateField('Fecha', validators=[DataRequired()], format='%Y-%m-%d')
    hora = TimeField('Hora', validators=[DataRequired()])
    duracion = IntegerField('Duración (minutos)', validators=[DataRequired()])
    detalles = TextAreaField('Detalles', validators=[DataRequired()])
    submit = SubmitField('Actualizar')


class DeleteReservationForm(FlaskForm):  
    submit = SubmitField('Borrar')