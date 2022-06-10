from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_albums_has_images
from flask_app import DATABASE_SCHEMA

class Image(model_base.base_model):
    table = 'Images'
    def __init__(self, data):
        super().__init__(data)
        self.url = data['url']
        self.name = data['name']
        self.description = data['description']
        self.user_id = data['user_id']

    @classmethod
    def get_all_in_album(cls, data:dict):
        """
        dictionary needs a key of "album_id"
        """
        query = """
        SELECT * FROM images
        JOIN albums_has_images ON albums_has_images.image_id = images.id
        WHERE albums_has_images.album_id = %(album_id)s;
        """
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        if results:
            all_images = []
            for dict in results:
                all_images.append(cls(dict))
            return all_images
        return []

    @staticmethod
    def validate(data, files):
        is_valid = True

        if len(data['name']) < 1:
            is_valid = False
            flash('Field is Required', 'err_image_name')

        for key in files:
            if files[key].content_type == 'application/octet-stream' and len(data['url']) < 1:
                is_valid = False
                flash('Image is required', 'err_image')
            
        return is_valid