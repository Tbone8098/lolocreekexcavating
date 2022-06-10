from flask_app import cloudinary
import os
import cloudinary.uploader
import cloudinary.api

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from functools import wraps
from flask import request, redirect, url_for, session

def login_required(f):
    @wraps(f)
    def login_required(*args, **kwargs):
        if 'uuid' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return login_required


def cloudinaryUpload(img, folder, public_id):
    cloudinary.config( 
        cloud_name = os.environ.get('CLOUD_NAME'), 
        api_key = os.environ.get('CLOUD_API_KEY'), 
        api_secret = os.environ.get('CLOUD_API_SECRET') 
        )

    resp = cloudinary.uploader.upload(
        file = img, 
        folder = folder, 
        public_id = public_id,
        overwrite = True, 
        )
    return resp
    

def send_mail(data):
    sender = data['sender']
    receiver = data['receiver']
    password = data['pw']
    message = data['message']

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(sender, password)
    print("logged in")

    server.sendmail(sender, receiver, message)
    print("email sent")

