from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()


courses = {
    1: {'name': 'python', 'videos': 13},
    2: {'name': 'Java', 'videos': 10},
    3: {'name': 'VB', 'videos': 20}
           }


class Main(Resource):
    def get(self, course_id):
        if course_id == 0:
            return courses
        else:
            return courses[course_id]

    def delete(self, course_id):
        del courses[course_id]
        return courses

    def post(self, course_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('videos', type=int)
        courses[course_id] = parser.parse_args()
        return courses




api.add_resource(Main, '/api/courses/<int:course_id>')  # handler for address /api/main (Main - class with method get

api.init_app(app)  # initializing of handler for address /api/main

if __name__ == '__main__':
    app.run(port=3000, host='localhost', debug=True)
