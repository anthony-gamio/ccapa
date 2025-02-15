from extensions import db
from flask import current_app
from datetime import datetime

class Solicitud(db.Model):
    __tablename__ = "logistica_solicitudes"
    
    id = db.Column(db.Integer, primary_key=True)
    codigo_atencion = db.Column(db.String(20), unique=True, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    
    cliente = db.Column(db.String(100), nullable=False)
    razon_social = db.Column(db.String(200), nullable=False)
    ruc = db.Column(db.String(11), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(15), nullable=False)

    # Datos principales
    incoterm = db.Column(db.String(10), nullable=False)
    origen = db.Column(db.String(100), nullable=False)
    destino = db.Column(db.String(100), nullable=False)
    producto = db.Column(db.String(200), nullable=False)
    dimensiones = db.Column(db.String(100), nullable=False)  # "LxAxH cm"
    peso = db.Column(db.Float, nullable=False)  # Kg
    valor = db.Column(db.Float, nullable=False)

    # Datos opcionales
    embalaje = db.Column(db.String(50), nullable=True)
    tipo_carga = db.Column(db.String(50), nullable=True)
    servicios_adicionales = db.Column(db.String(200), nullable=True)
    comentarios = db.Column(db.Text, nullable=True)

    archivo = db.Column(db.String(255), nullable=True) 

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.codigo_atencion = self.generar_codigo()

    def generar_codigo(self):
        fecha = datetime.utcnow().strftime("%Y%m%d")
        ultimo = Solicitud.query.filter(Solicitud.codigo_atencion.like(f"ATN-{fecha}-%")).count() + 1
        return f"ATN-{fecha}-{ultimo:03d}"