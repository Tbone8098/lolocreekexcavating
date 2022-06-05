from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_user

@app.route('/login')
def login():
    return render_template('/admin/login.html')

@app.route('/logout')
def logout():
    del session['uuid']
    return redirect('/')

@app.route('/register')
def register():
    return render_template('/admin/register.html')

@app.route('/user/create', methods=['post'])
def create_user():
    if not model_user.User.validation(request.form):
        return redirect('/register')
    hash = bcrypt.generate_password_hash(request.form['pw'])
    data = {
        **request.form,
        'pw' : hash
    }
    del data['confirm_pw']

    id = model_user.User.create(**data)
    session['uuid'] = id
    return redirect('/dashboard')

@app.route('/user/<int:id>')
def show_user(id):
    pass 

@app.route('/user/<int:id>/edit')
def edit_user(id):
    pass 

@app.route('/user/<int:id>/update', methods=['post'])
def update_user(id):

    if not model_user.User.validation(request.form):
        return redirect('/')

    data = {
        **request.form
    }

    model_user.User.update_one(id=id, **data)

    pass 

@app.route('/user/<int:id>/delete')
def delete_user(id):
    model_user.User.delete_one(id=id)
    pass 
