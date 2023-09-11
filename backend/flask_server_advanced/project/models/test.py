from enum import IntFlag
from datetime import datetime, timedelta
from flask import current_app
from sqlalchemy.orm.query import Query
from project.extensions import db, bcrypt
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import BaseQuery
from random import randint
from typing import Tuple, Optional

class UserRole(IntFlag):
    USER = 1
    USER_ADMIN = 2
    BACKEND_ADMIN = 4



class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    given_name = db.Column(db.String(128))
    family_name = db.Column(db.String(128))
    cellphone_number = db.Column(db.String(128))
    cellphone_cc = db.Column(db.String(16))  # cellphone_country_code
    username = db.Column(db.String(128), unique=True, nullable=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)
    roles = db.Column(db.Integer, default=UserRole.USER.value, nullable=False)
    password = db.Column(db.String(255), nullable=True)
    token_hash = db.Column(db.String(255), nullable=True)
    email_token_hash = db.Column(db.String(255), nullable=True)
    email_validation_date = db.Column(db.DateTime, nullable=True)
    google_id = db.Column(db.String(64), unique=True, nullable=True)  # null if never logged in google
    google_access_token = db.Column(db.String, nullable=True)
    fb_id = db.Column(db.String(64), unique=True, nullable=True)  # null if never logged in facebook
    fb_access_token = db.Column(db.String, nullable=True)
    cellphone_validation_code = db.Column(db.String(4))
    cellphone_validation_code_expiration = db.Column(db.DateTime, nullable=True)
    cellphone_validation_date = db.Column(db.DateTime, nullable=True)
    
    refer_to_friend_link = db.Column(db.String)

    associated_groups = db.relationship("UserGroupAssociation", back_populates="user")
    groups = association_proxy('associated_groups', 'group')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, email:str, password:str=None, given_name:str=None, family_name:str=None, cellphone_number:str=None, cellphone_cc:str=None,
                 email_validation_date:datetime=None, google_id:str=None, google_access_token:str=None, fb_id:str=None, fb_access_token:str=None, cellphone_validation_code:str=None,
                 cellphone_validation_code_expiration:datetime=None,
                 cellphone_validation_date:datetime=None, roles:UserRole=UserRole.USER, created_at:datetime=datetime.utcnow()):
        self.email = email
        self.given_name = given_name
        self.family_name = family_name
        if password:
            self.password = bcrypt.generate_password_hash(password,
                                                          current_app.config.get('BCRYPT_LOG_ROUNDS')).decode()
        self.created_at = created_at
        self.updated_at = created_at
        self.cellphone_number = cellphone_number
        self.cellphone_cc = cellphone_cc
        self.email_validation_date = email_validation_date
        self.fb_id = fb_id
        self.fb_access_token = fb_access_token
        self.google_id = google_id
        self.google_access_token = google_access_token
        self.cellphone_validation_code = cellphone_validation_code
        self.cellphone_validation_code_expiration = cellphone_validation_code_expiration
        self.cellphone_validation_date = cellphone_validation_date
        self.roles = roles.value

    def __repr__(self):
        return '<User %r>' % self.email

    @staticmethod
    def first_by(**kwargs):
        """Get first db entity that match to criterium"""
        return User.query.filter_by(**kwargs).first()

    def first(*criterion):
        """Get first db entity that match to criterium"""
        return User.query.filter(*criterion).first()

    @staticmethod
    def get(id: int):
        """Get db entity that match the id"""
        return User.query.get(id)

