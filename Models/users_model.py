from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    correo = db.Column(db.String(30), nullable=False)
    contraseña = db.Column(db.String(30), nullable=False)
    usuario = db.Column(db.String(30))
    nombre = db.Column(db.String(30))
    apellido = db.Column(db.String(30))
    telefono = db.Column(db.Integer, nullable=False)
    imagen_perfil = db.Column(db.String(300))

class UsuariosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuarios

usuario_schema = UsuariosSchema()
usuarios_schema = UsuariosSchema(many=True)

