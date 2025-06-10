from database.connect import Connect
from psycopg2 import Error

def realizarCadastroDoIp(endereco_ip, data_e_hora, data_e_hora_liberado):
    connect = Connect()
    connection = connect.conn()

    cursor = connection.cursor() # type: ignore
    cursor.execute("SELECT 1 FROM access WHERE endereco_ip = %s", (endereco_ip,))

    if cursor.fetchone():
        print(f"Já existe o endereço {endereco_ip} na tabela")
        return True
    else:
        print("Ip não cadastrado, inserindo no banco de dados")
        try:
            cursor.execute("INSERT INTO access(endereco_ip, data_e_hora, data_e_hora_liberado) VALUES (%s, %s, %s)", (endereco_ip, data_e_hora, data_e_hora_liberado,))
            connection.commit() # type: ignore
            print("Dados inseridos com sucesso")
        except Error as e:
            print(f"Erro ao tentar inserir os dados: {e}")

    connect.closeConn(connection)

def cadastrarNovaData(endereco_ip, data_e_hora, data_e_hora_liberado):
    connect = Connect()
    connection = connect.conn()
    cursor = connection.cursor()  # type: ignore

    try:
        cursor.execute("UPDATE access SET data_e_hora=%s, data_e_hora_liberado=%s WHERE endereco_ip=%s",(data_e_hora, data_e_hora_liberado, endereco_ip,))
        connection.commit() # type: ignore
        print("Dados atualizados com sucesso")
    except Error as e:
        print(f"Erro ao tentar atualizar os dados: {e}")

    connect.closeConn(connection)

#def retonar