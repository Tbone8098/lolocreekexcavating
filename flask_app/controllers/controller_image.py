from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models import model_image, model_business_info

@app.route('/images/all')          
def images_all():
    context = {
        'all_photos': model_image.Image.get_all(),
        'business': model_business_info.BusinessInfo.get_all()[0]
    }
    return render_template('onlooker/images_all.html', **context)