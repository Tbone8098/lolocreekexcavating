from flask_app import cloudinary
import os
import cloudinary.uploader
import cloudinary.api

def cloudinaryUpload(img, folder, public_id):
    cloudinary.config( 
        cloud_name = os.environ.get('CLOUD_NAME'), 
        api_key = os.environ.get('CLOUD_API_KEY'), 
        api_secret = os.environ.get('CLOUD_API_SECRET') 
        )

    image = img
    resp = cloudinary.uploader.upload(
        image, 
        folder = folder, 
        public_id = public_id,
        overwrite = True, 
        )
    return resp
    