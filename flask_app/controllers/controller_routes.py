from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_business_info

@app.route('/')
def index():
    context = {
        'business': model_business_info.BusinessInfo.get_all()[0]
    }
    return render_template('onlooker/index.html', **context)

@app.route('/dashboard')
def dashboard():
    context = {
            'business': model_business_info.BusinessInfo.get_all()[0]
    }
    return render_template('admin/dashboard.html', **context)

@app.route('/aboutus')
def aboutus():
    context = {
            'business': model_business_info.BusinessInfo.get_all()[0]
    }
    return render_template('/onlooker/aboutus.html', **context)

@app.route('/services')
def services():
    context = {
            'business': model_business_info.BusinessInfo.get_all()[0]
    }
    return render_template('/onlooker/services.html', **context)

@app.route('/contactus')
def contactus():
    context = {
            'business': model_business_info.BusinessInfo.get_all()[0]
    }
    return render_template('/onlooker/contactus.html', **context)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'page not found'