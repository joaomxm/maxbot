from flask import Blueprint
from flask_restful import Api

from .resources import *

bp = Blueprint("api", __name__, url_prefix='/api')
api = Api(bp)

api.add_resource(FacesRobot,'/robot/')

def init_app(app):
    """Inicializar blueprint """
    app.register_blueprint(bp)
