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