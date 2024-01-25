import json
from flask import request
from config.db import db
from models.aspci_base import Arrive
from models.aspci_base import Users
from flask import jsonify  
import uuid
from datetime import datetime


def CreateArrive():

    reponse = {}

    try:

        matricule = request.json.get('matricule')

        new_arrive = Arrive()


        new_arrive.a_matricul = matricule



        try:
            db.session.add(new_arrive)
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



def GetReport():
    response = {}
    
    try:
        all_report = Arrive.query.all()

        if all_report:
            report_information = []

            for report in all_report:

                my_date = report.creation_date.isoformat()

                report_info = {
                    'id': report.id,
                    'matricule': report.a_matricul,
                    'date_and_hour': my_date,
                }
                report_information.append(report_info)

            response['status'] = 'success'
            response ['result'] = report_information
        else:
            response['status'] = 'error'
            response['message'] = 'Aucun rapport trouvé dans la base de données.'

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response


def GetSingleUser():
    response = {}

    try:
        matricule = request.json.get('u_matricule')
        # Récupérer l'utilisateur depuis la base de données en fonction de l'ID
        user = Users.query.filter_by(u_uid= id).first()

        if user:
            # Créer un dictionnaire pour stocker les informations de l'utilisateur
            user_info = {
                'user_id': user.id,
                'user_uid': user.u_uid,
                'firstname': user.u_firstname,
                'lastname': user.u_lastname,
                'username': user.u_username,
                'email': user.u_email,
                'date_of_birth': user.u_date_of_birth,
                'place_of_birth': user.u_place_of_birth,
                'number' : user.u_number,
                'function' : user.u_function,
                'parents_name' : user.u_parents_name,
                'parents_number' : user.u_parents_number,
                'matricule' : user.u_matricule,

                # ... Ajoutez d'autres informations d'utilisateur si nécessaire
            }

            response['status'] = 'success'
            response['result'] = user_info
        else:
            response['status'] = 'erreur'
            response['message'] = f"Aucun utilisateur trouvé avec l'ID suivant: {id}."

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response