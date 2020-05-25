import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from db import db
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

PORT = os.environ.get('PORT', 5000)

app = Flask(__name__, template_folder='../template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.secret_key = os.environ['SECRET_KEY']
app.secret_key = 'secret'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    app.run(port=PORT, debug=True)
