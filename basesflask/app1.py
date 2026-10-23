
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    titulo = "Pagina de inicio"
    listado = ["Python", "Flask", "Jinja2", "HTML", "CSS"]

    return render_template(
        "index.html",
        titulo=titulo,
        listado=listado
    )


@app.route("/operasbas", methods=["GET", "POST"])
def operasbas():
    n1 = ""
    n2 = ""
    res = None
    operacion = "sumar"
    error = None

    if request.method == "POST":
        n1 = request.form.get("n1", "").strip()
        n2 = request.form.get("n2", "").strip()
        operacion = request.form.get("operacion", "sumar")

        try:
            num1 = float(n1)
            num2 = float(n2)

            if operacion == "sumar":
                res = num1 + num2
            elif operacion == "restar":
                res = num1 - num2
            elif operacion == "multiplicar":
                res = num1 * num2
            else:
                error = "Selecciona una operacion valida."

        except ValueError:
            error = "Introduce dos numeros validos."

    return render_template(
        "operasbas.html",
        n1=n1,
        n2=n2,
        res=res,
        operacion=operacion,
        error=error
    )


@app.route("/distancia")
def distancia():
    return render_template("distancia.html")


@app.route("/hola")
def hola():
    return "<h1>Hola PWA - IEVN1003</h1>"


@app.route("/user/<string:nom>")
def user(nom):
    return "<h1>Hola User: {} </h1>".format(nom)


@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)


@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return "ID: {} nombre: {}".format(id, username)


@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es: {}".format(n1 + n2)


if __name__ == "__main__":
    app.run(debug=True)
