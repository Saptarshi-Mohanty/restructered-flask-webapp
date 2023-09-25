from flask import Flask
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__, static_folder=r"C:\Users\SaptarshiMohanty\Flask-webapp\webapp\source", template_folder=r"C:\Users\SaptarshiMohanty\Flask-webapp\webapp\frontend\templates")

from core.routes import *
from core.config import *

if __name__ == '__main__':
    app.run(debug=True)
