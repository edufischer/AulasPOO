import csv
import random
import os


from Usuario import Usuario
from Album import Album

usuarios = []
figurinhas = []
trocas = []
usuarioEstaLogado = False

def carregarUsuarios():
    global usuarios
    with open('usuarios.csv', 'r') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        next(leitor)  # Pular a primeira linha (cabeçalho)
        for linha in leitor:
            if len(linha) >= 3:  # Verifica se há pelo menos 3 valores na linha
                nome, senha, album = linha
                usuarios.append(Usuario(nome, senha, album))  # Passar o 'album' para o construtor do Usuario
    return usuarios

def carregarFigurinhas():

# Abra o arquivo CSV em modo de leitura
    with open('figurinhas.csv', mode='r') as arquivo_csv:
        # Crie um objeto leitor CSV
        figurinhas = csv.reader(arquivo_csv)
    
        # Itere pelas linhas do arquivo
        for linha in figurinhas:
         print(linha[0])
    
    figurinhas.close()



# Função principal


#            if usuario_logado:
#                while True:
#                    opcao_album = menu_album()
#                    if opcao_album == '1':
#                        ver_album(usuario_logado.album)
#                    #elif opcao_album == '2':
#                    #    gerenciar_colecao(usuario_logado)
#                    #elif opcao_album == '3':
#                    #    abrir_pacote(usuario_logado)
#                    elif opcao_album == '4':
#                        break
#                    else:
#                        print("Opção inválida.")
#
#        elif opcao == '3':
#            salvar_usuarios(usuarios)
#            salvar_figurinhas(figurinhas)
#            salvar_trocas(trocas)
#            break
#        else:
#            print("Opção inválida.")



# Menu do Programa

def Iniciar():
    print()
    print('Iniciando o programa...\n')
    print('Carregando o programa...\n')
    carregarUsuarios()
    #carregar_figurinhas()
    #carregar_trocas()

def executarMenuPrincipal():
    print()
    print('1 - Criar Novo Album')
    print('2 - Acessar meu Album')
    print('0 -Sair\n')

    resposta = input('Escolha uma opção: ')
    os.system('cls'if os.name== 'nt'else'clear')

    return resposta

def executarMenuSecundario():
    print()
    print('1 - Ver album')
    print('2 - Gerenciar colecao')
    print('3 - Abrir pacote figurinhas')
    print('0 -Sair\n')

    resposta = input('Escolha uma opção: ')
    os.system('cls'if os.name== 'nt'else'clear')

    return resposta

def Executar():
    ExecucaoEmAndamento = True
    global usuarioEstaLogado 
    global usuario

    if usuarioEstaLogado == False:
        while ExecucaoEmAndamento is True:
            acaoUsuario = executarMenuPrincipal()
            if acaoUsuario == '1':
                nome = input('Digite seu nome de usuário: ')
                senha = input('Digite sua senha: ')
                novoUsuario = Usuario()  
                cadastrarUsuario = novoUsuario.cadastrar(nome, senha)
                usuarios.append(cadastrarUsuario)
        
            # Itere pela lista de usuários e acesse o nome de usuário usando o método getInfo
                for usuario in usuarios:
                    nome_de_usuario = usuario.getNomeDeUsuario()
                    print(f"Nome de usuário: {str(nome_de_usuario)}")

            #elif acaoUsuario == '2':
            #    nome = input('Digite seu nome de usuário: ')
            #    senha = input('Digite sua senha: ')
            #    for usuario in usuarios:
            #        if usuario.verificarLogin(nome, senha) is True: 
            #            usuarioLogado = usuario.getAlbum() 
            #            usuarioEstaLogado = True
            #            print(usuarioLogado)
            #            ExecucaoEmAndamento = False
            #            print(usuarios)
            #            
            #    else:
            #        print('Usuário não encontrado ou senha incorreta')

            elif (acaoUsuario == '0'):
                ExecucaoEmAndamento = False #terminarExecucao é falso, logo vai sair do loop no proximo giro.

            else:
                print('Escolha invalida! Tente de novo.')

    elif usuarioEstaLogado == True: Executar2()

def Executar2():
    ExecucaoEmAndamento = True
    global usuarioEstaLogado 

    if usuarioEstaLogado == False:
        while ExecucaoEmAndamento is True:
            acaoUsuario = executarMenuSecundario()

            if acaoUsuario == '1':
                nome = input('Digite seu nome de usuário: ')
                senha = input('Digite sua senha: ')
                novoUsuario = Usuario()  
                cadastrarUsuario = novoUsuario.cadastrar(nome, senha)
                usuarios.append(cadastrarUsuario)

            elif (acaoUsuario == '0'):
                ExecucaoEmAndamento = False #terminarExecucao é falso, logo vai sair do loop no proximo giro.

            else:
                print('Escolha invalida! Tente de novo.')

def salvarUsuarios(usuarios):
    
        with open('usuarios.csv', 'w', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Nome', 'Senha', 'Album'])
        
            for usuario in usuarios:
                print(usuario)
                print('LISTA: ',usuarios)
                escritor.writerow([usuario.getNomeDeUsuario, usuario.getSenhaDeUsuario, usuario.getAlbum])


def Finalizar():
    print('Inicilizando salvamento dos dados...!')
    # Função para salvar dados nos arquivos CSV
    global usuarios
    salvarUsuarios(usuarios)
    print('O programa foi encerrado!')

# Programa principal
if __name__ == '__main__':
    Iniciar()
    Executar()
    Finalizar()


