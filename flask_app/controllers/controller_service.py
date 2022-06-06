from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models import model_service

@app.route('/admin/services')          
def admin_services():
    context = {
        'all_services': model_service.Service.get_all()
    }
    return render_template('admin/services.html', **context)

@app.route('/service/create', methods=['POST'])          
def service_create():
    if not model_service.Service.validate(request.form):
        return redirect('/admin/services')
    
    model_service.Service.create(**request.form)
    return redirect('/admin/services')

@app.route('/service/<int:id>')          
def service_show(id):
    return render_template('service_show.html')

@app.route('/service/<int:id>/edit')          
def service_edit(id):
    return render_template('service_edit.html')

@app.route('/service/<int:id>/update', methods=['POST'])          
def service_update(id):
    return redirect('/')

@app.route('/service/<int:id>/delete')          
def service_delete(id):
    model_service.Service.delete_one(id=id)
    return redirect('/admin/services')
