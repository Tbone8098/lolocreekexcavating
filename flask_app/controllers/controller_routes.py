from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_business_info, model_service, model_album, model_user
from flask_app.config.helpers import login_required, send_mail

import os

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
@login_required
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
@login_required
def admin_gallery():
    context = {
        'all_albums': model_album.Album.get_all()
    }
    return render_template('/admin/gallery.html', **context)

@app.route('/send_email', methods=['post'])
def send_email():
    data = {**request.form}
    data['sender'] = os.environ.get('EMAIL_ADDRESS')
    data['receiver'] = os.environ.get('EMAIL_ADDRESS')
    data['pw'] = os.environ.get('EMAIL_PASSWORD')

    data['message'] = f"""
    Message from your friendly neigborhood WebworkX, \n
    New Message From: {data['name']} | Email: {data['email']} \n
    {data['message']} \n
    Sincerely, \n
    WebworkX
    """

    send_mail(data)
    flash('Message Sent! Thank you for your interest. We will get back to you as soon as possible!', 'contact_us_message')
    return redirect('/contactus')

@app.route('/admin/contact_the_dev')
@login_required
def contact_the_dev():
    context = {
        'all_users': model_user.User.get_all()
    }
    return render_template('/admin/contact_the_dev.html', **context)

@app.route('/admin/contact_the_dev/process', methods=['post'])
@login_required
def contact_the_dev_process():
    data = {**request.form}
    data['sender'] = os.environ.get('EMAIL_ADDRESS')
    data['receiver'] = os.environ.get('DEV_EMAIL_ADDRESS')
    data['pw'] = os.environ.get('EMAIL_PASSWORD')

    submitter = model_user.User.get_one(id = session['uuid'])

    data['message'] = f"""
    Bug Report, \n
    New Message From: {submitter.name} \n
    {data['message']} \n
    """
    send_mail(data)
    return redirect('/dashboard')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'page not found'