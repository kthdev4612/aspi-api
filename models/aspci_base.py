import datetime
from config.db import *
from sqlalchemy.sql import expression
import uuid


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_firstname = db.Column(db.String(128), nullable=False)
    u_lastname = db.Column(db.String(128), nullable=False)
    u_username = db.Column(db.String(128), nullable=False)
    u_email = db.Column(db.String(128), nullable=False)
    u_password = db.Column(db.String(128), nullable=False)
    u_date_of_birth = db.Column(db.String(128), nullable=False)
    u_place_of_birth = db.Column(db.String(128), nullable=False)
    u_number = db.Column(db.String(128), nullable=False)
    u_function = db.Column(db.String(128), nullable=False)
    u_matricule = db.Column(db.String(128), nullable=False)
    u_parents_name = db.Column(db.String(128), nullable=False)
    u_parents_number = db.Column(db.String(128), nullable=False)
    u_img_link = db.Column(db.Text())
    u_uid = db.Column(db.String(128))
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)


class Reports(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    r_comment = db.Column(db.String(255), nullable=False)
    user_matricule = db.Column(db.String(255), nullable=False)
    user_uid = db.Column(db.String(255), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    a_firstname = db.Column(db.String(128), nullable=False)
    a_lastname = db.Column(db.String(128), nullable=False)
    a_username = db.Column(db.String(128), nullable=False)
    a_email = db.Column(db.String(128), nullable=False)
    a_password = db.Column(db.String(128), nullable=False)
    a_number = db.Column(db.String(128), nullable=False)
    a_role = db.Column(db.String(128), nullable=False)
    a_matricule = db.Column(db.String(128), nullable=False)
    a_country = db.Column(db.String(128), nullable=False)
    a_uid = db.Column(db.String(128))
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

class StatusReport(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    u_id = db.Column(db.Integer, db.ForeignKey('users.id') )
    u_firstname = db.Column(db.String(255), nullable=False)
    a_firstname = db.Column(db.String(255), nullable=False)
    a_matricule = db.Column(db.String(255), nullable=False)
    s_status = db.Column(db.String(255), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)