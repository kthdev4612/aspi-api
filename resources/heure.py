from flask_restful import Resource
import json
from flask import request
from helpers.heure import *


class HeureApi(Resource):

    def post(self, route):
        if route == "createHeure":
            return heure()
    
    def get(self, route):
        if route == "getHeure":
            return getHeure()
        