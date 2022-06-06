from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import model_business_info
from flask_app.config.helpers import cloudinaryUpload


@app.route('/admin/business_info')          
def business_info_new():
    business_info = model_business_info.BusinessInfo.get_all()
    if not business_info:
        model_business_info.BusinessInfo.create()
        return redirect('/business_info')

    context = {
        'business': business_info[0]
    }
    return render_template('admin/business_info.html', **context)

@app.route('/business_info/update', methods=['POST'])          
def business_info_update():
    print(request.files)
    data = {**request.form}
    if request.files:
        resp = cloudinaryUpload(request.files['about_us_img'], '/business_info', 'about_us')
        data['about_us_img'] = resp['url']

    model_business_info.BusinessInfo.update_one(**data)
    return redirect('/business_info')

