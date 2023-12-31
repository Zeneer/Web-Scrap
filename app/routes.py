# Importa las bibliotecas y clases necesarias
import uuid
from bs4 import BeautifulSoup
from bson import ObjectId
from flask import render_template, session , request, redirect, url_for
import requests
from app import app, mongo
from .forms import CapturaForm, SignupForm
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Establece el backend Agg antes de importar pyplot
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import random
import re
from passlib.hash import pbkdf2_sha256
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




db = mongo['pueba_formulario']  # Nombre de la base de datos
coleccion = db['usuarios'] #Nombre de la coleccion de la DB


def calificacion_general_universidad():
    # Genera un valor aleatorio que simula la calificación general
    calificacion = np.random.uniform(low=0, high=100)

    # Redondea la calificación a dos decimales
    calificacion = round(calificacion, 2)

    # Establece un umbral para determinar si la universidad es "buena" o "mala"
    umbral_buena = 70

    # Determina si la universidad es "buena" o "mala" basándose en el umbral
    estado_universidad = "Buena" if calificacion >= umbral_buena else "Mala"

    # Configura el backend de matplotlib para Agg
    plt.switch_backend('Agg')

    # Crea una representación visual de la calificación
    plt.bar(["Calificación General"], [calificacion], color='skyblue')
    plt.xlabel('Universidad')
    plt.ylabel('Nivel')
    plt.title('Calificación General de la Universidad')
    plt.ylim(0, 100)  # Establece el rango del eje y de 0 a 100



    # Convierte la gráfica a un formato que puede ser integrado en HTML
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)
    img_encoded = base64.b64encode(img_buf.read()).decode('utf-8')
    plt.close()

    return calificacion, estado_universidad, img_encoded

def bullyng_general_universidad():
    # Genera un valor aleatorio que simula la calificación general
    calificacion1 = np.random.uniform(low=0, high=100)

    # Redondea la calificación a dos decimales
    calificacion1 = round(calificacion1, 2)

    # Establece un umbral para determinar si la universidad es "buena" o "mala"
    umbral_buena1 = 80

    # Determina si la universidad es "buena" o "mala" basándose en el umbral
    estado_bullyng = "Alto" if calificacion1 >= umbral_buena1 else "Bajo"

    # Configura el backend de matplotlib para Agg
    plt.switch_backend('Agg')

    # Crea una representación visual de la calificación
    plt.bar(["Calificación General"], [calificacion1], color='red')
    plt.xlabel('Universidad')
    plt.ylabel('Nivel bullyng')
    plt.title('Bullyng General de la Universidad')
    plt.ylim(0, 100)  # Establece el rango del eje y de 0 a 100



    # Convierte la gráfica a un formato que puede ser integrado en HTML
    img_buf1 = BytesIO()
    plt.savefig(img_buf1, format='png')
    img_buf1.seek(0)
    img_encoded1 = base64.b64encode(img_buf1.read()).decode('utf-8')
    plt.close()

    return calificacion1, estado_bullyng, img_encoded1

def decersion_general_universidad():
    # Genera un valor aleatorio que simula la calificación general
    calificacion2 = np.random.uniform(low=0, high=100)

    # Redondea la calificación a dos decimales
    calificacion2 = round(calificacion2, 2)

    # Establece un umbral para determinar si la universidad es "buena" o "mala"
    umbral_buena2 = 70

    # Determina si la universidad es "buena" o "mala" basándose en el umbral
    estado_decersion = "Alto" if calificacion2 >= umbral_buena2 else "Bajo"

    # Configura el backend de matplotlib para Agg
    plt.switch_backend('Agg')

    # Crea una representación visual de la calificación
    plt.bar(["Calificación General"], [calificacion2], color='orange')
    plt.xlabel('Universidad')
    plt.ylabel('Nivel de decersion')
    plt.title('Decersion General de la Universidad')
    plt.ylim(0, 100)  # Establece el rango del eje y de 0 a 100



    # Convierte la gráfica a un formato que puede ser integrado en HTML
    img_buf2 = BytesIO()
    plt.savefig(img_buf2, format='png')
    img_buf2.seek(0)
    img_encoded2 = base64.b64encode(img_buf2.read()).decode('utf-8')
    plt.close()

    return calificacion2, estado_decersion, img_encoded2

