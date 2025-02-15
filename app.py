import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request
from config import Config
from models import Solicitud
from forms import SolicitudForm
from mailer import enviar_correo
from extensions import db, mail

app = Flask(__name__)
app.config.from_object(Config)

# Configurar carpeta de subida
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Crear la carpeta si no existe

db.init_app(app)
mail.init_app(app)

@app.route("/", methods=["GET", "POST"])
def formulario():
    form = SolicitudForm()
    if form.validate_on_submit():
        file = request.files.get("archivo")  # Obtiene el archivo de manera segura
        filename = None  # Evita errores si no se sube archivo

        if file and file.filename:  # Verifica si hay archivo adjunto
            filename = secure_filename(file.filename)  # Sanitiza el nombre
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)  # Guarda el archivo en la carpeta de subida
            print(f" Archivo guardado en: {filepath}")  # Depuración

        from mailer import enviar_correo
        data = {key: value for key, value in form.data.items() if key not in ["submit", "csrf_token"]}
        data["archivo"] = filename  # Guarda solo el nombre en la BD

        with app.app_context():
            solicitud = Solicitud(**data)
            db.session.add(solicitud)
            db.session.commit()
            enviar_correo(solicitud)
        
        return render_template("confirmacion.html", codigo=solicitud.codigo_atencion)

    return render_template("formulario.html", form=form)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Crea la BD si no existe
    app.run(debug=True)
