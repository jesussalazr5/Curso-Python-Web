from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import flash
from flask import url_for
from flask import redirect

app = Flask("Meu app")
app.config["SECRET_KEY"] = "pudim"

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


@app.route("/login", methods=["GET", "POST"])
def login():
    erro = None
    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "admin":
            session["logado"] = True
            flash("Bem vindo")
            return redirect(url_for("exibir_entradas"))
        else:
            erro = "Usuario ou senha invalidos"
    return render_template("login.html", erro=erro)