def ingreso_general_universidad():
    # Genera un valor aleatorio que simula la calificación general
    calificacion3 = np.random.uniform(low=0, high=100)

    # Redondea la calificación a dos decimales
    calificacion3 = round(calificacion3, 2)

    # Establece un umbral para determinar si la universidad es "buena" o "mala"
    umbral_buena3 = 50

    # Determina si la universidad es "buena" o "mala" basándose en el umbral
    estado_ingreso = "Alto" if calificacion3 >= umbral_buena3 else "Bajo"

    # Configura el backend de matplotlib para Agg
    plt.switch_backend('Agg')

    # Crea una representación visual de la calificación
    plt.bar(["Calificación General"], [calificacion3], color='green')
    plt.xlabel('Universidad')
    plt.ylabel('Nivel de Ingreso')
    plt.title('Ingreso General de la Universidad')
    plt.ylim(0, 100)  # Establece el rango del eje y de 0 a 100



    # Convierte la gráfica a un formato que puede ser integrado en HTML
    img_buf3 = BytesIO()
    plt.savefig(img_buf3, format='png')
    img_buf3.seek(0)
    img_encoded3 = base64.b64encode(img_buf3.read()).decode('utf-8')
    plt.close()

    return calificacion3, estado_ingreso, img_encoded3

@app.route('/resultadoJson', methods=['GET', 'POST']) 

def Capjson():
    if request.method == 'POST':
        try:
            # Intenta cargar la lista JSON desde la entrada del usuario
            datos_json = json.loads(request.form['datos_json'])
        except json.JSONDecodeError as e:
            return render_template('fail.html')

        # Solicita al usuario ingresar el nombre de la colección
        nombre_coleccion = request.form['nombre_coleccion']

        # Selecciona la colección (si no existe, se creará)
        coleccion = db[nombre_coleccion]

        # Inserta los datos en la colección
        resultado = coleccion.insert_many(datos_json)

        # Imprime los IDs de los documentos insertados
        mensaje = f"Documentos insertados con éxito. IDs: {resultado.inserted_ids}"
        return render_template('exito.html', mensaje=mensaje)



