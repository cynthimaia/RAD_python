from flask_restful import Resource
from flask import jsonify
class Index(Resource):
    def get(self):
        return jsonify("Bem vindo a aplicacao Flask")
