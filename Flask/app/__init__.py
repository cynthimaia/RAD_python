from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS
#pip install flask-cors
#facilita a interação com banco de dados

app = Flask(__name__)
CORS(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db' #URI do banco de dados
api = Api(app)
db = SQLAlchemy(app)
#instancia do objeto SQLalchemy

from app.models.products import Products
with app.app_context(): #contexto da aplicação
    db.create_all()

from app.view.reso_products import Index,ProductCreate, ProductUpdate, ProductDelete,ProductById
api.add_resource(Index, "/")
api.add_resource(ProductCreate, "/create")
api.add_resource(ProductUpdate, "/update")
api.add_resource(ProductDelete, "/delete")
api.add_resource(ProductById, '/search')

'''@app.route("/index")
def index():
    #return "<h1> Minha Aplicação em Flask </h1>"
    return render_template("index.html")'''
