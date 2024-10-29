from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
#facilita a interação com banco de dados

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db' #URI do banco de dados
api = Api(app)
db = SQLAlchemy(app)
#instancia do objeto SQLalchemy

from app.models.products import Products
with app.app_context(): #contexto da aplicação
    db.create_all()

from app.view.reso_products import Index,ProductCreate, ProductUpdate, ProductDelete
api.add_resource(Index, "/")
api.add_resource(ProductCreate, "/create")
api.add_resource(ProductDelete, "/delete")

'''@app.route("/index")
def index():
    #return "<h1> Minha Aplicação em Flask </h1>"
    return render_template("index.html")'''
