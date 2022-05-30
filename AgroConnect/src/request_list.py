from src.database_connection import Connection


# Class responsável por recuperar todos os pedidos do usuário
class Request_List(list):

    def __init__(self, user_id) -> None:
        self.id = user_id
    

    def generate_list(self, connection) -> str:

        # Se for um usuário, recupere seus pedidos
        if len(self.id) == 11: 
            query = connection.query_collect(f"""SELECT requests.request_number, requests.product, 
            requests.payment_method, requests.status FROM users INNER JOIN requests 
            ON users.cpf = requests.user_cpf WHERE users.cpf = '{self.id}'""")

            return query

        # Se for um usuário jurídico, recupere todos os pedidos.
        if len(self.id) == 14: 
            query = connection.query_collect("""SELECT requests.request_number, 
            requests.product, requests.payment_method FROM requests""")
            
            return query