from flask_mail import Mail, Message
from config import Config

mail = Mail()

def enviar_correo(solicitud):
    mail.init_app(app)
    msg = Message("Nueva Solicitud de Cotización", recipients=["admin@empresa.com"])
    msg.body = f"Se ha recibido una nueva solicitud de cotización con el código: {solicitud.codigo_atencion}"
    mail.send(msg)