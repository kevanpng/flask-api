from flask_restplus import Api
from .namespace1 import api as ns1


api = Api(
    title='my title',
    version='1.0',
    description='random description'
)

api.add_namespace(ns1)
# api.add_namespace(ns1, path='/prefix/of/ns1')
