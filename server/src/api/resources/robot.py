from flask_restful import Resource
from flask import jsonify

class FacesRobot(Resource):
    """ Resource Face Robot """

    def get(self):
        """ GET  """
        return jsonify({'message':'hello'})
