from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, TextAreaField, SubmitField, EmailField, DecimalField
from wtforms.validators import DataRequired, Optional, Length, Email
from flask_wtf.file import FileField, FileAllowed

class SolicitudForm(FlaskForm):

    cliente = StringField("Cliente", validators=[DataRequired(), Length(min=2, max=100)])
    razon_social = StringField("Razón Social", validators=[DataRequired(), Length(min=2, max=200)])
    ruc = StringField("RUC", validators=[DataRequired(), Length(min=11, max=11)])
    correo = EmailField("Correo Electrónico", validators=[DataRequired(), Email()])
    telefono = StringField("Teléfono", validators=[DataRequired(), Length(min=6, max=15)])

    incoterm = SelectField("Incoterm", choices=[("EXW", "EXW"), ("FOB", "FOB"), ("CIF", "CIF"), ("DAP", "DAP"), ("DDP", "DDP")], validators=[DataRequired()])
    origen = StringField("Origen", validators=[DataRequired()])
    destino = StringField("Destino", validators=[DataRequired()])
    producto = StringField("Producto", validators=[DataRequired()])
    dimensiones = StringField("Dimensiones (LxAxH cm)", validators=[DataRequired()])
    peso = FloatField("Peso (kg)", validators=[DataRequired()])
    valor = DecimalField("Valor (USD)", validators=[DataRequired()]) 
    
    embalaje = StringField("Tipo de Embalaje", validators=[Optional()])
    tipo_carga = StringField("Tipo de Carga", validators=[Optional()])
    servicios_adicionales = StringField("Servicios Adicionales", validators=[Optional()])
    comentarios = TextAreaField("Comentarios", validators=[Optional()])

    archivo = FileField("Adjuntar archivo", validators=[FileAllowed(["jpg", "png", "pdf", "docx"], "Solo se permiten archivos JPG, PNG, PDF y DOCX")])
    
    submit = SubmitField("Enviar Solicitud")