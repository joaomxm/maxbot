from flask import Flask
from . import api


def create_app():
    """ Criando o App Flask  """
    app = Flask(__name__)
    
    api.init_app(app)

    return app
