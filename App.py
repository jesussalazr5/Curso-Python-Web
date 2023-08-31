from flask import Flask

app = Flask("Meu app")


@app.route("/")
def hello():
    return "Hello World"


@app.route("/novo")
def novo():
    return "<h1> Nova Pagina</h1>"
