from flask import Flask, render_template
import os
from flask_restful import Resource, Api
from flask_migrate import Migrate
from config.db import db
from config.constant import *
from models.aspci_base import *
from resources.users import UsersApi
from resources.reports import ReportsApi
from resources.admin import AdminApi
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.secret_key = os.urandom(24)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = LIEN_BASE_DE_DONNEES
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False


db.init_app(app)

migrate = Migrate(app, db)
api = Api(app)





@app.route('/a')
def home():
    print('HELLO IM HERE')
    return render_template('index.html')

api.add_resource(UsersApi, '/api/user/<string:route>', endpoint='all_user', methods=['GET', 'POST', 'DELETE', 'PATCH'])
api.add_resource(ReportsApi, '/api/report/<string:route>', endpoint='all_report', methods=['GET', 'POST', 'DELETE', 'PATCH'])
api.add_resource(AdminApi, '/api/admin/<string:route>', endpoint='all_admin', methods=['GET', 'POST', 'DELETE', 'PATCH'])


if __name__ == '__main__':
    app.run(debug=True,  host="0.0.0.0")