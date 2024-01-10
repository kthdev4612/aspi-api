from flask_restful import Resource
import json
from flask import request
from helpers.users import *



class UsersApi(Resource):
    def post(self, route):
        if route == "CreateUser":
            return CreateUser()
        
        if route == "DeletedUser":
            return DeleteUser()

    # def delete(self, route):
    #     if route == "DeletedUser":
    #         return DeleteUser()
    

    def patch(self, route):
        if route == "Updateuser":
            return UpdateUser()


    def get(self, route):
        if route == "GetAllUsers":
            return GetUsers()
        
        if route == 'GetSingleUser':
            return GetSingleUser()