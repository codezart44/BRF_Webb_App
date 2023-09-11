
from flask import current_app
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from ..extensions import db, bcrypt
from datetime import datetime
from uuid import uuid4      # universally unique identifier


class UserRole:
    USER = 1
    USER_ADMIN = 2

class User(db.Model):
    __tablename__ = 'users'
    user_id = Column(Integer, default=uuid4(), primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone_number = Column(String(255), unique=True, nullable=False)
    active = Column(Boolean, default=True, nullable=False)
    role = Column(Integer, default=UserRole.USER, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)

    def __init__(
            self, 
            email:str, password:str, first_name:str, last_name:str, phone_number:str, 
            active:bool=True, role:UserRole=UserRole.USER, created_at:datetime=datetime.utcnow(),
        ) -> None:
        
        self.email = email
        self.pw_hash = bcrypt.generate_password_hash(password, current_app.config('APP_SETTINGS'))
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.active = active
        self.role = role
        self.created_at = created_at
        self.updated_at = created_at

    def __repr__(self) -> str:
        return f'<User \'{self.email}\'>'
    
    @staticmethod
    def all(*args):
        '''All users to meet criterion'''
        return User.query.filter(*args).all()

    @staticmethod
    def all_by(**kwargs):
        '''All users with attribute value'''
        return User.query.filter_by(**kwargs).all()
    
    @staticmethod
    def get(user_id: int):
        '''Get user by id'''
        return User.query.get(user_id)
    
    

    


# CREATE TABLE IF NOT EXISTS residents (
#     [resident_id] INT PRIMARY KEY,
#     -- [apartment_id] INT NOT NULL, 
#     -- [moved_in_dttm] VARCHAR(255) NOT NULL,
#     -- [moved_out_dttm] VARCHAR,
#     [first_name] VARCHAR(255) NOT NULL,
#     [last_name] VARCHAR(255) NOT NULL,
#     [email] VARCHAR(255) NOT NULL,
#     [phone_number] VARCHAR(255) NOT NULL,
#     [password] VARCHAR(255) NOT NULL,
#     [member_number] INT,                -- is signed up for news letters 
#     -- FOREIGN KEY ([apartment_id]) REFERENCES apartments([apartment_id])
# );

# CREATE TABLE IF NOT EXISTS laundry_users (
#     [laundry_user_id] INT PRIMARY KEY,
#     [resident_id] INT NOT NULL,
#     [num_bookings] INT NOT NULL,
#     FOREIGN KEY ([resident_id]) REFERENCES users([resident_id])
# );