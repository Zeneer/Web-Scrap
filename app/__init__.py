from flask import Flask
from pymongo import MongoClient


app = Flask(__name__, template_folder='./templates', static_folder='./static')

# Configuración de la conexión a MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017'  # Cambia esto con tu URI de MongoDB

# Clave secreta para CSRF
app.config['SECRET_KEY'] = 'AHGKJJLJDA6565AD54F6A'  # Reemplaza esto con una cadena aleatoria y segura

# Inicializar la conexión a MongoDB
mongo = MongoClient(app.config['MONGO_URI'])


from app import routes


