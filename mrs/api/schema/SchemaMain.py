from flask_marshmallow import Marshmallow
from mrs.api.model.modelMain import Task
import sys
sys.path.append(".")
from mrs import app


ma = Marshmallow(app)
class TaskSchema(ma.Schema):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description')

