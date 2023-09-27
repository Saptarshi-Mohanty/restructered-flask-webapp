from flask import render_template, redirect, url_for, flash

from forms.registration import RegistrationForm
from helper.util import pipeline

def registration_logic():
    from core.hash import password_hashing
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = password_hashing(form.password.data)
        pipeline.insert_user(fname=form.first_name.data, lname=form.last_name.data, email=form.email.data, empid=form.empid.data, title=form.title.data, password=hashed_password)
        flash(f'Account created for {form.first_name.data}')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
