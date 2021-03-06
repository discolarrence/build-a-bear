"""
Routes and views for the flask application.
"""

import json
from flask import render_template, redirect, url_for, request, make_response, flash
from build_a_bear import app
from build_a_bear.options import DEFAULTS


def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data

 
@app.route('/')
def index():
    return render_template('index.html', saves=get_saved_data())


@app.route('/builder')
def builder():
    return render_template('builder.html', saves=get_saved_data(), options=DEFAULTS)


@app.route('/save', methods=['POST'])
def save():
    flash("That looks awesome!")
    response = make_response(redirect(url_for('builder')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('character', json.dumps(data))
    return response