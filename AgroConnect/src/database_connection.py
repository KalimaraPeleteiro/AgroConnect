import psycopg2

#Classe responsável pela conexão ao banco de dados
class Connection():

    def __init__(self, db, usr, pwd, host, port) -> None:
        self.database = psycopg2.connect(database=db, user=usr, password=pwd, host=host, port=port)


    def query_collect(self, query) -> str or bool:
        try:
            cursor = self.database.cursor()
            cursor.execute(query)
            query_result = cursor.fetchall()
        except Exception:
            return None
        return query_result


    def query_change(self, query) -> bool:
        try:
            cursor = self.database.cursor()
            cursor.execute(query)
            cursor.close()
            self.database.commit()
        except Exception:
            return False
        return True
