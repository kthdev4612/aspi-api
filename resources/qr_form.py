from flask_restful import Resource
import json
from flask import request
from helpers.qr_form import *



class Qr_formApi(Resource):
    def get(self, route):
        if route == "form":
            return form()