@app.route('/', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        # Obtiene el valor ingresado por el usuario en el formulario de búsqueda
        valor_busqueda = request.form['valor_busqueda']


        # Utiliza una expresión regular para hacer la búsqueda insensible a mayúsculas y minúsculas
        regex = re.compile(valor_busqueda, re.IGNORECASE)

        # Especifica los campos que deseas recuperar
        #campos_deseados = {'_id': 0, 'universidad_id': 0,'universidad_cp': 0,'gmaps_latitud': 0, 'gmaps_longitud': 0, 'estado_id': 0, 'municipio_id': 0, 'localidad_id': 0, 'link_sic': 0, 'fecha_mod': 0}  # Agrega los campos que necesitas

        # Realiza la búsqueda en la base de datos y proyecta solo los campos deseados
        resultado = coleccion.find_one({'universidad_nombre': regex}) #, projection=campos_deseados)

        calificacion, estado_universidad, img_encoded = calificacion_general_universidad()
        calificacion1, estado_bullyng, img_encoded1 = bullyng_general_universidad()
        calificacion2, estado_decersion, img_encoded2 = decersion_general_universidad()
        calificacion3, estado_ingreso, img_encoded3 = ingreso_general_universidad()

        num = np.random.uniform(low=1, high=2)
        num = round(num)
                # Verifica si el resultado es None (no se encontró ningún documento)
        if resultado is None:
            return render_template('fail2.html', valor_busqueda=valor_busqueda)
        
        # Renderiza la plantilla de resultados y pasa el resultado como argumento
        return render_template('resultado_busqueda.html', resultado=resultado, calificacion=calificacion, estado_universidad=estado_universidad, img_encoded=img_encoded, num=num,calificacion1=calificacion1, estado_bullyng=estado_bullyng, img_encoded1=img_encoded1,
                               calificacion2=calificacion2, estado_decersion=estado_decersion, img_encoded2=img_encoded2, calificacion3=calificacion3, estado_ingreso=estado_ingreso, img_encoded3=img_encoded3)
        

    # Obtén nombres aleatorios de tu base de datos
    nombres = coleccion.distinct('universidad_nombre')  # Reemplaza 'nombre' con el campo que contiene los nombres

    # Selecciona un nombre aleatorio
    nombre_aleatorio = random.choice(nombres)
    # Renderiza la plantilla de búsqueda si la solicitud es GET
    return render_template('buscar.html', nombre_aleatorio=nombre_aleatorio)

@app.route('/registrarDatos')
def registrar_datos():
    form = CapturaForm()
    #json = Capjson()
    return render_template('registro.html', form=form, json=json)

@app.route('/resultadoRegistro', methods=['GET', 'POST'])
def procesar_datos():
    form = CapturaForm(request.form)

    if (form.validate()):
        # Acciones con los datos (almacenamiento, procesamiento, etc.)
        datos = {
            'universidad_nombre': form.nombre.data,
            'universidad_colonia': form.colonia.data,
            'universidad_calle_numero': form.calle.data,
            'universidad_telefono1': form.telefono.data,
            'pagina_web': form.pagina_web.data,
        }
        # Aquí puedes realizar las acciones que necesites con los datos

        # Almacenar los datos en MongoDB
        mi_coleccion = db['usuarios']  # Nombre de la colección
        mi_coleccion.insert_one(datos)

        return render_template('exito.html', datos=datos)
    else:
        if not form.validate():

            for field, errors in form.errors.items():
                print(f"Errores en el campo {field}: {', '.join(errors)}")
        return render_template('fail.html', form=form)


@app.route('/mostrarDatos')
def mostrar_datos():
    # Recupera los datos de la colección
    datos = coleccion.find()

    # Convierte los datos a una lista para pasarlos al template
    datos_lista = list(datos)

    # Renderiza la plantilla y pasa los datos como argumento
    return render_template('mostrarDatos.html', datos=datos_lista)

#Formulario de evaluacion de proyecto
@app.route('/evaluarowo')
def evaluarowo():
 
    return render_template('EvaluarUni.html')

#CONFIGURACION CRUD
@app.route('/registerex')
def exitoso():

    return render_template('register_exitoso.html')
@app.route('/loguearte')
def loguearte():
    return render_template('login.html')

@app.route('/signup',methods=['GET'])
def registerowo():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html')

@app.route('/signup/register', methods=['POST'])
def registeruwu():
    form = SignupForm(request.form)

    # Crear el objeto de usuario
    user = {
        "_id": uuid.uuid4().hex,
        "name": request.form.get('nombre1'),
        "email": request.form.get('email1'),
        "password": request.form.get('password1')
    }

    # Encriptar la contraseña
    user['password'] = pbkdf2_sha256.hash(user['password'])

    # Verificar si la dirección de correo electrónico ya existe
    existing_user = db['users'].find_one({"email": user['email']})
    if existing_user:
        return render_template('fail.html', form=form)

    # Insertar el nuevo usuario en la base de datos
    db['users'].insert_one(user)

    # Renderizar la plantilla con la información del usuario registrado
    return render_template('register_exitoso.html', user=user)
   
@app.route('/login/owo', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Buscar el usuario en la base de datos por el correo electrónico
        user = db['users'].find_one({"email": email})

        if user and pbkdf2_sha256.verify(password, user['password']):
            # Iniciar sesión del usuario
            session['user'] = {
                '_id': user['_id'],
                'name': user['name'],
                'email': user['email']
            }
            return redirect(url_for('exito'))  # Redirigir al panel de control
       
        else:
            return render_template('fail3.html', message='Login failed. Invalid email or password.')

    return render_template('login.html')

# Ruta para el panel de control
@app.route('/exito')
def exito():
    if 'user' in session:
        print(session['user'])  
        return render_template('dashboard.html', user=session['user'])
    else:
        return redirect(url_for('loguearte'))
    
#Configuración evluacion

@app.route('/enviar_evaluacion', methods=['POST'])
def enviar_evaluacion():
    # Obtén el nombre de la universidad desde el formulario
    nombre_universidad = request.form.get('encuesta')

    # Crear un diccionario para almacenar las respuestas
    respuestas = {
        'nombre_universidad': nombre_universidad,
        'pregunta1': request.form.get('pregunta1'),
        'pregunta2': request.form.get('pregunta2'),
        'pregunta3': request.form.get('pregunta3'),
        'pregunta4': request.form.get('pregunta4'),
        'pregunta5': request.form.get('pregunta5'),
        'pregunta6': request.form.get('pregunta6'),
        'pregunta7': request.form.get('pregunta7'),
        'pregunta8': request.form.get('pregunta8'),
        'pregunta9': request.form.get('pregunta9'),
        'pregunta10': request.form.get('pregunta10'),
        'pregunta11': request.form.get('pregunta11'),
        'pregunta12': request.form.get('pregunta12'),
        'pregunta13': request.form.get('pregunta13'),
        'pregunta14': request.form.get('pregunta14'),
        'pregunta15': request.form.get('pregunta15'),
        'pregunta16': request.form.get('pregunta16'),
        'pregunta17': request.form.get('pregunta17'),
        'pregunta18': request.form.get('pregunta18'),
        'pregunta19': request.form.get('pregunta19'),
        'pregunta20': request.form.get('pregunta20')
    }

    # Guardar las respuestas en la colección 'encuestas'
    UWU = db['encuestas']  # Nombre de la colección
    UWU.insert_one(respuestas)

    # Puedes redirigir a una página de agradecimiento o donde desees
    return render_template('exito.html', nombre_universidad=nombre_universidad, respuestas=respuestas)


@app.route('/mostrarEncuesta')
def mostrar_encuestas():
    # Recupera todos los datos de la colección
    datos = db['encuestas'].find({})

    # Convierte los datos a una lista para pasarlos al template
    datos_lista = list(datos)

    # Renderiza la plantilla y pasa los datos como argumento
    return render_template('mostrarEncuesta.html', datos=datos_lista)

#SCRAPER
@app.route('/scraper', methods=['GET', 'POST'])
def scraper():
    if request.method == 'POST':
        link = request.form['link']
        data = scrape_data(link)
        save_to_mongo(data)
        return redirect(url_for('mostrar_encuestas'))

    return render_template('scraper.html')

def scrape_data(link):
 # Configuración de Selenium
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36')

    driver = webdriver.Chrome(options=options)
    # Cargar la página
    driver.get(link)

    # Esperar a que se cargue el contenido (puedes ajustar el tiempo según sea necesario)
    driver.implicitly_wait(10)

    # Obtener el contenido de la página después de que JavaScript haya cargado
    page_source = driver.page_source
    driver.quit()

    soup = BeautifulSoup(page_source, 'html.parser')

    # Encuentra la información específica que estás buscando
    universidades_publicas = []

    # Ajusta este código según la estructura HTML de la página
    # En este ejemplo, se asume que las universidades están en divs con la clase "universidad-card"
    universidades_divs = soup.find_all('div', class_='universidad-card')

    for universidad_div in universidades_divs:
        nombre = universidad_div.find('h2').text
        direccion = universidad_div.find('p', class_='direccion').text
        telefono = universidad_div.find('p', class_='telefono').text

        universidad_info = {
            'nombre': nombre,
            'direccion': direccion,
            'telefono': telefono
        }

        universidades_publicas.append(universidad_info)

    # Devuelve los datos en un diccionario
    data = {
        'link': link,
        'universidades_publicas': universidades_publicas
        # Puedes agregar más datos según sea necesario
    }
    print(data)
    return data

def save_to_mongo(data):
    # Guarda los datos en MongoDB
    # Ajusta según tu esquema de datos y colección en MongoDB
    collection = db['scraping']
    collection.insert_one(data)