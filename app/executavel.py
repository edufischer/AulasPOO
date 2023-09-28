import csv
import os

from Usuario import Usuario
from Album import Album
from Pagina import Pagina
from Figurinha import Figurinha

usuariosDataBase = []
usuariosNovos = []
usuarioLogado = None
verificandoLogin = False
usuariosCombinados = []

def carregarUsuarios():
   global usuariosDataBase
   try:
       with open('usuarios.csv', 'r', newline='') as arquivo_csv:
           leitor = csv.DictReader(arquivo_csv)
           for linha in leitor:
               usuariosDataBase.append(linha)
               print(usuariosDataBase)
       print('Usuários carregados com sucesso!')
   except FileNotFoundError:
       print('Arquivo de usuários não encontrado. Criando novo arquivo...')
 

def salvarUsuarios():
    global usuariosDataBase
    global usuariosNovos
    global usuariosCombinados

    for i in usuariosDataBase:
        usuariosCombinados.append(i)
    
    for usuario in usuariosNovos:
        teste = usuario.desserializar()
        usuariosCombinados.append(teste)

    with open('usuarios.csv', 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['Nome', 'Senha', 'Album'])

        for usuario in usuariosCombinados:
            escritor.writerow([usuario['nome'], usuario['senha'], usuario['album']])

    print('Usuários salvos com sucesso!')

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
    global teste2
    global usuariosNovos
    global usuariosDataBase
    global verificandoLogin
    global usuarioLogado

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Menu Principal:\n')
        print('1 - Criar Novo Album')
        print('2 - Acessar meu Album')
        print('0 - Sair\n')
        print(usuariosDataBase)
        print(usuariosNovos)

        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input('Digite seu nome de usuário: ')
            senha = input('Digite sua senha: ')
            novoUsuario = Usuario()  
            novoUsuario.cadastrar(nome, senha)
            usuariosNovos.append(novoUsuario)
            #teste = novoUsuario.getAlbum()
            #teste2 = teste.getFigurinhas()

        elif escolha == '2':
            nome = input('Digite seu nome de usuário: ')
            senha = input('Digite sua senha: ')
            for usuario in usuariosDataBase or usuariosNovos:
                verificandoLogin = usuario.verificarLogin(nome, senha)
                if verificandoLogin is True:
                    usuarioLogado = usuario
                    print('Efetuando o login...')
                    menuSecundario()
                       
        elif escolha == '2':
            menuTerciario()
        elif escolha == '0':
            break
        else:
            input("Opção inválida. Pressione Enter para continuar...")
        
def menuSecundario():
    global usaarioLogado
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Álbum de {usuarioLogado}:\n')
        print('1 - Ver álbum')
        print('2 - Gerenciar coleção')
        print('3 - Abrir pacote de figurinhas')
        print('0 - Voltar para o menu principal\n')
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            # Ver Álbum (Tabela 1 - Opção 1)
            album = usuario.getAlbum()  # Obtém o álbum do usuário
            pagina_atual = 1  # Começa na página 1

            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'Álbum de {nomeUsuarioAtual} - Página {pagina_atual}:\n')

                # Implemente a lógica para mostrar as figurinhas da página atual
                pagina = album.getPaginas()[pagina_atual - 1]
                figurinhas_da_pagina = pagina.getFigurinhas()

                for figurinha in figurinhas_da_pagina:
                    if figurinha.getStatus() == 1:
                        # Figurinha colada
                        print(f"Figurinha {figurinha.getNumero()} - {figurinha.getNome()} (Colada)")
                    elif figurinha.getNumero() in usuario.getFigurinhas():
                        # Figurinha a ser colada
                        print(f"Figurinha {figurinha.getNumero()} - {figurinha.getNome()} (Colar)")
                    else:
                        # Figurinha não possui
                        print(f"Figurinha {figurinha.getNumero()} - {figurinha.getNome()} (Não possui)")

        print('\nOpções:')
        print('1 - Avançar para a próxima página')
        print('2 - Retroceder para a página anterior')
        print('0 - Voltar para o menu anterior\n')

        escolha_pagina = input("Escolha uma opção: ")
        
        if escolha_pagina == '1' and pagina_atual < len(album.getPaginas()):
            pagina_atual += 1
        elif escolha_pagina == '2' and pagina_atual > 1:
            pagina_atual -= 1
        elif escolha_pagina == '0':
            break  # Voltar para o menu anterior

            input("Tarefa 1 concluída. Pressione Enter para continuar...")
        elif escolha == '2':
            # Gerenciar a coleção (Tabela 2 - Opção 1)
            usuario.mostrarColecao()
            input("Tarefa 2 concluída. Pressione Enter para continuar...")
        elif escolha == '3':
            # Implemente a lógica para abrir pacote de figurinhas
            input("Tarefa 3 concluída. Pressione Enter para continuar...")
        elif escolha == '0':
            break  # Voltar para o menu anterior
        else:
            input("Opção inválida. Pressione Enter para continuar...")







            

def menuTerciario():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Menu Opção 2:")
        print("1 - Realizar tarefa 1")
        print("2 - Realizar tarefa 2")
        print("3 - Voltar para o Menu Principal")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            # Implemente a lógica para a tarefa 1
            input("Tarefa 1 concluída. Pressione Enter para continuar...")
        elif escolha == '2':
            # Implemente a lógica para a tarefa 2
            input("Tarefa 2 concluída. Pressione Enter para continuar...")
        elif escolha == '3':
            break  # Voltar para o menu anterior
        else:
            input("Opção inválida. Pressione Enter para continuar...")

def Finalizar():
    print('Iniciando salvamento dos dados...')
    salvarUsuarios()
    print('O programa foi encerrado!')

# Programa principal
if __name__ == '__main__':
    Iniciar()
    Executar()
    Finalizar()


