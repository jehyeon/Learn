from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)


class RegistUser(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        args = parser.parse_args()

        name = args['name']
        email = args['email']

        return {'name': name, 'email': email}


api.add_resource(RegistUser, '/user')

if __name__ == '__main__':
    app.run(debug=True)