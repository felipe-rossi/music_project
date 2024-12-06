from app import app
from flask import render_template
from flask import request
from api_youtube import buscarMusicaAleatoria

todos_generos = ['rock alternativo','rock','afrobeats','arrochadeira','avant-pop','axé','black MIDI','bubblegum dance','bubu','chacarera','champeta','chillwave','cloud rap',
                'cumbia villera','dolewave','downtempo','dream trance','eletrobrega','eurotrance','eurobeat','flamenco house','grupero','hip hop chines','idilio',
                'italodance','japanoise','kaseko','Konsrock','kuduro','maloya','mantinada','martial industrial','memphis rap','moombahton','murder ballad','musica ambiente'
                ,'circense','mizrahi','pop arabe','profana','sertaneja','taoista','utilitária','novo flamenco','nu-disco','pastoral','pastoril' ,'polca','pop progressivo',
                'rumba catalana','seapunk','sovietwave','vallenato','vaporwave','xuc','zukuma', 'trap', 'trap brasileiro', 'forro', 'metalcore', 'rap anime', 'sertanejo', 
                'nu-metal', 'funk', 'funk brasileiro', 'sertanejo universitário','rock clássico','hard rock','punk rock','indie rock','black metal','death metal','doom metal','power metal','speed metal','thrash metal','grunge','progressive rock','glam rock','pop',
                'pop tradicional','pop eletrônico','dance pop','synthpop','k-pop','hip hop','rap','gangsta rap','conscious rap','lo-fi', 'hip hop','hip hop alternativo','eletrônica','electronic dance music',
                'house','techno','trance','drum and bass','dubstep','electro swing','chillwave','jazz','jazz tradicional','bebop','smooth jazz','jazz fusion','free jazz','latin jazz','dixieland','blues',
                'blues tradicional','chicago blues','delta blues','blues rock','reggae','reggae tradicional','dub','dancehall','ska','country','country tradicional','country pop','country rock','bluegrass',
                'r&b','r&b clássico','neo-soul','contemporary r&b','funk americano','soul','soul clássico','motown','funk soul','folk','folk tradicional','indie folk','folk rock', 'folk metal','americana','clássica',
                'música clássica','barroca','romântica','música contemporânea','música de câmara','música latina','salsa','bachata','merengue','cumbia','reggaeton','flamenco','tango','bossa Nova','world music',
                'música africana','música indiana','música árabe','música celta','mpb', 'samba', 'forró','gospel','gospel tradicional','contemporary christian music','música gospel americana','música gospel brasileira',
                'punk','punk tradicional','hardcore punk','pop punk','anarcho-punk','new age','música ambiental','música espiritual','música instrumental','industrial','industrial rock','industrial metal',
                'electronic body music','experimental','música concreta','avant-garde','noise','funk tradicional','funk carioca', 'funk paulista','funk rock','música de video game','chiptune','post-rock',
                'shoegaze','post-punk','rock emo','ska punk','hardcore','techno trance','breakbeat','glitch','future bass','chillout','tropical house','synthwave','reggaeton','afrobeat','zydeco', 'pagode', 'metal sinfônico']


@app.route("/", methods=['GET', 'POST'])
def homePage():
    
    videos_ids_escolhido_aletoriamente = []
    genero_musical = ""
    mensagem_alert = ""
    
    if request.method == "POST":
        genero_musical = request.form.get('txtGenero', type=str)
        
        if genero_musical != None:
            genero_musical = genero_musical.replace('í', 'i').replace('ê', 'e').replace('ö', 'o').replace('ú', 'u').replace('á', 'a').lower()
            
            if genero_musical not in todos_generos or genero_musical == "":
                mensagem_alert = "Verifique os campos digitados por favor e tente novamente!"
                genero_musical = None
            
            elif genero_musical != None:
                videos_ids_escolhido_aletoriamente = buscarMusicaAleatoria(genero_musical) 
    
        
    return render_template("index.html", 
                           genero_musical=genero_musical, 
                           mensagem_alert=mensagem_alert,
                           videos_ids_escolhido_aletoriamente=videos_ids_escolhido_aletoriamente)

