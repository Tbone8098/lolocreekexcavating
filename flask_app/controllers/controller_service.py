from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models import model_service

@app.route('/admin/services')          
def admin_services():
    context = {
        'all_services': model_service.Service.get_all()
    }
    return render_template('admin/services.html', **context)

@app.route('/admin/service/create', methods=['POST'])          
def service_create():
    if not model_service.Service.validate(request.form):
        return redirect('/admin/services')
    data = {**request.form}
    if 'files' in data:
        del data['files']
    
    model_service.Service.create(**data)
    return redirect('/admin/services')

@app.route('/service/<int:id>')          
def service_show(id):
    return render_template('service_show.html')

@app.route('/admin/service/<int:id>/edit')          
def service_edit(id):
    context = {
        'service': model_service.Service.get_one(id=id)
    }
    return render_template('admin/service_edit.html', **context)

@app.route('/admin/service/<int:id>/update', methods=['POST'])          
def service_update(id):
    if not model_service.Service.validate(request.form):
        return redirect(f'/admin/service/{id}/edit')
    
    data = {**request.form}
    del data['files']
    model_service.Service.update_one(id=id, **data)
    return redirect('/admin/services')

@app.route('/admin/service/<int:id>/delete')          
def service_delete(id):
    model_service.Service.delete_one(id=id)
    return redirect('/admin/services')
