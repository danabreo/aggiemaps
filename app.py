from flask import Flask, jsonify
from flask_restful import Resource, reqparse, Api

app = Flask(__name__)
api = Api(app)

class Version(Resource):
  def get(self):
    return '1.0.0 - August 10, 2019'

api.add_resource(Version, '/version')

if __name__=='__main__':    
  app.run(debug=True)
