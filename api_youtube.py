import requests as request
import random
from datetime import datetime
from dotenv import load_dotenv
import os


load_dotenv()

chave_api = os.getenv("API_KEY") 
url_base = "https://www.googleapis.com/youtube/v3/search"
todos_ids_gerados = []
videos_ids_escolhido_aletoriamente = []
todos_titulos_videos = []
i = 0
nextPage = None


def buscarMusicaAleatoria(genero_musical):
    global i
    global todos_ids_gerado
    global videos_ids_escolhido_aletoriamente
    global todos_titulos_videos
    global nextPage
    
    if len(videos_ids_escolhido_aletoriamente) > 0:
        videos_ids_escolhido_aletoriamente.clear()
        todos_titulos_videos.clear()
    
    todos_ids_gerados.clear()
    
    order = random.choice(['date','viewCount','relevance'])
    
    for i in range(0, 1):
        
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
                    "videoEmbeddable": "true", # Apenas vídeos incorporáveis
                    "order" : order,
                    "pageToken": nextPage
        }
  
        resposta = request.get(url_base, params=parametros)
        print(resposta.status_code)
        print(resposta.json().get("", []))
      
        if resposta.status_code == 200:
            
            videos = resposta.json().get("items", [])
            nextPage = resposta.json().get("nextPageToken")
            
            for video in videos:
                if video["snippet"].get("liveBroadcastContent") != "upcoming":        
                    todos_ids_gerados.append(video.get("id", {}).get("videoId"))
    
            print(f"Quantidade de ids_gerados: {len(todos_ids_gerados)}")

            for j in range(0, 8):
                videos_ids_escolhido_aletoriamente.append(random.choice(todos_ids_gerados))
                for video in videos:
                    if videos_ids_escolhido_aletoriamente[j] == video.get("id", {}).get("videoId"):
                        todos_titulos_videos.append(video["snippet"].get("title"))
        
    data_e_hora_atual = datetime.now()
    print("Todos os títulos: ",todos_titulos_videos)
    print("Todos os ids escolhidos aleatóriamente: ",videos_ids_escolhido_aletoriamente)
    return videos_ids_escolhido_aletoriamente,todos_titulos_videos,data_e_hora_atual
