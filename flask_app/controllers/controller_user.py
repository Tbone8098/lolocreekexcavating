from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.config.helpers import login_required
from flask_app.models import model_user, model_business_info

@app.route('/login')
def login():
    context = {
        'business': model_business_info.BusinessInfo.get_all()[0]
    }
    return render_template('/admin/login.html', **context)

@app.route('/login/process', methods=['POST'])
def process_login():
    if not model_user.User.validation_login(request.form):
        return redirect('/login')
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    del session['uuid']
    return redirect('/')

@app.route('/register')
def register():
    context = {
        'business': model_business_info.BusinessInfo.get_all()[0]
    }
    return render_template('/admin/register.html', **context)

@app.route('/user/create', methods=['post'])
def create_user():
    if not model_user.User.validation(request.form):
        return redirect('/register')
    hash = bcrypt.generate_password_hash(request.form['pw'])
    data = {
        **request.form,
        'pw' : hash,
        'level': 5
    }
    del data['confirm_pw']

    id = model_user.User.create(**data)
    session['uuid'] = id
    return redirect('/dashboard')

@app.route('/user/<int:id>')
def show_user(id):
    pass 

@app.route('/admin/user/<int:id>/edit')
@login_required
def edit_user(id):
    context = {
        'user': model_user.User.get_one(id=id)
    }
    return render_template('admin/user_edit.html', **context)

@app.route('/admin/user/<int:id>/update', methods=['post'])
@login_required
def update_user(id):
    if not model_user.User.validate_is_empty(request.form):
        return redirect(f'/user/{id}/edit')
    
    if 'pw' in request.form:
        user = model_user.User.get_one(id=id)
        if not bcrypt.check_password_hash(user.pw, request.form['old_pw']):
            flash("Bad Old Password", 'err_user_old_pw')
        else:
            if request.form['pw'] != request.form['confirm_pw']:
                flash("Passwords don't match", 'err_user_confirm_pw')

    model_user.User.update_one(id=id, **request.form)
    return redirect(f'/user/{id}/edit')

@app.route('/user/<int:id>/delete')
def delete_user(id):
    model_user.User.delete_one(id=id)
    pass 
