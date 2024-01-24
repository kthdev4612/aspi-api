from flask_restful import Resource
import json
from flask import request
from helpers.arrive import *


class ArriveApi(Resource):

    def post(self, route):
        if route == "CreateArrive":
            return CreateArrive()
            

    def get(self, route):
        if route == "getReport":
            return GetReport()