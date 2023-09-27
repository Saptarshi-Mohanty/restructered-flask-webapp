from flask import render_template

from api.logic.login_lo import login_logic
from api.logic.registration_lo import registration_logic
from api.logic.search_lo import search_logic
from api.logic.result_lo import result_logic
from app import app

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route("/login", methods=['GET', 'POST'])
def login():
    return login_logic()

@app.route("/register", methods=['GET', 'POST'])
def register():
    return registration_logic()

@app.route("/search", methods=['GET', 'POST'])
def search():
    return search_logic()

@app.route("/result/<name>/<value>", methods = ['POST', 'GET'])
def result(name, value):
    return result_logic(name=name, value=value)