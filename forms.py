from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Optional

class SolicitudForm(FlaskForm):
    incoterm = SelectField("Incoterm", choices=[("EXW", "EXW"), ("FOB", "FOB"), ("CIF", "CIF"), ("DAP", "DAP"), ("DDP", "DDP")], validators=[DataRequired()])
    origen = StringField("Origen", validators=[DataRequired()])
    destino = StringField("Destino", validators=[DataRequired()])
    producto = StringField("Producto", validators=[DataRequired()])
    dimensiones = StringField("Dimensiones (LxAxH cm)", validators=[DataRequired()])
    peso = FloatField("Peso (kg)", validators=[DataRequired()])
    
    embalaje = StringField("Tipo de Embalaje", validators=[Optional()])
    tipo_carga = StringField("Tipo de Carga", validators=[Optional()])
    servicios_adicionales = StringField("Servicios Adicionales", validators=[Optional()])
    comentarios = TextAreaField("Comentarios", validators=[Optional()])
    
    submit = SubmitField("Enviar Solicitud")