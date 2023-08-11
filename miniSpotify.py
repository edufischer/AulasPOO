import random
import os #para chamar comandos do sistema

baseDeDados = [
    ['Fa fe fi fo Funk',	'Anira', 'Funk', 2019, '3:05'],
    [ 'Sofrência de programar', 'Ada & Turing',	'Sertanejo', 1998, '2:58' ],
    [ 'Rock’n Rolo', 'The Buns','Rock',	1984, '4:01' ],
    [ 'Grifinoria Girls', 'Katy Potter', 'Pop',	2017, '2:25' ],
    ['Outra musica', 'Anira', 'Funk', 2019, '3:05']
]

playlist = []

# Tasks das Funcoes


def ExibirBaseDados():
    id = 0
    for linha in baseDeDados:
        print(f'{id:<4}', end='')
        for item in linha:
            print(f'{item:<25}', end='')
        print()  # Quebra de linha
        id += 1

def MontarPlayList():
    continuar = 'S'
    while continuar == 'S':
        musica_add = int(input('Digite o ID da música para adicionar a playlist: '))
        musica_add = baseDeDados[musica_add]
        if musica_add not in playlist:
            playlist.append(musica_add)
        else: print('Musica já está na playlist. Favor tente novamente outra música.')
        continuar = input('Deseja continuar? S/N: ').upper()

def VisualizarPlaylist():
    id = 0
    for linha in playlist:
        print(f'{id:<4}', end='')
        for item in linha:
            print(f'{item:<25}', end='')
        print()  # Quebra de linha
        id += 1

def EmbaralharPlaylist():
    random.shuffle(playlist) 

def DuracaoTotal():
    tempos = []
    total_minutos = 0
    total_segundos = 0
    for i in playlist:
        tempo = (i[4])
        tempos.append(tempo)

    for i in tempos:
        minutos, segundos = map(int, i.split(":"))
        total_segundos += segundos
        total_minutos += minutos
    print("Tempo total:", total_minutos, 'minutos e',total_segundos,'segundos')

def ConsultarMusica():
    musica = input('Digite o nome da música: ').lower().capitalize()
    for linha in baseDeDados:
        for nome in linha:
            if nome == musica:
                print('\nO indice da musica no banco é: ', baseDeDados.index(linha))

def ConsultarBanda():
    contador = 0
    lista_indices = []
    artista = input('Digite o nome do artista/banda: ').lower().capitalize()
    for linha in baseDeDados:
        for nome in linha:
            if nome == artista:
                contador += 1
                indice = baseDeDados.index(linha)
                lista_indices.append(indice)
    print(f'Foram encontradas: {contador} músicas do artista/banda {artista}. Os índices das músicas são: {lista_indices}')

# Programa abaixo

def Iniciar():
    print()
    print('Iniciando o programa...')
    # Carregar ou ler dados de entrada

def EscolherOpcao():
    print()
    print('1 - Visualizar Base de Dados do Spotify')
    print('2 - Montar sua Playlist')
    print('3 - Visualizar minha Playlist')
    print('4 - Embaralhar minha Playlist')
    print('5 - Mostrar tempo de duração da Playlist')
    print('6 - Consultar música')
    print('7 - Consultar por banda/artista')
    print('0 -Sair\n')
    resposta = input('Escolha uma opção: ')
    os.system('cls'if os.name== 'nt'else'clear')
    return resposta

def Executar():
    terminarExecucao = False
    while not terminarExecucao: # enquanto terminar execucao for falso vai ficar no looping
        acaoUsuario = EscolherOpcao()
        if (acaoUsuario == '1'):
            ExibirBaseDados()
        elif (acaoUsuario == '2'):
            MontarPlayList()
        elif (acaoUsuario == '3'):
            VisualizarPlaylist()
        elif (acaoUsuario == '4'):
            EmbaralharPlaylist()
        elif (acaoUsuario == '5'):
            DuracaoTotal()
        elif (acaoUsuario == '6'):
            ConsultarMusica()
        elif (acaoUsuario == '7'):
            ConsultarBanda()   
        elif (acaoUsuario == '0'):
            terminarExecucao = True #terminarExecucao é falso, logo vai sair do loop no proximo giro.
        else:
            print('Escolha invalida!Tente de novo.')

def Finalizar():
    print('O programa foi encerrado!')
    # Salvar dados, encerrar processos etc

# Programa principal
if __name__ == '__main__':
    Iniciar()
    Executar()
    Finalizar()