from flask import render_template, flash, redirect, url_for, request

from forms.registration import RegistrationForm
from forms.login import LoginForm
from forms.search import SearchPage
from helper.util import pipeline
from app import app

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route("/login", methods=['GET', 'POST'])
def login():
    from core.hash import hash_checking
    form = LoginForm()
    if form.validate_on_submit():
        result = pipeline.check_user(form.email.data)
        for doc in result:
            if hash_checking(password=form.password.data, hash=doc["password"]):
                return redirect(url_for('search'))
            else:
                flash(f'Email or Password does not match')
    return render_template('login.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    from core.hash import password_hashing
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = password_hashing(form.password.data)
        pipeline.insert_user(fname=form.first_name.data, lname=form.last_name.data, email=form.email.data, empid=form.empid.data, title=form.title.data, password=hashed_password)
        flash(f'Account created for {form.first_name.data}')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/search", methods=['GET', 'POST'])
def search():
    form = SearchPage()
    name = form.first_name.data
    value = None
    if form.dropdown.data:
        value = form.dropdown.data
    if request.method == 'POST' and value :
        return redirect(url_for("result", name=name, value=value))
    elif request.method == 'POST':
        return redirect(url_for("result", name=name))
    else:
        return render_template('search.html', form = form)

@app.route("/result/<name>/<value>", methods = ['POST', 'GET'])
def result(name, value):
    if name != "all" and value == 'sbn':
        r = pipeline.sort_name(name=name)
        return render_template('result.html', r = r)
    elif name != "all" and value == 'sbr':
        r = pipeline.sort_rating(name=name)
        return render_template('result.html', r = r)
    elif name != "all" and value == 'None':
        r = pipeline.get_first_name(name=name)
        return render_template('result.html', r = r)
    elif name == "all" and value =="sbn":
        r = pipeline.sort_name_all()
        return render_template('result.html', r = r)
    elif name == "all" and value =="sbr":
        r = pipeline.sort_rating_all()
        return render_template('result.html', r = r)
    elif name == 'all' and value == 'None':
        r = pipeline.get_all()
        return render_template('result.html', r = r)