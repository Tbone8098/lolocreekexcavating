from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_business_info, model_service, model_album
from flask_app.config.helpers import send_mail

@app.route('/')
def index():
    business_info = model_business_info.BusinessInfo.get_all()
    if not business_info:
        model_business_info.BusinessInfo.create()
        return redirect('/')
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
def about_us():
    context = {
            'business': model_business_info.BusinessInfo.get_all()[0]
    }
    return render_template('/onlooker/aboutus.html', **context)

@app.route('/services')
def services():
    context = {
            'business': model_business_info.BusinessInfo.get_all()[0],
            'all_services': model_service.Service.get_all()
    }
    return render_template('/onlooker/services.html', **context)

@app.route('/gallery')
def gallery():
    context = {
            'business': model_business_info.BusinessInfo.get_all()[0],
            'all_albums': model_album.Album.get_all()
    }
    return render_template('/onlooker/gallery.html', **context)

@app.route('/contactus')
def contactus():
    context = {
            'business': model_business_info.BusinessInfo.get_all()[0]
    }
    return render_template('/onlooker/contactus.html', **context)

@app.route('/admin/gallery')
def admin_gallery():
    context = {
        'all_albums': model_album.Album.get_all()
    }
    return render_template('/admin/gallery.html', **context)

@app.route('/send_email')
def send_email():
    send_mail()
    return redirect('/')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'page not found'