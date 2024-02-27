import json
from flask import request
from config.db import db
from models.aspci_base import Presence
from flask import jsonify  




def CreatePresence():
    reponse = {}

    try:
        firstname = request.json.get('p_firstname')
        lastname = request.json.get('p_lastname')
        matricule = request.json.get('p_matricule')
        # admin_id = request.json.get('admin_id')
    

        new_presence = Presence()

        new_presence.p_firstname = firstname
        new_presence.p_lastname = lastname
        new_presence.p_matricule = matricule
        # new_presence.admin_id = admin_id
        try:
            db.session.add(new_presence)
            db.session.commit()
            print("La presence a été enregistrée avec succès !")
        except Exception as e:
            db.session.rollback()
            print(f"Une erreur s'est produite : {str(e)}")

        reponse['status'] = 'success'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse




def getPresence():
    response = {}
    
    try:
        a_id = request.json.get('admin_id')
        all_presence = Presence.query.filter_by(admin_id=a_id).all()

        if all_presence:
            information = []

            for item in all_presence:
                item_info = {
                    'id': item.id,
                    'matricule': item.p_matricule,
                    'lastname': item.p_lastname,
                    'firstname': item.p_firstname,
                    'date':str(item.creation_date),
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
