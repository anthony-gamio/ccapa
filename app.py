from flask import Flask, render_template, request
from config import Config
from models import Solicitud
from forms import SolicitudForm
from mailer import enviar_correo
from extensions import db, mail

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
mail.init_app(app)

@app.route("/", methods=["GET", "POST"])
def formulario():
    form = SolicitudForm()
    if form.validate_on_submit():
        from mailer import enviar_correo
        data = {key: value for key, value in form.data.items() if key not in ["submit", "csrf_token"]}
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