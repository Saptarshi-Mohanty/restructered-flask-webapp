from flask import render_template, redirect, url_for, request

from forms.search import SearchPage

def search_logic():
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