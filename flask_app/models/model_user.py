from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User(model_base.base_model):
    table = 'Users'
    def __init__(self, data):
        super().__init__(data)
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']

    @staticmethod
    def validation(data:dict) -> bool:
        is_valid = True

        if len(data['first_name']) < 1:
            is_valid = False
            flash('Required Field', 'err_user_first_name_reg')

        if len(data['last_name']) < 1:
            is_valid = False
            flash('Required Field', 'err_user_last_name_reg')

        if len(data['email']) < 1:
            is_valid = False
            flash('Required Field', 'err_user_email_reg')
        elif not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('Invalid Email', 'err_user_email_reg')
        else:
            potential_user = User.get_one(email=data['email'])
            if potential_user:
                is_valid = False
                flash('Email already exists', 'err_user_email_reg')

        if len(data['pw']) < 1:
            is_valid = False
            flash('Required Field', 'err_user_pw_reg')

        if len(data['confirm_pw']) < 1:
            is_valid = False
            flash('Required Field', 'err_user_confirm_pw_reg')
        elif data['confirm_pw'] != data['pw']:
            is_valid = False
            flash('Passwords must match', 'err_user_confirm_pw_reg')
        
        return is_valid


    @staticmethod
    def validation_login(data:dict) -> bool:
        is_valid = True

        if len(data['email']) < 1:
            is_valid = False
            flash('Required Field', 'err_user_email_login')
        elif not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('Invalid Email', 'err_user_email_login')
        else:
            potential_user = User.get_one(email=data['email'])
            if not potential_user:
                is_valid = False
                flash('Unknown Email', 'err_user_email_login')
            else:
                session['uuid'] = potential_user.id

        if len(data['pw']) < 1:
            is_valid = False
            flash('Required Field', 'err_user_pw_login')

        return is_valid

