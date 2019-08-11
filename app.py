from flask import Flask, jsonify
from flask_restful import Resource, reqparse, Api

app = Flask(__name__)
api = Api(app)

class Version(Resource):
    def get(self):
        return '1.1.0 - August 11, 2019'



api.add_resource(Version, '/version')
#api.add_resource(Coordinates, '/coordinates/<string:stop>')
#api.add_resource(Routes, '/routes/<string:startLat>/<string:startLng>/<string:endLat>/<string:endLng>')

if __name__=='__main__':
  app.run(debug=True)
    
