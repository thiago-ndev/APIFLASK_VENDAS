import os

class Config:
    DEBUG = os.getenv('DEBUG', False)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
