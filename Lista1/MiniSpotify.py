import random
import os 
from Musica import Musica

baseDeDados = [
    Musica('Fa fe fi fo Funk', 'Anira', 'Funk', 2019, '3:05'),
    Musica('Sofrência de programar', 'Ada & Turing', 'Sertanejo', 1998, '2:58'),
    Musica('Rock’n Rolo', 'The Buns', 'Rock', 1984, '4:01'),
    Musica('Vai Malandra', 'Anira', 'Funk', 2022, '5:00'),
]

playlist = []

# Tasks das Funcoes

def exibirBaseDados():
    indice = 0

    while indice < len(baseDeDados):
     musica = baseDeDados[indice]
     print(f"ID: {indice} - Título: {musica.titulo}. Artista: {musica.artista}. Genêro: {musica.genero}. Ano: {musica.ano}.")
     print()
     indice += 1  

def montarPlayList():
    continuar = 'S'
    while continuar == 'S':
        musica_add = int(input('Digite o ID da música para adicionar a playlist: '))
        if 0 <= musica_add < len(baseDeDados):
            objeto_musica = baseDeDados[musica_add]
            if objeto_musica not in playlist:
                playlist.append(objeto_musica)
            else:
                print('Música já está na playlist. Favor tentar outra música.')
        else:
            print('ID de música inválido.')
        continuar = input('Deseja continuar? S/N: ').upper()

def dadosPlaylist():
    indice = 0

    while indice < len(playlist):
     musica = playlist[indice]
     print(f"ID: {indice} - Título: {musica.titulo}. Artista: {musica.artista}. Genêro: {musica.genero}. Ano: {musica.ano}.")
     print()
     indice += 1  

def visualizarPlaylist(): 
    if len(playlist) == 0:
        print('A playlist está vazia.')
        return  # Sai da função se a playlist estiver vazia

    dadosPlaylist()
    
        
def tocarPlaylist():
    indice = 0

    if len(playlist) == 0:
        print('A playlist está vazia.')
        return 
    
    while indice < len(playlist):
     musica = playlist[indice]
     musica.tocarMusica()
     musica.encerrarMusica()
     print()
     indice += 1  
    

def embaralharPlaylist():
    if len(playlist) == 0:
        print('A playlist está vazia.')
        return 

    random.shuffle(playlist) 
    dadosPlaylist()


def duracaoTotal():
    indice = 0
    tempos = []

    while indice < len(playlist):
     musica = playlist[indice]
     tempos.append(musica.duracao)
     indice += 1  
    
    total_minutos = 0
    total_segundos = 0

    for tempo in tempos:
        minutos, segundos = map(int, tempo.split(':'))
        total_minutos += minutos
        total_segundos += segundos

    # Converter segundos extras para minutos
    total_minutos += total_segundos // 60
    total_segundos %= 60

    print(f"Tempo total: {total_minutos} minutos e {total_segundos} segundos")

def consultarMusica():

    nome = input('Digite o nome da música para procura-la: ')
    indice = 0

    # Acessando os atributos de cada objeto na lista
    while indice < len(baseDeDados):
     musica = baseDeDados[indice]
     if nome == musica.titulo:
        print(f"\nO ID da música {musica.titulo} é: {indice}.")
        break
     else: indice+= 1


def consultarBanda():
    artista = input('Digite o nome do artista/banda para procura-la: ')
    lista_musicas = []
    indice = 0

    while indice < len(baseDeDados):
     musica = baseDeDados[indice]
     if artista == musica.artista:
        lista_musicas.append(indice)
     indice+= 1 
    print(f'\nA lista de ID encontradas do Artista/Banda foi: {lista_musicas}')

# Programa abaixo

def iniciar():
    print()
    print('Iniciando o programa...')

def escolherOpcao():
    print()
    print('1 - Visualizar Base de Dados do Spotify')
    print('2 - Montar sua Playlist')
    print('3 - Visualizar minha Playlist')
    print('4 - Tocar minha Playlist')
    print('5 - Embaralhar minha Playlist')
    print('6 - Mostrar tempo de duração da Playlist')
    print('7 - Consultar música')
    print('8 - Consultar por banda/artista')
    print('0 -Sair\n')
    resposta = input('Escolha uma opção: ')
    os.system('cls'if os.name== 'nt'else'clear')
    return resposta

def executar():
    terminarExecucao = False
    while not terminarExecucao: # enquanto terminar execucao for falso vai ficar no looping
        acaoUsuario = escolherOpcao()
        if (acaoUsuario == '1'):
            exibirBaseDados()
        elif (acaoUsuario == '2'):
            montarPlayList()
        elif (acaoUsuario == '3'):
            visualizarPlaylist()
        elif (acaoUsuario == '4'):
            tocarPlaylist()    
        elif (acaoUsuario == '5'):
            embaralharPlaylist()
        elif (acaoUsuario == '6'):
            duracaoTotal()
        elif (acaoUsuario == '7'):
            consultarMusica()
        elif (acaoUsuario == '8'):
            consultarBanda()  
        elif (acaoUsuario == '0'):
            terminarExecucao = True #terminarExecucao é falso, logo vai sair do loop no proximo giro.
        else:
            print('Escolha invalida!Tente de novo.')

def finalizar():
    print('O programa foi encerrado!')
    # Salvar dados, encerrar processos etc

# Programa principal
if __name__ == '__main__':
    iniciar()
    executar()
    finalizar()