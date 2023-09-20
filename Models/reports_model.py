from Models.users_model import db, ma

class Reportes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    barrio = db.Column(db.String(300))
    estrato = db.Column(db.Integer)
    municipio = db.Column(db.String(200))
    coordenadas = db.Column(db.String(200))
    modalidad_delito = db.Column(db.String(300))
    tipo_arma = db.Column(db.String(300))
    fecha = db.Column(db.Date)
    hora = db.Column(db.Time)
    direccion = db.Column(db.String(255))
    afectados = db.Column(db.Integer)
    genero_victima = db.Column(db.String(20))
    tipo_zona = db.Column(db.String(30))
    archivo_evidencia = db.Column(db.String(255))
    descripcion = db.Column(db.Text)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))  # Usar 'usuarios.id' en lugar de 'Usuarios.id'
    usuario_rel = db.relationship('Usuarios', backref='reportes')

class ReportesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reportes

reporte_schema = ReportesSchema()
reportes_schema = ReportesSchema(many=True)

