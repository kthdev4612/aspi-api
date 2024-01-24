import json
from flask import request
from config.db import db
from models.aspci_base import Arrive
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
                    'date and hour': my_date,
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