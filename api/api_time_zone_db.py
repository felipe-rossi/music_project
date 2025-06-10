import requests as request
from datetime import datetime

def buscarDataHoraAtual():
    
    parametros = {
        "key": "VUBR9078YMH6",
        "format":"json",
        "country": "BR",
        "by": "zone",
        "zone": "America/Sao_Paulo"
        
    }
    resposta = request.get(url="https://api.timezonedb.com/v2.1/get-time-zone", params=parametros)

    if resposta.status_code != 200:
        raise Exception("Erro ao obter data e hora da API")
    else:
        data_e_hora_atual = resposta.json()["formatted"]
        data_e_hora_atual_convertida = datetime.strptime(data_e_hora_atual, "%Y-%m-%d %H:%M:%S")

        return data_e_hora_atual_convertida
