import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "supersecretkey"
    
    # Configuración de PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "postgresql://usuario:password@localhost/nombre_bd"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración de correo
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")  # Tu correo
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")  # Tu contraseña de aplicación
    MAIL_DEFAULT_SENDER = MAIL_USERNAME