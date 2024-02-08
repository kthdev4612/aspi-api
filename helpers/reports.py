import json
from flask import request
from config.db import db
from models.aspci_base import Reports
from models.aspci_base import Users
from flask import jsonify  
import uuid

def createReport():
    response = {}

    try:


        comment = request.json.get('coment')
        u_id = request.json.get('user_id')
        u_matricule = request.json.get('user_matricule')
        u_uid = request.json.get('user_uid')

        new_report = Reports()

        new_report.r_comment = comment
        new_report.user_id = u_id
        new_report.user_matricule = u_matricule
        new_report.user_uid = u_uid

        try:
            #ajout de toutes les informations de l'utilisateur dans la base de donnée
            db.session.add(new_report)
            db.session.commit()
            print("Le rapport a été poster avec succès !")
        except Exception as e:
            db.session.rollback()
            print(f"Une erreur s'est produite : {str(e)}")

        response['satus'] = 'success'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response



def Getreport():
    response = {}
    
    try:
        
        all_report = Reports.query.all()

        if all_report:
            report_information = []

            for report in all_report:
                report_info = {
                    'report_id': report.id,
                    'user_id': report.user_id,
                    'comment': report.r_comment,
                    'matricule': report.user_matricule,
                    'uid': report.user_uid,
                    
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
