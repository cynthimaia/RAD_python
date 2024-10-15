from flask import Flask, render_template


app = Flask(__name__)

@app.route("/index")
def index():
    #return "<h1> Minha Aplicação em Flask </h1>"
    return render_template("index.html")
