from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models import model_album

@app.route('/album/create', methods=['POST'])          
def album_create():
    if not model_album.Album.validate(request.form):
        return redirect('/admin/gallery')

    model_album.Album.create(**request.form, user_id=session['uuid'])
    return redirect('/admin/gallery')

@app.route('/album/<int:id>')          
def album_show(id):
    return render_template('album_show.html')

@app.route('/album/<int:id>/edit')          
def album_edit(id):
    return render_template('album_edit.html')

@app.route('/album/<int:id>/update', methods=['POST'])          
def album_update(id):
    return redirect('/')

@app.route('/album/<int:id>/delete')          
def album_delete(id):
    return redirect('/')
