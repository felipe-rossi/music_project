from connect import Connect
from psycopg2 import Error


def main(endereco_ip, data_e_hora, data_e_hora_liberado):
    connect = Connect()
    connection = connect.conn()

    cursor = connection.cursor() # type: ignore
    cursor.execute("SELECT 1 FROM access WHERE endereco_ip = %s", (endereco_ip,))

    if cursor.fetchone():
        print(f"Já existe o endereço {endereco_ip} na tabela")
    else:
        print("Ip não cadastrado, inserindo no banco de dados")
        try:
            cursor.execute("INSERT INTO access(endereco_ip, data_e_hora, data_e_hora_liberado) VALUES (%s, %s, %s)", (endereco_ip, data_e_hora, data_e_hora_liberado,))
            connection.commit() # type: ignore
            print("Dados inseridos com sucesso")
        except Error as e:
            print(f"Erro ao tentar inserir os dados: {e}")

    connect.closeConn(connection)

main("166.3.4.5","2025-06-07 14:30:00", "2025-06-08 14:30:00")