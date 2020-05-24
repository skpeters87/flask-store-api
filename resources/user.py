from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='invalid entry')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='invalid entry')

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "UserModel already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'UserModel created successfully'}, 201

    def delete(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            UserModel.delete_from_db()
            return {'message': 'user deleted sucessfully'}

        return {'message': 'user not found'}, 400
