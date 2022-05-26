from flask import Flask, redirect, render_template, request
from src.database_connection import Connection


app = Flask(__name__, template_folder='template')

# Configurando Banco de Dados
db = Connection("Startup-AgroConnect", "kalimara", "hitman", "localhost", 5432)


# Rotas da Aplicação
@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/login")
def login_form():
    return render_template("login.html")


@app.route("/validate", methods=["POST"])
def validate_user():
    email = request.form['email']
    password = request.form['password']

    query = db.query_collect("SELECT * FROM users")

    for db_email, db_pwd in query:
        if db_email == email and db_pwd == password:
            return redirect("/dashboard")
    else:
        return redirect("/")


@app.route("/signup")
def sign_up_form():
    return render_template("sign_up.html")


@app.route("/dashboard")
def dahsboard():
    return render_template("dashboard.html")


app.run(debug=True)
