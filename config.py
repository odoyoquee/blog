import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://grace:gee@localhost/blog'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
  

class ProdConfig(Config):
    SQLALCHEMY_DATABASE = os.environ.get("DATABASE_URL")
    pass 

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://grace:gee@localhost/blog' 
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}