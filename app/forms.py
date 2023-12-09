from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, NumberRange

class CapturaForm(FlaskForm):
    nombre = StringField('Nombre del usuario', validators=[InputRequired()])
    colonia = StringField('Colonia', validators=[InputRequired()])
    calle = StringField('Calle', validators=[InputRequired()])
    telefono = StringField('Telefono', validators=[InputRequired()])
    pagina_web = StringField('Pagina Web', validators=[InputRequired()])


class BusquedaForm(FlaskForm):
    nombre_busqueda = StringField('Buscar por Nombre', validators=[InputRequired()])

class SignupForm(FlaskForm):
    nombre1 = StringField('nombre', validators=[InputRequired()])
    email1 = StringField('email', validators=[InputRequired()])
    password1 = StringField('password', validators=[InputRequired()])