from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_contact_info

@app.route('/contact_info')
def new_contact_info():
    return render_template('/admin/contact_info.html')

@app.route('/contact_info/create', methods=['post'])
def create_contact_info():

    if not model_contact_info.Contact_info.validation(request.form):
        return redirect('/')

    data = {
        **request.form
    }

    id = model_contact_info.Contact_info.create(**data)

    pass 

@app.route('/contact_info/<int:id>')
def show_contact_info(id):
    pass 

@app.route('/contact_info/<int:id>/edit')
def edit_contact_info(id):
    pass 

@app.route('/contact_info/<int:id>/update', methods=['post'])
def update_contact_info(id):

    if not model_contact_info.Contact_info.validation(request.form):
        return redirect('/')

    data = {
        **request.form
    }

    model_contact_info.Contact_info.update_one(id=id, **data)

    pass 

@app.route('/contact_info/<int:id>/delete')
def delete_contact_info(id):
    model_contact_info.Contact_info.delete_one(id=id)
    pass 