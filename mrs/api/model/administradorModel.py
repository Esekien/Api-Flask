from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import safe_str_cmp


import sys
sys.path.append(".")
from mrs import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False, unique=True)
    full_name = db.Column(db.Text, nullable=False)

    # NOTE: In a real application make sure to properly hash and salt passwords
    def check_password(self, password):
        return safe_str_cmp(password, "password")

#PREGUNTAR SI YA EXISTEN PARA NO CREARLO DE NUEVO
#db.create_all()

