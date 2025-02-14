from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, Solicitud
from forms import SolicitudForm
from mailer import enviar_correo

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/", methods=["GET", "POST"])
def formulario():
    form = SolicitudForm()
    if form.validate_on_submit():
        solicitud = Solicitud(**form.data)
        db.session.add(solicitud)
        db.session.commit()
        enviar_correo(solicitud)
        return render_template("confirmacion.html", codigo=solicitud.codigo_atencion)
    return render_template("formulario.html", form=form)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Crea la BD si no existe
    app.run(debug=True)