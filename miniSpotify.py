import random

baseDeDados = [
    ['Fa fe fi fo Funk',	'Anira', 'Funk', 2019, '3:05'],
    [ 'Sofrência de programar', 'Ada & Turing',	'Sertanejo', 1998, '2:58' ],
    [ 'Rock’n Rolo', 'The Buns','Rock',	1984, '4:01' ],
    [ 'Grifinoria Girls', 'Katy Potter', 'Pop',	2017, '2:25' ],
    ['Outra musica', 'Anira', 'Funk', 2019, '3:05']
]

playlist = []


def ExibirBaseDados():
    id = 0
    for i in baseDeDados:
        for j in i:
            print (id, '\t',j, end = '\t')
        id = id + 1
        print() #quebra de linha

def MontarPlayList():
    musica_add = int(input('Digite o ID da música para adicionar a playlist: '))
    musica_add = baseDeDados[musica_add]
    if musica_add not in playlist:
        playlist.append(musica_add)
    else: print('Musica já está na playlist. Favor tente novamente outra música.')
   
def VisualizarPlaylist():
    id = 0
    for i in playlist:
        for j in i:
            print (id, '\t',j, end = '\t')
        id = id + 1
        print() 

def DuracaoTotal():
    tempos = []
    total_minutos = 0
    total_segundos = 0
    for i in playlist:
        tempo = (i[4])
        tempos.append(tempo)
    print(tempos)

    for i in tempos:
        minutos, segundos = map(int, i.split(":"))
        total_segundos += segundos
        total_minutos += minutos
    print("Tempo total em minutos:", total_minutos, "e em segundos:",total_segundos)


def ConsultarMusica():
    index = 5
    musica = input('Digite o nome da música: ')
    for linha in baseDeDados:
        for nome in linha:
            if nome == musica:
                print('O indice da musica no banco é: ', baseDeDados.index(linha))
               

# a) Visualizar base de dados: se escolhida esta opção, o programa deve mostrar ao usuário a tabela com todas as músicas
ExibirBaseDados()

# montar playlist
MontarPlayList()
MontarPlayList()

#visualizar playlist
VisualizarPlaylist()

#embaralhar playlist 

#mostrar duracao total da playlist, em minutos
DuracaoTotal() 

#consultar musica
ConsultarMusica()
#consultar por banda/musica