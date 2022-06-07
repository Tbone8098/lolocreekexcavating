from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA
import re

class Album(model_base.base_model):
    table = 'Albums'
    def __init__(self, data):
        super().__init__(data)
        self.name = data['name']

    @staticmethod
    def validate(data):
        is_valid = True

        if len(data['name']) < 1:
            flash('Field is required', 'err_album_name')
            is_valid = False
        
        return is_valid