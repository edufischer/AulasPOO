import csv
import os

usuarios = []



class Usuario:
    def __init__ (self):
        self.__nome = Usuario.getNomeDeUsuario
        self.__senha = Usuario.getSenhaDeUsuario
        self.__album = Album()

    def getNomeDeUsuario(self):
        return self.__nome
    
    def getSenhaDeUsuario(self):
        return self.__senha
    
    def cadastrar(self, nome, senha):
        self.__nome = nome
        self.__senha = senha
    
    def verificarLogin(self, nome, senha):
       if self.__nome == nome and self.__senha == senha:
           return True
       else: return False

    def getAlbum (self):
        return self.__album

class Album:
    def __init__(self):
        self.__paginas = Pagina()
        self.__figurinhas = Figurinha()
        self.__requisicoesTrocas = Troca()

    def getPaginas(self):
        return self.__paginas
    
    def getFigurinhas(self):
        return self.__figurinhas
    
    def getRequisicoesTrocas(self):
        return self.__requisicoesTrocas

    def setPaginas(self, paginas):
        self.__paginas = paginas
    
    def setFigurinhas(self, figurinhas):
        self.__figurinhas = figurinhas
    
    def setRequisicoesTrocas(self, requisicoesTrocas):
        self.__requisicoesTrocas = requisicoesTrocas
    

class Figurinha:
    def __init__(self, numero=None, nome=None, conteudo=None, status=0, nroPagina=0):
        self.__numero = numero
        self.__nome = nome
        self.__conteudo = conteudo
        # 0 = na coleção; 1 = colada no álbum; 2 = disponível para troca
        self.__status = status
        self.nroPaginas = nroPagina

class Pagina:
    def __init__(self):
        self.figurinhas = Figurinha()
        self.titulo = 0
        self.minNro = 1
        self.maxNro = 133

class Troca:
    def __init__(self, nomeProponente=None, figurinhaRequerida=None, figurinhaDisponivel=None, status=None):
        self.__nomeProponente = nomeProponente
        self.__figurinhaRequerida = figurinhaRequerida
        self.__figurinhaDisponivel = figurinhaDisponivel
        # 0 = aguardando; 1 (aceita); 2(recusada)
        self.__status = status

    def aceitar(bool):
        pass


########################################################################################################################


def carregarUsuarios():
    global usuarios
    try:
        with open('usuarios.csv', 'r') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                nome = linha['Nome']
                senha = linha['Senha']
                # Supondo que você tenha implementado o método de desserialização
                album_serializado = linha['Album']
                usuario = Usuario()
                usuario.cadastrar(nome, senha)
                usuarios.append(usuario)
        print('Usuários carregados com sucesso!')
    except FileNotFoundError:
        print('Arquivo de usuários não encontrado. Criando novo arquivo...')

def salvarUsuarios():
    global usuarios
    with open('usuarios.csv', 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['Nome', 'Senha', 'Album'])

        for usuario in usuarios:
            nomeUsuario = usuario.getNomeDeUsuario()
            senhaUsuario = usuario.getSenhaDeUsuario()
            albumUsuario = usuario.getAlbum()
            escritor.writerow([nomeUsuario, senhaUsuario, albumUsuario])
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


