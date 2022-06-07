from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models import model_images

@app.route('/images/new')          
def images_new():
    return render_template('images_new.html')

@app.route('/images/create', methods=['POST'])          
def images_create():
    return redirect('/')

@app.route('/images/<int:id>')          
def images_show(id):
    return render_template('images_show.html')

@app.route('/images/<int:id>/edit')          
def images_edit(id):
    return render_template('images_edit.html')

@app.route('/images/<int:id>/update', methods=['POST'])          
def images_update(id):
    return redirect('/')

@app.route('/images/<int:id>/delete')          
def images_delete(id):
    return redirect('/')
