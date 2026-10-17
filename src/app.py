from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hola mundo</h1>"


@app.route("/hola")
def hola():
    return "<h1>Hola PWA - IEVN1003</h1>"


@app.route("/user/<string:nom>")
def user(nom):
    return "Hola, {}".format(nom)


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