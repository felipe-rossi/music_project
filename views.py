from app import app
from flask import render_template
from flask import request
from api_youtube import buscarMusicaAleatoria

todos_generos = ['rock alternativo','rock','afrobeats','arrochadeira','avant-pop','axé','black MIDI','bubblegum dance','bubu','chacarera','champeta','chillwave','cloud rap',
                 'cumbia villera','dolewave','downtempo','dream trance','eletrobrega','eurotrance','eurobeat','flamenco house','grupero','hip hop chines','idilio',
                 'italodance','japanoise','kaseko','Konsrock','kuduro','maloya','mantinada','martial industrial','memphis rap','moombahton','murder ballad','musica ambiente'
                 ,'circense','mizrahi','pop arabe','profana','sertaneja','taoista','utilitária','novo flamenco','nu-disco','pastoral','pastoril' ,'polca','pop progressivo',
                 'rumba catalana','seapunk','sovietwave','vallenato','vaporwave','xuc','zukuma', 'trap', 'trap brasileiro', 'forro', 'metalcore', 'rap anime', 'sertanejo', 'nu-metal', 'funk', 'funk brasileiro']


@app.route("/", methods=['GET', 'POST'])
def homePage():
    
    videos_ids_escolhido_aletoriamente = []
    loading = False
    genero_musical = ""
    quantidade_musicas = 0
    mensagem_alert = ""
    
    if request.method == "POST":
        genero_musical = request.form.get('txtGenero', type=str)
        quantidade_musicas = request.form.get('inputQuantidadeMusica', type=int)
        
        if genero_musical != None:
            genero_musical = genero_musical.replace('í', 'i').replace('ê', 'e').replace('ö', 'o').replace('ú', 'u').replace('á', 'a').lower()
            
            if genero_musical not in todos_generos or genero_musical == "" or quantidade_musicas <= 0 or quantidade_musicas > 4:
                mensagem_alert = "Verifique os campos digitados por favor e tente novamente!"
                genero_musical = None
            
            elif genero_musical != None:
                videos_ids_escolhido_aletoriamente = buscarMusicaAleatoria(genero_musical, quantidade_musicas) 
    
        
    return render_template("index.html", 
                           genero_musical=genero_musical, 
                           mensagem_alert=mensagem_alert,
                           quantidade_musicas=quantidade_musicas,
                           videos_ids_escolhido_aletoriamente=videos_ids_escolhido_aletoriamente,
                           loading=loading)

