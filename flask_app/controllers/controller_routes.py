from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
# from flask_app.models import model_user

@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/dashboard')
    session['page'] = 'landing_page'
    return render_template('onlooker/index.html')


@app.route('/aboutus')
def aboutus():
    return render_template('/onlooker/aboutus.html')

@app.route('/services')
def services():
    return render_template('/onlooker/services.html')

@app.route('/contactus')
def contactus():
    return render_template('/onlooker/contactus.html')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'page not found'