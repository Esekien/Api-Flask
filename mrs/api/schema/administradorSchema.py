from flask_marshmallow import Marshmallow
from mrs.api.model.administradorModel import User
import sys
sys.path.append(".")
from mrs import app


ma = Marshmallow(app)

class AdminSchema(ma.Schema):
    class Meta:
        model = User
        fields = ('id', 'username', 'full_name')
