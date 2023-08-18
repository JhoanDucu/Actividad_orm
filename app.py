from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
user = 'root'
password = 'sena'
url = 'localhost'
bd_name = 'flask_sqlalchemy'
full_url = f'mysql://{user}:{password}@{url}/{bd_name}'

app.config['SQLALCHEMY_DATABASE_URI'] = full_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate()
migrate.init_app(app,db)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    correo = db.Column(db.String(250))
    
    def __init__(self, id, nombre, apellido, correo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
    
    def json(self):
        return {'id': self.id, 'nombre': self.nombre, 'apellido': self.apellido, 'correo': self.correo}
    
    def __str__(self):
        return str(self.__class__)+':'+str(self.__dict__)