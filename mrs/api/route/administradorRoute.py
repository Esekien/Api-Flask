from flask import Flask, request, jsonify
from flask import Blueprint
from flask_jwt import   jwt_required,current_identity
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import JWTManager 
from mrs import jwt

import sys
sys.path.append(".")


admin = Blueprint('login',__name__)




from mrs.api.schema.administradorSchema import AdminSchema

from mrs import db
from mrs.api.model.administradorModel import  User

class adm():
    # identity when creating JWTs and converts it to a JSON serializable format.
    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.id

    @jwt.user_lookup_loader
    @jwt_required() 
    def user_lookup_callback(_jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()



    @admin.route("/", methods=["POST"])
    
    def login():
        username = request.json.get("username", None)
        password = request.json.get("password", None)

        user = User.query.filter_by(username=username).one_or_none()
        if not user or not user.check_password(password):
            return jsonify("Wrong username or password"), 401

        # Notice that we are passing in the actual sqlalchemy user object here
        access_token = create_access_token(identity=user)
        return jsonify(access_token=access_token)


    @admin.route("/who_am_i", methods=["GET"])
    @jwt_required()
    def protected():
        # We can now access our sqlalchemy User object via `current_user`.
        return jsonify(
            id=current_user.id,
            full_name=current_user.full_name,
            username=current_user.username,
        )
