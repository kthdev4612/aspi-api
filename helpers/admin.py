import json
from flask import request
from config.db import db
from models.aspci_base import Admin
from flask import jsonify  
import uuid
# import bcrypt
from werkzeug.security import generate_password_hash, check_password_hash


def CreateUser():

    reponse = {}

    try:

        firstname = request.json.get('firstname')
        lastname = request.json.get('lastname')
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        number = request.json.get('number')
        role = request.json.get('role')
        country = request.json.get('country')
        id = str(uuid.uuid4())
        matricule = "ASPCI_" + str(uuid.uuid4()).upper().replace('-', '')[:4]
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        new_admin = Admin()


        new_admin.a_firstname = firstname
        new_admin.a_lastname = lastname
        new_admin.a_username = username
        new_admin.a_email = email
        new_admin.a_password = hashed_password
        new_admin.a_number = number
        new_admin.a_role = role
        new_admin.a_country = country
        new_admin.a_uid = id
        new_admin.a_matricule = matricule



        try:
            db.session.add(new_admin)
            db.session.commit()
            print("Les informations de l'admin a été enregistrées avec succès !")
        except Exception as e:
            db.session.rollback()
            print(f"Une erreur s'est produite : {str(e)}")

        reponse['satus'] = 'success'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse




def Login():
    reponse = {}

    try:
        username = request.json.get('username')
        password = request.json.get('password')

        admin = Admin.query.filter_by(a_username=username).first()

        if admin and check_password_hash(admin.a_password, password):
            reponse['status'] = 'success'
            reponse['result'] = {
                'id': admin.id,
                'uid': admin.a_uid,
                'firstname': admin.a_firstname,
                'lastname': admin.a_lastname,
                'email': admin.a_email,
                'number': admin.a_number,
                'role': admin.a_role,
                'username': admin.a_username,
                'matricule': admin.a_matricule,
            }

        else:
            reponse['status'] = 'error'
            reponse['error_description'] = 'Nom d\'utilisateur ou mot de passe incorrect.'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse