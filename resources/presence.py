from flask_restful import Resource
import json
from flask import request
from helpers.presence import *


class PresenceApi(Resource):

    def post(self, route):
        if route == "CreatePresence":
            return CreatePresence()
        
    def post(self, route):
        if route == "getAllPresence":
            return getPresence()
    
    # def get(self, route):
    #     if route == "getAllPresence":
    #         return getPresence()
        