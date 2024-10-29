from flask_restful import Resource, reqparse
from flask import jsonify
from app.models.products import Products
#adicionar
argumentos = reqparse.RequestParser()
argumentos.add_argument('name', type=str)
argumentos.add_argument("price", type=float)
#atualizar
argumentos_update = reqparse.RequestParser()
argumentos_update.add_argument('id', type=int)
argumentos_update.add_argument("name", type=str)
argumentos_update.add_argument("price", type=float)
#deletar
argumentos_delete = reqparse.RequestParser()
argumentos_delete.add_argument('id', type=int)


class ProductDelete(Resource):
    def delete(self):
        try:
            datas = argumentos_delete.parse_args()
            Products.delete_products(self, datas['id']) 
            return {"message": 'Product create successfully!'}, 200
        except Exception as e:
            return jsonify({'status':500,'msg':f'{e}'}), 500
        
class ProductUpdate(Resource):
    def put(self):
        try:
            datas = argumentos_update.parse_args()
            Products.update_products(self, datas['id'],datas['name'], datas['price'])
            return {"message": 'Product create successfully!'}, 200
        except Exception as e:
            return jsonify({'status':500,'msg':f'{e}'}), 500

class Index(Resource):
    def get(self):
        return jsonify("Bem vindo a aplicacao Flask")
class ProductCreate(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            Products.save_products(self, datas['name'], datas['price'])
            return {"message": 'Product create successfully!'}, 200
        except Exception as e:
            return jsonify({'status':500,'msg':f'{e}'}), 500

