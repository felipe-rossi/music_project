from app import app
from flask import render_template
from flask import request
from api.api_youtube import buscarMusicaAleatoria
from unidecode import unidecode 
from database.access_control import retonarDataHoraLiberada
import redis

todos_generos = ['rock alternativo','rock','afrobeats','arrochadeira','avant-pop','axé','black MIDI','bubblegum dance','bubu','chacarera','champeta','chillwave','cloud rap',
                'cumbia villera','dolewave','downtempo','dream trance','eletrobrega','eurotrance','eurobeat','flamenco house','grupero','hip hop chines','idilio',
                'italodance','japanoise','kaseko','Konsrock','kuduro','maloya','mantinada','martial industrial','memphis rap','moombahton','murder ballad','musica ambiente'
                ,'circense','mizrahi','pop arabe','profana','sertaneja','taoista','utilitária','novo flamenco','nu-disco','pastoral','pastoril' ,'polca','pop progressivo',
                'rumba catalana','seapunk','sovietwave','vallenato','vaporwave','xuc','zukuma', 'trap', 'trap brasileiro', 'forro', 'metalcore', 'rap anime', 'sertanejo', 
                'nu-metal', 'funk', 'funk brasileiro', 'sertanejo universitário','rock classico','hard rock','punk rock','indie rock','black metal','death metal','doom metal',
                'power metal','speed metal','thrash metal','grunge','progressive rock','glam rock','pop','pop tradicional','pop eletronico','dance pop','synthpop','k-pop','hip hop',
                'rap','gangsta rap','conscious rap','lo-fi', 'hip hop','hip hop alternativo','eletrônica','electronic dance music','house','techno','trance','drum and bass','dubstep',
                'electro swing','chillwave','jazz','jazz tradicional','bebop','smooth jazz','jazz fusion','free jazz','latin jazz','dixieland','blues','blues tradicional','chicago blues',
                'delta blues','blues rock','reggae','reggae tradicional','dub','dancehall','ska','country','country tradicional','country pop','country rock','bluegrass','r&b','r&b classico',
                'neo-soul','contemporary r&b','funk americano','soul','soul classico','motown','funk soul','folk','folk tradicional','indie folk','folk rock', 'folk metal','americana','classica',
                'musica classica','barroca','romântica','musica contemporânea','musica de camara','musica latina','salsa','bachata','merengue','cumbia','reggaeton','flamenco','tango','bossa Nova',
                'world music','musica africana','musica indiana','musica arabe','musica celta','mpb', 'samba', 'forro','gospel','gospel tradicional','contemporary christian music','musica gospel americana'
                ,'musica gospel brasileira','punk','punk tradicional','hardcore punk','pop punk','anarcho-punk','new age','musica ambiental','musica espiritual','musica instrumental','industrial',
                'industrial rock','industrial metal','electronic body music','experimental','musica concreta','avant-garde','noise','funk tradicional','funk carioca', 'funk paulista','funk rock',
                'musica de video game','chiptune','post-rock','shoegaze','post-punk','rock emo','ska punk','hardcore','techno trance','breakbeat','glitch','future bass','chillout','tropical house',
                'synthwave','reggaeton','afrobeat','zydeco', 'pagode', 'metal sinfonico', 'babymetal', 'sertanejo universitario','eletronica']

videos_ids_escolhido_aletoriamente = []
genero_musical = ""
data_e_hora_liberado = ""
data_e_hora_atual = ""
videos_ids_com_titulo = []
resultado = ""
chave = ""

@app.route("/", methods=['GET', 'POST'])
def homePage():
    global resultado
    global chave
    global endereco_ip

    resultado = redis.Redis(host="localhost", port=6379, db=0)

    endereco_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    chave = f"ip:{endereco_ip}"

    if resultado.exists(chave):
        data_e_hora_liberado = retonarDataHoraLiberada(endereco_ip)
        if data_e_hora_liberado:
            data_e_hora_liberado = data_e_hora_liberado.strftime("%d/%m/%Y %H:%M:%S")
        return render_template("bloqueado.html", data_e_hora_liberado=data_e_hora_liberado)   
        
    return render_template("index.html")

@app.route("/resultado", methods=['GET', 'POST'])
def resultadoPage():
    global resultado
    global chave
    mensagem_alert = ""
    global videos_ids_com_titulo
    global genero_musical
    global videos_ids_escolhido_aletoriamente

    if request.method == "POST":
        genero_musical_raw = request.form.get('txtGenero', type=str)
        genero_musical = unidecode(genero_musical_raw).lower() if genero_musical_raw else ""   # type: ignore
        
        if not genero_musical or genero_musical not in todos_generos:
            mensagem_alert = "Verifique os campos digitados por favor e tente novamente!"
            genero_musical = None
            return render_template("index.html",
                                   mensagem_alert=mensagem_alert)
            
        else:
            try:
                videos_ids_escolhido_aletoriamente, todos_titulos_videos  = buscarMusicaAleatoria(genero_musical, endereco_ip) 
                videos_ids_com_titulo = zip(videos_ids_escolhido_aletoriamente, todos_titulos_videos)
                resultado.setex(chave,60,"bloqueado") # type: ignore #86400
            except Exception as e:
                mensagem_alert = "Erro ao buscar músicas. Tente novamente mais tarde."
                print("Erro na busca:", e)

        print("Genero: ", genero_musical)     

    return render_template("resultado.html", 
                           genero_musical=genero_musical, 
                           videos_ids_com_titulo=videos_ids_com_titulo,
                           videos_ids_escolhido_aletoriamente=videos_ids_escolhido_aletoriamente or [])