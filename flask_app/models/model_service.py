from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA
import re

class Service(model_base.base_model):
    table = 'services'
    def __init__(self, data):
        super().__init__(data)
        self.name = data['name']
        self.description = data['description']

    @staticmethod
    def validate(data):
        is_valid = True

        if len(data['name']) < 1:
            is_valid = False
            flash('Field is required', 'err_service_name')

        if len(data['description']) < 1:
            is_valid = False
            flash('Field is required', 'err_service_description')
        
        return is_valid