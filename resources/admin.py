from flask_restful import Resource
import json
from flask import request
from helpers.admin import *


class AdminApi(Resource):

    def post(self, route):
        if route == "CreateAdmin":
            return CreateUser()