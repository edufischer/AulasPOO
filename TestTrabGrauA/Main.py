import csv
import random
import os


from Usuario import Usuario
from Album import Album

usuarios = []
figurinhas = []
trocas = []
nomeUsuarioAtual = None
nomeUsuarioAtual = None



def carregarUsuarios():
    global usuarios
    with open('usuarios.csv', 'r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
            nome = linha['Nome']
            senha = linha['Senha']
            album_serializado = linha['Album']
            album_dict = eval(album_serializado)  # Converta a string serializada em um dicionário
            album = Album.deserializar(album_dict)  # Use o método de deserialização do seu Album
            usuario = Usuario(nome, senha)
            usuario.setAlbum(album)  # Atribua o álbum ao usuário usando o método apropriado
            usuarios.append(usuario)
    print(usuarios)
    return usuarios
    

def salvarUsuarios():
    global usuarios
    with open('usuarios.csv', 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['Nome', 'Senha', 'Album'])
        
        for usuario in usuarios:
            nomeUsuario = usuario.getNomeDeUsuario()
            senhaUsuario = usuario.getSenhaDeUsuario()
            
            # Serializa o álbum do usuário para uma representação de texto
            albumSerializado = usuario.getAlbum().serializar()
            
            escritor.writerow([nomeUsuario, senhaUsuario, albumSerializado])



def Iniciar():
    print()
    print('Iniciando o programa...\n')
    print('Carregando o programa...\n')
    carregarUsuarios()
    #carregar_figurinhas()
    #carregar_trocas()


def Executar():
    global nomeUsuarioAtual
    global usuario
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Menu Principal:\n')
        print('1 - Criar Novo Album')
        print('2 - Acessar meu Album')
        print('0 -Sair\n')
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':

            nome = input('Digite seu nome de usuário: ')
            senha = input('Digite sua senha: ')
            novoUsuario = Usuario()  
            novoUsuario.cadastrar(nome, senha)
            usuarios.append(novoUsuario)
            print(usuarios)

        elif escolha == '2':
            nome = input('Digite seu nome de usuário: ')
            senha = input('Digite sua senha: ')
            for usuario in usuarios:
                nomeUsuarioAtual = str(usuario.getNomeDeUsuario())
                senhaUsuarioAtual = str(usuario.getSenhaDeUsuario())
                usuarioAlbumAtual = usuario.getAlbum()
                
                if nomeUsuarioAtual == nome and senhaUsuarioAtual == senha:
                    print('Efetuando o login...')
                    menuSecundario()
                       
        elif escolha == '2':
            menuTerciario()
        elif escolha == '0':
            break
        else:
            input("Opção inválida. Pressione Enter para continuar...")

def menuSecundario():
    global nomeUsuarioAtual
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Albúm de {nomeUsuarioAtual}:\n')
        print('1 - Ver album')
        print('2 - Gerenciar colecao')
        print('3 - Abrir pacote figurinhas')
        print('0 - Voltar menu principal\n')
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            # Faça a tarefa 1
            input("Tarefa 1 concluída. Pressione Enter para continuar...")
        elif escolha == '2':
            # Faça a tarefa 2
            input("Tarefa 2 concluída. Pressione Enter para continuar...")
        elif escolha == '0':
            break  # Voltar para o menu anterior
        else:
            input("Opção inválida. Pressione Enter para continuar...")

def menuTerciario():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Menu Opção 2:")
        print("1. Realizar tarefa 1")
        print("2. Realizar tarefa 2")
        print("3. Voltar para o Menu Principal")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            # Faça a tarefa 1
            input("Tarefa 1 concluída. Pressione Enter para continuar...")
        elif escolha == '2':
            # Faça a tarefa 2
            input("Tarefa 2 concluída. Pressione Enter para continuar...")
        elif escolha == '3':
            break  # Voltar para o menu anterior
        else:
            input("Opção inválida. Pressione Enter para continuar...")


def Finalizar():
    print('Inicilizando salvamento dos dados...!')
    # Função para salvar dados nos arquivos CSV
    global usuarios
    salvarUsuarios()
    print('O programa foi encerrado!')

# Programa principal
if __name__ == '__main__':
    Iniciar()
    Executar()
    Finalizar()


