from flask_mail import Message
from extensions import mail  # ✅ Usamos la instancia de mail de extensions.py
from flask import current_app

def enviar_correo(solicitud):
    with current_app.app_context(): 
        msg = Message(
            "Nueva Solicitud de Cotización",
            sender=current_app.config["MAIL_DEFAULT_SENDER"],  # ✅ Asegurar remitente
            recipients=["anthony.gamio.a@uni.pe", "pccanto@ccapaeirl.com"]  # Cambia esto si necesitas múltiples correos
        )

        detalles = f"""
        Se ha recibido una nueva solicitud de cotización.
        
        Código de Atención: {solicitud.codigo_atencion}
        Fecha de Creación: {solicitud.fecha_creacion}
        Incoterm: {solicitud.incoterm}
        Origen: {solicitud.origen}
        Destino: {solicitud.destino}
        Producto: {solicitud.producto}
        Dimensiones: {solicitud.dimensiones}
        Peso: {solicitud.peso} kg
        """

        # ✅ Agregar campos opcionales si no están vacíos
        if hasattr(solicitud, "comentarios") and solicitud.comentarios:
            detalles += f"\nComentarios: {solicitud.comentarios}"

        if hasattr(solicitud, "tipo_embalaje") and solicitud.tipo_embalaje:
            detalles += f"\nTipo de Embalaje: {solicitud.tipo_embalaje}"

        if hasattr(solicitud, "seguro") and solicitud.seguro:
            detalles += f"\nSeguro: {solicitud.seguro}"

        if hasattr(solicitud, "prioridad") and solicitud.prioridad:
            detalles += f"\nPrioridad: {solicitud.prioridad}"

        msg.body = detalles  # ✅ Agregamos el mensaje al cuerpo del correo

        mail.send(msg)  # ✅ Ahora usa la instancia configurada en extensions.py
