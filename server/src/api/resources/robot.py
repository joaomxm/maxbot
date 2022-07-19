from flask_restful import Resource,reqparse
from flask import jsonify

from ...services import executar

class FacesRobot(Resource):
    """ Resource Face Robot """
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('face', type = str, default='feliz',
                                    required=False,location='args')

    def get(self):
        """ GET  """
        args = self.reqparse.parse_args()

        resp = executar(args['face'])

        return jsonify({'message':'Sucesso','data': resp})
