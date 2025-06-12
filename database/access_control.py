from database.connect import Connect
from psycopg2 import Error

def realizarCadastroDoIp(endereco_ip):
    connect = Connect()
    connection = connect.conn()

    cursor = connection.cursor() # type: ignore
    cursor.execute("SELECT 1 FROM access WHERE endereco_ip = %s", (endereco_ip,))

    if cursor.fetchone():
        print("Já existe o endereço de ip na tabela")
    else:
        print("Ip não cadastrado, inserindo no banco de dados")
        try:
            cursor.execute("INSERT INTO access (endereco_ip) VALUES (%s)", (endereco_ip,))
            connection.commit() # type: ignore
            print("Dados inseridos com sucesso")
        except Error as e:
            print(f"Erro ao tentar inserir os dados: {e}")

    connect.closeConn(connection)

def cadastrarDatasDeAcesso(endereco_ip, data_e_hora, data_e_hora_liberado):
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

def retonarDataHoraLiberada(endereco_ip):
    data_e_hora_liberado = None
    connect = Connect()
    connection = connect.conn()
    cursor = connection.cursor() # type: ignore
    try:
        cursor.execute("SELECT data_e_hora_liberado FROM access WHERE endereco_ip=%s",(endereco_ip,))
        result = cursor.fetchone()

        if result: 
            data_e_hora_liberado = result[0]

        connection.commit() # type: ignore
        print(data_e_hora_liberado)
    except Error as e:
        print(f"Erro ao buscar data e hora liberado: {e}")
    
    connect.closeConn(connection)

    return data_e_hora_liberado
