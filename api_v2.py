from flask import Blueprint
from flask_restplus import Api
from apis.namespace1 import api as ns1

blueprint = Blueprint('api', __name__, url_prefix='/api/2')
api = Api(
    blueprint,
    title='my title 2',
    version='2.0',
    description='random desc 2',
)

api.add_namespace(ns1)
