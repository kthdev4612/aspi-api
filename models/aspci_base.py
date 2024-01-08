import datetime
from config.db import *
from sqlalchemy.sql import expression
import uuid


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_firstname = db.Column(db.String(128), nullable=False)
    u_lastname = db.Column(db.String(128), nullable=False)
    u_email = db.Column(db.String(128), nullable=False)
    u_date_of_birth = db.Column(db.String(128), nullable=False)
    u_place_of_birth = db.Column(db.String(128), nullable=False)
    u_number = db.Column(db.String(128), nullable=False)
    u_function = db.Column(db.String(128), nullable=False)
    u_parents_name = db.Column(db.String(128), nullable=False)
    u_parents_number = db.Column(db.String(128), nullable=False)
    u_uid = db.Column(db.String(128))
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)


class Reports(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_Id = db.Column(db.Integer, db.ForeignKey(Users.id) )
    r_comment = db.Column(db.String(255), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)