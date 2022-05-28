from src.database_connection import Connection


# Class responsável por recuperar todos os pedidos do usuário
class Request_List(list):

    def __init__(self, user_cpf) -> None:
        self.cpf = user_cpf
    

    def generate_list(self, connection) -> str:
        query = connection.query_collect(f"""SELECT requests.request_number, requests.product, 
        requests.payment_method FROM users INNER JOIN requests ON users.cpf = requests.user_cpf 
        WHERE users.cpf = '{self.cpf}'""")

        return query