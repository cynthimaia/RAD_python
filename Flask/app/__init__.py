from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#facilita a interação com banco de dados

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db' #URI do banco de dados

db = SQLAlchemy(app)
#instancia do objeto SQLalchemy

from app.models.products import Products
with app.app_context(): #contexto da aplicação
    db.create_all()

@app.route("/index")
def index():
    #return "<h1> Minha Aplicação em Flask </h1>"
    return render_template("index.html")
