from flask import render_template, flash, redirect, url_for

from forms.login import LoginForm
from helper.util import pipeline

def login_logic():
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
