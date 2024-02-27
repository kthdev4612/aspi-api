from flask_restful import Resource
import json
from flask import request
from helpers.reports import *



class ReportsApi(Resource):
    
    def post(self, route):
        if route == "CreateReport":
            return createReport()
        
        if route == "getSingleReport":
            return GetSingleReport()
        
        if route == "GetAllReport":
            return Getreport()


    # def delete(self, route):
    #     if route == "DeletedRport":
    #         return "true"
    

    # def patch(self, route):
    #     if route == "UpdateReport":
    #         return "true"


    # def get(self, route):
    #     if route == "GetAllReport":
    #         return Getreport()
        
        # if route == 'GetSingleReport':
        #     return "true"