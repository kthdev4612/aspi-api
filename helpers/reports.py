import json
from flask import request
from config.db import db
from models.aspci_base import Reports
from flask import jsonify  
import uuid


def createReport():
    response = {}

    try:
        comment = request.json.get('comment')

        new_report = Reports()

        new_report.r_comment = comment
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