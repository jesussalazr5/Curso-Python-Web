from flask import Flask
from flask import render_template

app = Flask("Meu app")

# mock
posts = [
    {"titulo": "Minha primeira postagem", "texto": "teste"},
    {"titulo": "Segundo Post", "texto": "outro teste"},
]


@app.route("/")
def exibir_entradas():
    entradas = posts  # Mock das postagens
    return render_template("exibir_entradas.html", entradas=entradas)


@app.route("/layout")
def layout():
    return render_template("layout.html")
