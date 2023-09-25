import os

from app import app

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
MONGO_URI = os.environ.get('MONGO_URI')