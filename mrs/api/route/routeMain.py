from flask import Flask, request, jsonify
from flask import Blueprint
from flask_jwt import  current_identity
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from mrs.api.route.administradorRoute import adm


import sys
sys.path.append(".")


home_api = Blueprint('api',__name__)


from mrs.api.schema.SchemaMain import TaskSchema 
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


from mrs import db
from mrs.api.model.modelMain import Task



class Api(adm):

    @jwt_required()
    @home_api.route('/', methods=['POST'])
    def create_task():
        title =  request.values.get("title", type=str, default=None)
        description = request.values.get("description", type=str, default=None)

        new_task= Task(title, description)

        db.session.add(new_task)
        db.session.commit()

        return task_schema.jsonify(new_task) 

    @jwt_required()
    @home_api.route('/', methods=['GET'])
    def get_tasks():
        all_tasks = Task.query.all()
        result = tasks_schema.dump(all_tasks)
        return jsonify(result)

    @jwt_required()
    @home_api.route('/<id>', methods=['GET'])
    def get_task(id):
        task = Task.query.get(id)
        return task_schema.jsonify(task)

    @jwt_required()
    @home_api.route('/<id>', methods=['PUT'])
    def update_task(id):
        task = Task.query.get(id)

        title = request.json['title']
        description = request.json['description']

        task.title = title
        task.description = description

        db.session.commit()

        return task_schema.jsonify(task)
    @jwt_required()
    @home_api.route('/<id>', methods=['DELETE'])
    def delete_task(id):
        task = Task.query.get(id)
        db.session.delete(task)
        db.session.commit()
        return task_schema.jsonify(task)



