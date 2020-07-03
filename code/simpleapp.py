from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from user import UserRegister

newapp = Flask(__name__)
api = Api(newapp)
newapp.secret_key = "babuji"
jwt = JWT(newapp, authenticate, identity)

items = []

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="price field is mandatory"

    )

    def post(self, name):
        data = Item.parser.parse_args()
        if next(filter(lambda x:x['name']==name,items), None):
            return {'Item': f"Item with name {name} already exists"}, 400

        data = request.get_json(silent=True)
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 200

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x:x['name']==name,items), None)
        return {'Item':item}, 200 if item else 404


api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')
newapp.run(host='0.0.0.0',port=50000)