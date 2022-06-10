from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.config.helpers import login_required

from flask_app.models import model_image, model_business_info, model_albums_has_images

@app.route('/images/all')          
def images_all():
    context = {
        'all_photos': model_image.Image.get_all(),
        'business': model_business_info.BusinessInfo.get_all()[0]
    }
    return render_template('onlooker/images_all.html', **context)

@app.route('/admin/image/<int:id>/edit')          
@login_required
def images_edit(id):
    context = {
        'image': model_image.Image.get_one(id=id),
        'join': model_albums_has_images.AlbumsHasImages.get_one(image_id=id)
    }
    return render_template('admin/image_edit.html', **context)

@app.route('/admin/image/<int:id>/update', methods=['POST'])          
@login_required
def image_update(id):
    join = model_albums_has_images.AlbumsHasImages.get_one(image_id=id)
    model_image.Image.update_one(**request.form, id=id)
    return redirect(f'/admin/album/{join.album_id}/edit')

@app.route('/admin/image/<int:id>/delete')          
@login_required
def images_delete(id):
    album = model_albums_has_images.AlbumsHasImages.get_one(image_id=id)
    model_image.Image.delete_one(id=id)
    return redirect(f'/admin/album/{album.album_id}/edit')