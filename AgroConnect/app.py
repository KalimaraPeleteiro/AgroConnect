from flask import Flask, redirect, render_template, request, session
from src.database_connection import Connection
from src.request_list import Request_List
from src.request import Request
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

    # Recuperando os pedidos do usuário
    if 'cpf' in session: 
        list = Request_List(session['cpf'])
        list = list.generate_list(db)
        
        return render_template("dashboard.html", list=list)
    
    # Recuperando TODOS os pedidos
    if 'cnpj' in session: 
        list = Request_List(session['cnpj'])
        list = list.generate_list(db)

        return render_template("dashboard_juridic.html", list=list)


@app.route("/form")
def request_form():
    if 'user' not in session:
        return redirect("/login")

    return render_template("request_form.html")


@app.route("/order/<int:id>")
def order_details(id):
    if 'user' not in session:
        return redirect("/login")    

    query = db.query_collect(f"SELECT * FROM requests WHERE requests.request_number = '{id}'")
    user = db.query_collect(f"""SELECT * FROM users INNER JOIN requests 
                            ON users.cpf = requests.user_cpf 
                            WHERE requests.user_cpf = '{query[0][0]}'""")

    request = Request(query[0][1], query[0][2], query[0][3], query[0][4], query[0][5])

    return render_template("order.html", request=request, user=user[0][3])


# Rotas Intermediárias
@app.route("/validate", methods=["POST"])
def validate_user():
    email = request.form['email']
    password = request.form['password']

    query = db.query_collect("SELECT * FROM users")
    query_companies = db.query_collect("SELECT * FROM companies")

    # Buscando na lista de usuários físicos
    for user in query: 
        if user[1] == email and user[2] == password:
            session['cpf'] = user[0]
            session['user'] = email
            return redirect("/dashboard")
    else:
        # Buscando na lista de usuários jurídicos
        for user in query_companies: 
            if user[1] == email and user[2] == password:
                session['cnpj'] = user[0]
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
    description = request.form['message']
    cellphone = request.form['cellphone']

    db.query_change(f"""INSERT INTO requests VALUES('{session['cpf']}', 
    '{request_number}', '{product}', '{payment_method}', '{description}',
    '{cellphone}', 1)""")

    return redirect("/dashboard")


@app.route("/statuschange/<int:id>")
def status_change(id):

    db.query_change(f"UPDATE requests SET status = '2' WHERE request_number = '{id}'")

    return redirect("/dashboard")


@app.route("/leave")
def logout():
    del session['user']

    if 'cpf' in session:
        del session['cpf']
    elif 'cnpj' in session:
        del session['cnpj']
    
    return redirect("/")


app.run(debug=True)
