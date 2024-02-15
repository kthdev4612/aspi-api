from flask_restful import Resource
import json
from flask import request
from helpers.report_status import *



class StatusReportsApi(Resource):
    
    def post(self, route):
        if route == "CreateReportStatus":
            return createReportStatus()
        
        # if route == "getSingleReport":
        #     return GetSingleReport()


    # def delete(self, route):
    #     if route == "DeletedRport":
    #         return "true"
    

    # def patch(self, route):
    #     if route == "UpdateReport":
    #         return "true"


    def get(self, route):
        if route == "GetAllReportStatus":
            return GetReportStatus()
        
        # if route == 'GetSingleReport':
        #     return "true"