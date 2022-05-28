from flask import Flask, redirect, render_template, request, session
from src.database_connection import Connection
from src.request_list import Request_List
from random import randint


app = Flask(__name__, template_folder='template')
app.secret_key = 'AgroConnect'

# Configurando Banco de Dados
db = Connection("Startup-AgroConnect", "kalimara", "hitman", "localhost", 5432)


# Rotas da Aplicação
@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/login")
def login_form():
    return render_template("login.html")


@app.route("/signup")
def sign_up_form():
    return render_template("signup.html")


@app.route("/dashboard")
def dahsboard():
    if 'user' not in session:
        return redirect("/login")

    list = Request_List(session['cpf'])
    list = list.generate_list(db)
    
    return render_template("dashboard.html", list=list)


@app.route("/form")
def request_form():
    if 'user' not in session:
        return redirect("/login")

    return render_template("request_form.html")


# Rotas Intermediárias
@app.route("/validate", methods=["POST"])
def validate_user():
    email = request.form['email']
    password = request.form['password']

    query = db.query_collect("SELECT * FROM users")

    for user in query:
        if user[1] == email and user[2] == password:
            session['cpf'] = user[0]
            session['user'] = email
            return redirect("/dashboard")
    else:
        return redirect("/signup")


@app.route("/registrate", methods=["POST"])
def registrate_user():
    return redirect("/login")


@app.route("/create", methods=["POST"])
def create_request():
    product = request.form['product']
    payment_method = request.form['payment']
    request_number = randint(1, 100000)

    db.query_change(f"""INSERT INTO requests VALUES('{session['cpf']}', 
    '{request_number}', '{product}', '{payment_method}')""")

    return redirect("/dashboard")


@app.route("/leave")
def logout():
    del session['user']
    return redirect("/")


app.run(debug=True)
