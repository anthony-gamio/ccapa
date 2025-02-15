import os
from flask_mail import Message
from extensions import mail  # ✅ Usamos la instancia de mail de extensions.py
from flask import current_app

def enviar_correo(solicitud):
    with current_app.app_context(): 
        msg = Message(
            "Nueva Solicitud de Cotización",
            sender=current_app.config["MAIL_DEFAULT_SENDER"],  # ✅ Asegurar remitente
            recipients=["anthony.gamio.a@uni.pe"]  # Cambia esto si necesitas múltiples correos
        )

        detalles = f"""
        Se ha recibido una nueva solicitud de cotización.
        
        Cliente: {solicitud.cliente}  
        Razón Social: {solicitud.razon_social}  
        RUC: {solicitud.ruc}  
        Correo: {solicitud.correo}  
        Teléfono: {solicitud.telefono}  

        Código de Atención: {solicitud.codigo_atencion}
        Fecha de Creación: {solicitud.fecha_creacion}
        Incoterm: {solicitud.incoterm}
        Origen: {solicitud.origen}
        Destino: {solicitud.destino}
        Producto: {solicitud.producto}
        Dimensiones: {solicitud.dimensiones}
        Peso: {solicitud.peso} kg
        Valor: ${solicitud.valor:.2f} USD
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

        if solicitud.archivo:
            filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], solicitud.archivo)
            try:
                with open(filepath, "rb") as f:
                    msg.attach(solicitud.archivo, "application/octet-stream", f.read())
            except FileNotFoundError:
                print(f"⚠ Archivo no encontrado: {filepath}")

        msg.body = detalles  # ✅ Agregamos el mensaje al cuerpo del correo

        mail.send(msg)  # ✅ Ahora usa la instancia configurada en extensions.py
