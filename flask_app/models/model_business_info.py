from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA
import re

class BusinessInfo(model_base.base_model):
    table = 'Business_info'
    def __init__(self, data):
        super().__init__(data)
        self.address = data['address']
        self.phone_number = data['phone_number']
        self.email = data['email']
        self.about_us = data['about_us']
        self.about_us_img = data['about_us_img']
        self.company_name = data['company_name']
        self.company_logo = data['company_logo']
        self.front_page_img = data['front_page_img']