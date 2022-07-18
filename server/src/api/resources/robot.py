from flask_restful import Resource
from flask import jsonify

from ...services import executar

class FacesRobot(Resource):
    """ Resource Face Robot """

    def get(self):
        """ GET  """
        executar('feliz')
        return jsonify({'message':'hello'})
