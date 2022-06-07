from cmath import log, pi
from flask_app import app
from flask import render_template, redirect, session, request, jsonify
from flask_app.models import model_business_info
from flask_app.config.helpers import cloudinaryUpload


@app.route('/admin/business_info')          
def business_info_new():
    business_info = model_business_info.BusinessInfo.get_all()
    context = {
        'business': business_info[0]
    }
    return render_template('admin/business_info.html', **context)

@app.route('/api/business_info/<int:id>/update', methods=['post'])
def api_business_update(id):
    print("testing")
    data = {**request.form}
    for item in data:
        if data[item] == 'undefined':
            return jsonify({
                'msg': 'failed' 
            })
    response = {
        'msg': 'success'
    }
    if request.files:
        for file in request.files:
            resp = cloudinaryUpload(request.files[file], '/business_info', file)
            data[file] = resp['url']
            response['img'] = resp['url']

    model_business_info.BusinessInfo.update_one(id=id, **data)
    return jsonify(response)

@app.route('/business_info/update', methods=['POST'])          
def business_info_update():
    data = {**request.form}
    if request.files:
        pictures = []
        for file in request.files:
            file_actual = request.files[file]
            file_actual.save('file')
            if file_actual.content_type != 'application/octet-stream':
                pictures.append({
                    'file': file_actual,
                    'name': file
                })
        
        print(pictures)
        if len(pictures):
            for item in pictures:
                print(item)
                resp = cloudinaryUpload(item['file'], '/business_info', item['name'])
                data[file] = resp['url']
        # for file in request.files:
            # file_actual = request.files[file]
            # file_actual.save('file')
            # print(file_actual.content_type)
            # if file_actual.content_type != 'application/octet-stream':
            #     print("&&&&&&&&&&&&&")
            #     print(file_actual)
            #     resp = cloudinaryUpload(request.files[file], '/business_info', file)
            #     data[file] = resp['url']

    model_business_info.BusinessInfo.update_one(**data)
    return redirect('/admin/business_info')

