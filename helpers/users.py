import json
from flask import request
from config.db import db
from models.aspci_base import Users
from flask import jsonify  
import uuid



#la fonction qui permet de de creer un utilisateur 
def CreateUser():

    reponse = {}

    try:

        #les variable qui permet de recuperer les infomation de l'utilisateur 
        firstname = request.json.get('firstname')
        lastname = request.json.get('lastname')
        email = request.json.get('email')
        date_of_birth = request.json.get('date_of_birth')
        place_of_birth = request.json.get('place_of_birth')
        number = request.json.get('number')
        function = request.json.get('function')
        parents_name = request.json.get('parents_name')
        parents_number = request.json.get('parents_number')
        id = str(uuid.uuid4())

    
        #nouvelle instance de la classe user qui se trouve dans le dossier model
        new_users = Users()


        #initialisation de chaque colonne de la classe par les variables interne
        new_users.u_firstname = firstname
        new_users.u_lastname = lastname
        new_users.u_email = email
        new_users.u_date_of_birth = date_of_birth
        new_users.u_place_of_birth = place_of_birth
        new_users.u_number = number
        new_users.u_function = function
        new_users.u_parents_name = parents_name
        new_users.u_parents_number = parents_number
        new_users.u_uid = id

        
          # Ajouter l'instance à la session et la sauvegarder dans la base de données
        try:
            #ajout de toutes les informations de l'utilisateur dans la base de donnée
            db.session.add(new_users)
            db.session.commit()
            print("Les informations de l'utilisateurs ont été enregistrées avec succès !")
        except Exception as e:
            db.session.rollback()
            print(f"Une erreur s'est produite : {str(e)}")

        reponse['satus'] = 'success'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse




# def UpdateUser():

#     reponse = {}

#     try:
#         firstname = request.json.get('firstname')
#         lastname = request.json.get('lastname')
#         email = request.json.get('email')
#         date_of_birth = request.json.get('date_of_birth')
#         place_of_birth = request.json.get('place_of_birth')
#         number = request.json.get('number')
#         function = request.json.get('function')
#         parents_name = request.json.get('parents_name')
#         parents_number = request.json.get('parents_number')
    
#         update_users = Users.query.filter_by(id=1).first()


#         update_users.user_firstname = firstname
#         update_users.user_lastname = lastname
#         update_users.user_email = email
#         update_users.user_date_of_birth = date_of_birth
#         update_users.user_place_of_birth = place_of_birth
#         update_users.user_number = number
#         update_users.user_function = function
#         update_users.user_parents_name = parents_name
#         update_users.user_parents_number = parents_number

#         try:
#             db.session.add(update_users)
#             db.session.commit()
#             print("Les informations de l'utilisateur ont été modifiés avec succès !")
#         except Exception as e:
#             db.session.rollback()
#             print(f"Une erreur s'est produite : {str(e)}")

#         reponse['satus'] = 'success'

#     except Exception as e:
#         reponse['error_description'] = str(e)
#         reponse['status'] = 'error'

#     return reponse



def UpdateUser():
    response = {}

    try:
        # Récupérer l'utilisateur à mettre à jour depuis la base de données en fonction de l'ID
        update_user = Users.query.filter_by(user_uid='ee15fb98-ebea-42e0-be04-ca63220af58c').first()

        if update_user:
            # Récupérer les nouvelles informations de l'utilisateur depuis la requête JSON
            firstname = request.json.get('firstname')
            lastname = request.json.get('lastname')
            email = request.json.get('email')
            date_of_birth = request.json.get('date_of_birth')
            place_of_birth = request.json.get('place_of_birth')
            number = request.json.get('number')
            function = request.json.get('function')
            parents_name = request.json.get('parents_name')
            parents_number = request.json.get('parents_number')

            # Mettre à jour les informations de l'utilisateur avec les nouvelles données
            update_user.user_firstname = firstname
            update_user.user_lastname = lastname
            update_user.user_email = email
            update_user.user_date_of_birth = date_of_birth
            update_user.user_place_of_birth = place_of_birth
            update_user.user_number = number
            update_user.user_function = function
            update_user.user_parents_name = parents_name
            update_user.user_parents_number = parents_number

            # Enregistrer les modifications dans la base de données
            try:
                db.session.add(update_user)
                db.session.commit()
                response['status'] = 'success'
                response['message'] = f"Informations de l'utilisateur avec l'ID  mises à jour avec succès!"
            except Exception as e:
                db.session.rollback()
                response['status'] = 'error'
                response['error_description'] = str(e)
        else:
            response['status'] = 'error'
            response['message'] = f"Utilisateur avec l'ID  non trouvé."

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response




def DeleteUser():
    response = {}

    try:
        id = request.json.get('user_uid')
        # Rechercher l'utilisateur à supprimer dans la base de données en fonction de l'ID
        deleted_user = Users.query.filter_by(user_uid=id).first()

        if deleted_user:
            # Supprimer l'utilisateur de la base de données
            try:
                db.session.delete(deleted_user)
                db.session.commit()
                response['status'] = 'success'
                response['message'] = f"Utilisateur avec l'ID {id} supprimé avec succès!"
            except Exception as e:
                db.session.rollback()
                response['status'] = 'error'
                response['error_description'] = str(e)
        else:
            response['status'] = 'error'
            response['message'] = f"Utilisateur avec l'ID {id} non trouvé."

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response



def GetUsers():
    response = {}
    
    try:
        # Récupérer tous les utilisateurs depuis la base de données
        all_users = Users.query.all()

        if all_users:
            # Créer une liste pour stocker les informations de tous les utilisateurs
            users_information = []

            # Parcourir tous les utilisateurs pour récupérer leurs informations
            for user in all_users:
                user_info = {
                    'user_uid': user.user_uid,
                    'firstname': user.user_firstname,
                    'lastname': user.user_lastname,
                    'email': user.user_email,
                    'date_of_birth': user.user_date_of_birth,
                    'place_of_birth': user.user_place_of_birth,
                    'number' : user.user_number,
                    'function' : user.user_function,
                    'parents_name' : user.user_parents_name,
                    'parents_number' : user.user_parents_number,
                    # ... Ajoutez d'autres informations d'utilisateur si nécessaire
                }
                users_information.append(user_info)

            response['status'] = 'success'
            response ['users'] = users_information
        else:
            response['status'] = 'error'
            response['message'] = 'Aucun utilisateur trouvé dans la base de données.'

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response




def GetSingleUser():
    response = {}

    try:
        id = request.json.get('user_uid')
        # Récupérer l'utilisateur depuis la base de données en fonction de l'ID
        user = Users.query.filter_by(user_uid= id).first()

        if user:
            # Créer un dictionnaire pour stocker les informations de l'utilisateur
            user_info = {
                'user_uid': user.user_uid,
                'firstname': user.user_firstname,
                'lastname': user.user_lastname,
                'email': user.user_email,
                'date_of_birth': user.user_date_of_birth,
                'place_of_birth': user.user_place_of_birth,
                'number' : user.user_number,
                'function' : user.user_function,
                'parents_name' : user.user_parents_name,
                'parents_number' : user.user_parents_number,
                # ... Ajoutez d'autres informations d'utilisateur si nécessaire
            }

            response['status'] = 'success'
            response['user'] = user_info
        else:
            response['status'] = 'erreur'
            response['message'] = f"Aucun utilisateur trouvé avec l'ID suivant: {id}."

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response
