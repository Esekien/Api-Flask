from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import safe_str_cmp

import sys
sys.path.append(".")
from mrs import db





class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True)
    description = db.Column(db.String(100))

    def __init__(self, title, description):
        self.title = title
        self.description = description



#PREGUNTAR SI YA EXISTEN PARA NO CREARLO DE NUEVO
#db.create_all()




