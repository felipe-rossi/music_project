import requests as request
import random

chave_api = "AIzaSyCc65gtzGyzvUzWrG2VK_dxwb6ldpzC0mg"
url_base = "https://www.googleapis.com/youtube/v3/search"
todos_ids_gerados = []
videos_ids_escolhido_aletoriamente = []
historico_ids = []
i = 0
nextPage = None


def buscarMusicaAleatoria(genero_musical, quantidade_musica, ):
    global i
    global todos_ids_gerado
    global videos_ids_escolhido_aletoriamente
    global nextPage
    
    if len(videos_ids_escolhido_aletoriamente) > 0:
        videos_ids_escolhido_aletoriamente.clear()
    
    todos_ids_gerados.clear()
    
    order = random.choice(['date','viewCount','relevance'])
    
    for i in range(0, 3):
        
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
        print(resposta.status_code)
        
        if resposta.status_code == 200:
            
            videos = resposta.json().get("items", [])
            nextPage = resposta.json().get("nextPageToken")
            
            for video in videos:
                if video["snippet"].get("liveBroadcastContent") != "upcoming":        
                    todos_ids_gerados.append(video.get("id", {}).get("videoId"))
    
    print(f"Quantidade de ids_gerados: {len(todos_ids_gerados)}")
    for j in range(0, quantidade_musica):
        videos_ids_escolhido_aletoriamente.append(random.choice(todos_ids_gerados))
    
    return videos_ids_escolhido_aletoriamente 