from flask_app import cloudinary
import os
import cloudinary.uploader
import cloudinary.api

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
    sender = os.environ.get('EMAIL_ADDRESS')
    reciver = os.environ.get('EMAIL_ADDRESS')
    password = os.environ.get('EMAIL_PASSWORD')

    message = f"""
    Message from your friendly neigborhood website, \n
    New Message From: {data['name']} | Email: {data['email']} \n
    {data['message']} \n
    \n
    Sincerely, WebworkX
    """

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(sender, password)
    print("logged in")

    server.sendmail(sender, reciver, message)
    print("email sent")

