import requests as request
import random, os
from datetime import timedelta, datetime
from dotenv import load_dotenv
from database.access_control import realizarCadastroDoIp, cadastrarDatasDeAcesso
from api.api_time_zone_db import buscarDataHoraAtual


load_dotenv()

chave_api = os.getenv("API_KEY2") 
url_base = "https://www.googleapis.com/youtube/v3/search"
todos_ids_gerados = []
videos_ids_escolhido_aletoriamente = []
todos_titulos_videos = []
titulos_escolhido_aleatoriamente = []
i = 0
nextPage = None

def buscarMusicaAleatoria(genero_musical, endereco_ip):
    global i
    global todos_ids_gerado
    global videos_ids_escolhido_aletoriamente
    global todos_titulos_videos
    global nextPage
    global  titulos_escolhido_aleatoriamente
    
    if len(videos_ids_escolhido_aletoriamente) > 0:
        videos_ids_escolhido_aletoriamente.clear()
        titulos_escolhido_aleatoriamente.clear()
    
    todos_ids_gerados.clear()
    
    for i in range(0, 5):
        
        print(nextPage)
        order = random.choice(['date','viewCount','relevance'])
        
        parametros = {
                    "part": "snippet",
                    "type": "video",
                    "videoCategoryId": "10",
                    "maxResults": 50,
                    "q": f"{genero_musical} song",
                    "key": chave_api,
                    "videoDuration": "medium",
                    "videoDefinition": "high",  # Alta qualidade
                    "order" : order,
                    "pageToken": nextPage
        }
  
        resposta = request.get(url_base, params=parametros)
        print(resposta.status_code)
      
        if resposta.status_code == 200:
            
            videos = resposta.json().get("items", [])
            nextPage = resposta.json().get("nextPageToken")
            
            for video in videos:
                if video["snippet"].get("liveBroadcastContent") != "upcoming":        
                    todos_ids_gerados.append(video.get("id", {}).get("videoId"))
                    todos_titulos_videos.append(video["snippet"].get("title"))

            print(f"Quantidade de ids_gerados: {len(todos_ids_gerados)}")
            

    for j in range(0, 10):
        id_video_aleatorio = random.choice(todos_ids_gerados)

        videos_ids_escolhido_aletoriamente.append(id_video_aleatorio)
        posicao_id = todos_ids_gerados.index(id_video_aleatorio)

        titulos_escolhido_aleatoriamente.append(todos_titulos_videos[posicao_id])

        todos_ids_gerados.pop(posicao_id)
        todos_titulos_videos.pop(posicao_id)

    data_e_hora_atual = buscarDataHoraAtual()
    data_e_hora_liberado = data_e_hora_atual + timedelta(days=1)
    realizarCadastroDoIp(endereco_ip)
    cadastrarDatasDeAcesso(endereco_ip, data_e_hora_atual, data_e_hora_liberado)
  
    return videos_ids_escolhido_aletoriamente,titulos_escolhido_aleatoriamente
