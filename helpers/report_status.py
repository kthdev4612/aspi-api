import json
from flask import request
from config.db import db
from models.aspci_base import StatusReport
from flask import jsonify  
import uuid



def createReportStatus():
    response = {}

    try:


        status = request.json.get('s_status')
        firstname = request.json.get('u_firstname')
        agen_firstname = request.json.get('a_firstname')
        agent_matricule = request.json.get('a_matricule')
        id = request.json.get('u_id')
        

        new_status = StatusReport()

        new_status.u_id = id
        new_status.u_firstname = firstname
        new_status.a_firstname = agen_firstname
        new_status.a_matricule = agent_matricule
        new_status.s_status = status

        try:
            db.session.add(new_status)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Une erreur s'est produite : {str(e)}")

        response['satus'] = 'success'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response





def GetReportStatus():
    response = {}
    
    try:
        
        all_reportSatus = StatusReport.query.all()

        if all_reportSatus:
            reportStatus_information = []

            for report in all_reportSatus:
                reportStatus_info = {
                    'status': report.s_status,
                    'matricule': report.a_matricule,
                    'agent_firstname': report.a_firstname,
                    'user_firstname': report.u_firstname,
                    
                }
                reportStatus_information.append(reportStatus_info)

            response['status'] = 'success'
            response ['result'] = reportStatus_information
        else:
            response['status'] = 'error'
            response['message'] = 'Aucun rapport trouvé dans la base de données.'

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response