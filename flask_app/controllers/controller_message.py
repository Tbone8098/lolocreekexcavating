from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.config.helpers import login_required

from flask_app.models import model_message, model_user
import os

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
    New Message From: {submitter.fullname} \n
    {data['message']} \n
    """

    db_data = {
        'message': data['message'],
        'sender': submitter.email,
        'reciever': data['receiver'],
        'ip': request.form['ip_address'],
        'level': 9,
    }
    model_message.Message.create(**db_data)
    # send_mail(data)
    return redirect('/dashboard')

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

    # TODO: look into hashing the ip address
    # TODO: write a query that counts the ip addresses of the messages sent in the last minute or so
 
    db_data = {
        'message': data['message'],
        'sender': data['email'],
        'receiver': data['receiver'],
        'ip': request.form['ip_address'],
        'level': 5,
    }
    model_message.Message.create(**db_data)
    # send_mail(data)
    flash('Message Sent! Thank you for your interest. We will get back to you as soon as possible!', 'contact_us_message')
    return redirect('/contactus')

# @app.route('/message/new')          
# def message_new():
#     return render_template('message_new.html')

# @app.route('/message/create', methods=['POST'])          
# def message_create():
#     return redirect('/')

# @app.route('/message/<int:id>')          
# def message_show(id):
#     return render_template('message_show.html')

# @app.route('/message/<int:id>/edit')          
# def message_edit(id):
#     return render_template('message_edit.html')

@app.route('/admin/message/<int:id>/update', methods=['POST'])    
@login_required      
def message_update(id):
    model_message.Message.update_one(id=id, **request.form)
    return redirect('/dashboard')

@app.route('/admin/message/<int:id>/delete')       
@login_required   
def message_delete(id):
    return redirect('/')
