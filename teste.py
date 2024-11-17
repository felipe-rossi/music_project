import requests as request
import random

chave_api = "AIzaSyDaRYk2Tl3AqEjYsoXUOZzTw3u7wtKn5mU"
url_base = "https://www.googleapis.com/youtube/v3/search"
todos_ids_gerados = []
videos_ids_escolhido_aletoriamente = []
i = 0
nextPage = None


def buscarMusicaAleatoria(genero_musical, quantidade_musica):
    global i
    global todos_ids_gerado
    global videos_ids_escolhido_aletoriamente
    global nextPage
    order = random.choice(['date','viewCount','relevance'])
    
    for i in range(0, 10):
        
        print(nextPage)
        order = random.choice(['date','viewCount','relevance'])
        
        parametros = {
                    "part": "snippet",
                    "type": "video",
                    "videoCategoryId": "10",
                    "maxResults": 50,
                    "q": genero_musical,
                    "key": chave_api,
                    "videoDuration": "medium",
                    "order" : order,
                    "pageToken": nextPage
        }
  
        resposta = request.get(url_base, params=parametros)
        
        if resposta.status_code == 200:
            
            print("Status code 200")
            videos = resposta.json().get("items", [])
            nextPage = resposta.json().get("nextPageToken")
            
            for video in videos:
                todos_ids_gerados.append(video.get("id", {}).get("videoId"))
    
    for j in range(0, quantidade_musica):
        videos_ids_escolhido_aletoriamente.append(random.choice(todos_ids_gerados))
            