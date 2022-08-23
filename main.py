from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api()


courses = {}


class Main(Resource):
    def get(self):
        return {'info': 'Some info', 'num': 56}


api.add_resource(Main, '/api/main')  # handler for address /api/main (Main - class with method get

api.init_app(app)  # initializing of handler for address /api/main

if __name__ == '__main__':
    app.run(port=3000, host='localhost', debug=True)
