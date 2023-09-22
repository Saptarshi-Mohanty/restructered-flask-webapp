from flask import Flask
from dotenv import load_dotenv

from backend.core.config import CONFIG

load_dotenv()
app = Flask(__name__, static_folder=r"C:\Users\SaptarshiMohanty\Flask-webapp\source", template_folder=r"C:\Users\SaptarshiMohanty\Flask-webapp\frontend\templates")
app.config['SECRET_KEY'] = CONFIG

from backend.core.routes import *

if __name__ == '__main__':
    app.run(debug=True)
