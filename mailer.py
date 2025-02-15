import os
from flask_mail import Message
from extensions import mail  # Usa la instancia de mail de extensions.py
from flask import current_app

def enviar_correo(solicitud):
    with current_app.app_context(): 
        msg = Message(
            "Nueva Solicitud de Cotización",
            sender=current_app.config["MAIL_DEFAULT_SENDER"],  # Asegurar remitente
            recipients=["anthony.gamio.a@uni.pe"]  # Múltiples correos
        )

        detalles = f"""
        Se ha recibido una nueva solicitud de cotización.
        
        **Datos del Cliente**
        - Cliente: {solicitud.cliente}  
        - Razón Social: {solicitud.razon_social}  
        - RUC: {solicitud.ruc}  
        - Correo: {solicitud.correo}  
        - Teléfono: {solicitud.telefono}  

        **Datos de la Carga**
        - Código de Atención: {solicitud.codigo_atencion}
        - Fecha de Creación: {solicitud.fecha_creacion}
        - Incoterm: {solicitud.incoterm}
        - Origen: {solicitud.origen}
        - Destino: {solicitud.destino}
        - Producto: {solicitud.producto}
        - Dimensiones: {solicitud.dimensiones}
        - Peso: {solicitud.peso} kg
        - Valor: ${solicitud.valor:.2f} USD
        """

        # Agregar campos opcionales si existen
        if solicitud.comentarios:
            detalles += f"\nComentarios: {solicitud.comentarios}"

        if solicitud.embalaje:
            detalles += f"\nTipo de Embalaje: {solicitud.embalaje}"

        if solicitud.tipo_carga:
            detalles += f"\nTipo de Carga: {solicitud.tipo_carga}"

        if solicitud.servicios_adicionales:
            detalles += f"\nServicios Adicionales: {solicitud.servicios_adicionales}"

        # 📎 Adjuntar archivo si existe
        if solicitud.archivo:
            filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], solicitud.archivo)
            try:
                with open(filepath, "rb") as f:
                    msg.attach(
                        filename=solicitud.archivo,
                        content_type="application/octet-stream",  # Genérico, podemos mejorarlo
                        data=f.read()
                    )
            except FileNotFoundError:
                print(f"📎 Archivo adjunto: {solicitud.archivo}")  # Depuración
            except FileNotFoundError:
                print(f"⚠ Archivo no encontrado: {filepath}")

        msg.body = detalles  # Agregamos el mensaje al cuerpo del correo
        mail.send(msg)  # Enviar correo
