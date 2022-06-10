from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_business_info, model_service, model_album, model_user, model_message
from flask_app.config.helpers import login_required, send_mail



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
    user = model_user.User.get_one(id=session['uuid'])
    context = {
            'business': model_business_info.BusinessInfo.get_all()[0],
            'all_messages': model_message.Message.get_all(is_where=True, is_completed=0, level=user.level),
            'user': model_user.User.get_one(id=session['uuid'])
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




@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'page not found'