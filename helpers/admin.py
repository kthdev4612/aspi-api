import json
from flask import request
from config.db import db
from models.aspci_base import Admin
from flask import jsonify  
import uuid
import bcrypt


#la fonction qui permet de de creer un utilisateur 
def CreateUser():

    reponse = {}

    try:

        #les variable qui permet de recuperer les infomation de l'utilisateur 
        firstname = request.json.get('firstname')
        lastname = request.json.get('lastname')
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        number = request.json.get('number')
        role = request.json.get('role')
        country = request.json.get('country')
        id = str(uuid.uuid4())
        # matricule = "ASPCI_" + str(uuid.uuid4()).upper().replace('-', '')[:4]


        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    
        #nouvelle instance de la classe user qui se trouve dans le dossier model
        new_admin = Admin()


        #initialisation de chaque colonne de la classe par les variables interne
        new_admin.a_firstname = firstname
        new_admin.a_lastname = lastname
        new_admin.a_username = username
        new_admin.a_email = email
        new_admin.a_password = hashed_password
        new_admin.a_number = number
        new_admin.a_role = role
        new_admin.a_country = country
        new_admin.a_uid = id
        # new_users.u_matricule = matricule

        
          # Ajouter l'instance à la session et la sauvegarder dans la base de données
        try:
            #ajout de toutes les informations de l'utilisateur dans la base de donnée
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