from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA
import re

class AlbumsHasImages(model_base.base_model):
    table = 'albums_has_images'
    def __init__(self, data):
        super().__init__(data)
        self.image_id = data['image_id']
        self.album_id = data['album_id']

