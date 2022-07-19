from flask_restful import Resource,reqparse
from flask import jsonify

from ...services import executar

class FacesRobot(Resource):
    """ Resource Face Robot """
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('face', type = str, default='default',
                                    required=False,location='args')

    def get(self):
        """ GET  """
        args = self.reqparse.parse_args()

        # executar(args)
        return jsonify({'message':'Sucesso','data': [
            (3,0),(2,1),(3,2),(3,5),(2,6),(3,7),
            (5,1),(6,2),(6,3),(6,4),(6,5),(5,6)
        ]})
