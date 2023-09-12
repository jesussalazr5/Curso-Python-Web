from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import flash
from flask import url_for
from flask import redirect
from posts import posts
from flask import abort
import sqlite3
from flask import g


app = Flask(__name__)  # antes estava meu app
app.config["SECRET_KEY"] = "pudim"
app.config.from_object(__name__)

DATABASE = "banco.db"


def conectar():
    return sqlite3.connect(DATABASE)


@app.before_request
def before_request():
    g.bd = conectar()


@app.teardown_request
def teardown_request(f):
    g.bd.close()


@app.route("/")
def exibir_entradas():
    # entradas = posts[::-1]  # Mock das postagens
    sql = "SELECT titulo, texto, data_criacao FROM posts ORDER BY id DESC"
    resultado = g.bd.execute(sql)
    entradas = []

    for titulo, texto, data_criacao in resultado.fetchall():
        entradas.append(
            {"titulo": titulo, "texto": texto, "data_criacao": data_criacao}
        )

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


@app.route("/logout")
def logout():
    session.pop("logado", None)
    flash("Logout OK")
    return redirect(url_for("exibir_entradas"))


@app.route("/inserir", methods=["POST"])
def inserir_entrada():
    if not session["logado"]:
        abort(401)
    titulo = request.form.get("titulo")
    texto = request.form.get("texto")
    sql = "INSERT INTO posts (titulo, texto) values(?,?)"
    g.bd.execute(sql, [titulo, texto])
    g.bd.commit()
    flash("Post criado com sucesso!")
    return redirect(url_for("exibir_entradas"))


# @app.route("/posts/<int:id>")
# def detalhe_entrada(id):
#     try:
#         entradas = posts[id - 1]
#         return render_template("detalhe_entrada.html", entradas=entradas)
#     except Exception:
#         return abort(404)
