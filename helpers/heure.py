import json
from flask import request
from config.db import db
from models.aspci_base import Heure
from flask import jsonify  


def heure():

    reponse = {}

    try:

        heure_debut = request.json.get('h_heure_debut')
        heure_fin = request.json.get('h_heure_fin')


        new_heure = Heure()

        new_heure.h_heure_debut = heure_debut
        new_heure.h_heure_fin = heure_fin
        
        try:
            db.session.add(new_heure)
            db.session.commit()
            print("L'heure a été ajouter !")
        except Exception as e:
            db.session.rollback()
            print(f"Une erreur s'est produite : {str(e)}")

        reponse['satus'] = 'success'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse


def getHeure():
    response = {}
    
    try:
        heure = Heure.query.all()

        if heure:
            information = []

            for item in heure:
                item_info = {
                    'id': item.id,
                    'debut':str(item.h_heure_debut),
                    'fin':str(item.h_heure_fin),
                }
                information.append(item_info)

            response['status'] = 'success'
            response ['result'] = information
        else:
            response['status'] = 'error'
            response['message'] = 'Aucun information trouvé dans la base de données.'

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response