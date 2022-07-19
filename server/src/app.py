from flask import Flask
from flask_cors import CORS
from . import api


def create_app():
    """ Criando o App Flask  """
    app = Flask(__name__)
    CORS(app)

    api.init_app(app)

    return app
