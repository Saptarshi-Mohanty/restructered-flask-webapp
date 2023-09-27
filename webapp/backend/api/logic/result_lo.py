from flask import render_template

from helper.util import pipeline

def result_logic(name, value):
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