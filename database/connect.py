import psycopg2, os
from psycopg2 import Error
from dotenv import load_dotenv

class Connect:
    load_dotenv()

    def conn(self):
        try:
            connect = psycopg2.connect(
                user="postgres",
                password=os.getenv("DB_PASSWORD"), # type: ignore
                host="127.0.0.1",
                port=5432,
                database="users")
           
            return connect
        
        except Error as e:
            print(f"Falha ao conectar ao banco de dados: {e}")

    def closeConn(self, connect):
        if connect:
            connect.close()