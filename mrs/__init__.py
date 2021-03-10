from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import create_access_token
from flask_jwt_extended import current_user
from flask_jwt import  jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
import sys
sys.path.append(".")



@jwt_required()
def get(self):
    return {"State": "Success"}


app = Flask(__name__)



app.config["JWT_SECRET_KEY"] = "super-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/ejemplo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

jwt = JWTManager(app)
db = SQLAlchemy(app)

from mrs.api.route.routeMain import home_api
app.register_blueprint(home_api, url_prefix='/api')

from mrs.api.route.administradorRoute import admin
app.register_blueprint(admin, url_prefix='/login')


