from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_base, model_user
from flask_app import DATABASE_SCHEMA
import re

class Message(model_base.base_model):
    table = 'Messages'
    def __init__(self, data):
        super().__init__(data)
        self.message = data['message']
        self.sender = data['sender']
        self.receiver = data['receiver']
        self.ip = data['ip']
        self.level = data['level']
        self.in_process = data['in_process']
        self.is_completed = data['is_completed']