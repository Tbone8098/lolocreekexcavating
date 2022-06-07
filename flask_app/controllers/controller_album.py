from flask_app import app
from flask_app.config.helpers import cloudinaryUpload
from flask import render_template, redirect, session, request, flash

from flask_app.models import model_album, model_image, model_albums_has_images

@app.route('/album/create', methods=['POST'])          
def album_create():
    if not model_album.Album.validate(request.form):
        return redirect('/admin/gallery')

    model_album.Album.create(**request.form, user_id=session['uuid'])
    return redirect('/admin/gallery')

@app.route('/album/<int:id>/add_photo', methods=['post'])          
def album_add_photo(id):
    album = model_album.Album.get_one(id=id)
    data = {**request.form}
    if not model_image.Image.validate(data, request.files):
        return redirect(f'/album/{id}/edit')

    for key in request.files:
        resp = cloudinaryUpload(request.files[key], f'/{album.name}', data['name'])
        data['url'] = resp['url']
    
    data['user_id'] = session['uuid']
    image_id = model_image.Image.create(**data)
    model_albums_has_images.AlbumsHasImages.create(image_id=image_id, album_id=album.id)

    return redirect(f'/album/{id}/edit')

@app.route('/album/<int:id>/edit')          
def album_edit(id):
    context = {
        'album': model_album.Album.get_one(id=id),
        'all_pictures': model_image.Image.get_all_in_album({'album_id': id})
    }
    return render_template('admin/album_edit.html', **context)

@app.route('/album/<int:id>/update', methods=['POST'])          
def album_update(id):
    return redirect('/')

@app.route('/album/<int:id>/delete')          
def album_delete(id):
    return redirect('/')
