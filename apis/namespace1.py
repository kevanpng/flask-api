from flask_restplus import Namespace, Resource, fields

api = Namespace('cats', description='Cats ops')

cat = api.model(
    'Cat',
    {
        'id': fields.String(required=True, description='cat id'),
        'name': fields.String(required=True, description='cat name')
    }
)

CATS = [
    {
        'id': 'felix',
        'name': 'Felix'
    }
]


@api.route('/')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(cat)
    def get(self):
        """
        list all cats
        """
        return CATS


@api.route('/<id>')
@api.param('id', 'the cat identifier')
@api.response(404, 'Cat not found')
class Cat(Resource):
    @api.doc('get_cat')
    @api.marshal_list_with(cat)
    def get(self, id):
        for cat in CATS:
            if cat['id'] == id:
                return cat
        api.abort(404)
