from flask_restplus import Api
from flask import Blueprint
from .namespace1 import api as ns1


blueprint = Blueprint('api', __name__)
api = Api(blueprint)

api.add_namespace(ns1)
# api.add_namespace(ns1, path='/prefix/of/ns1')
