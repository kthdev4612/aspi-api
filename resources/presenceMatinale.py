from flask_restful import Resource
import json
from flask import request
from helpers.presenceMatinale import *


class PresenceMatinaleApi(Resource):

    def post(self, route):
        if route == "CreatePresenceMatinale":
            return CreatePresencematinale()
        else:
            return {"message": "Route non prise en charge"}, 404
        
    def post(self, route):
        if route == "getPresenceMatinale":
            return getPresenceMatinale()
    
    # def get(self, route):
    #     if route == "getAllPresence":
    #         return getPresence()
        