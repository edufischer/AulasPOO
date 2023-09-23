import csv
import os

usuarios = []

class Usuario:
    def __init__(self):
        self.__nome = ""
        self.__senha = ""
        self.__album = Album()

    def getNomeDeUsuario(self):
        return self.__nome

    def getSenhaDeUsuario(self):
        return self.__senha

    def cadastrar(self, nome, senha):
        self.__nome = nome
        self.__senha = senha

    def verificarLogin(self, nome, senha):
        return self.__nome == nome and self.__senha == senha

    def getAlbum(self):
        return self.__album

    def configurarAlbum(self, album_serializado):
        # Implemente a lógica para configurar o álbum com os dados serializados
        pass    
    
    def serializar(self):
        dados = {
            'nome': self.__nome,
            'senha': self.__senha,
            'album': self.__album.serializar()  # Chama o método serializar do álbum
        }
        return dados

    @classmethod
    def desserializar(cls, dados):
        usuario = cls()
        usuario.cadastrar(dados['nome'], dados['senha'])
        usuario.configurarAlbum(dados['album'])  # Chama o método configurarAlbum para carregar o álbum
        return usuario

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

    def serializar(self):
        dados = {
            'paginas': self.__paginas.serializar(),
            'figurinhas': self.__figurinhas.serializar(),
            'requisicoesTrocas': self.__requisicoesTrocas.serializar()
        }
        return dados

    @classmethod
    def desserializar(cls, dados):
        album = cls()
        album.setPaginas(Pagina.desserializar(dados['paginas']))
        album.setFigurinhas(Figurinha.desserializar(dados['figurinhas']))
        album.setRequisicoesTrocas(Troca.desserializar(dados['requisicoesTrocas']))
        return album

class Figurinha:
    def __init__(self, numero=None, nome=None, conteudo=None, status=0, nroPagina=0):
        self.__numero = numero
        self.__nome = nome
        self.__conteudo = conteudo
        self.__status = status  # 0 = na coleção; 1 = colada no álbum; 2 = disponível para troca
        self.nroPaginas = nroPagina

    def serializar(self):
        dados = {
            'numero': self.__numero,
            'nome': self.__nome,
            'conteudo': self.__conteudo,
            'status': self.__status,
            'nroPagina': self.nroPaginas
        }
        return dados

    @classmethod
    def desserializar(cls, dados):
        return cls(
            numero=dados['numero'],
            nome=dados['nome'],
            conteudo=dados['conteudo'],
            status=dados['status'],
            nroPagina=dados['nroPagina']
        )

class Pagina:
    def __init__(self):
        self.figurinhas = Figurinha()
        self.titulo = 0
        self.minNro = 1
        self.maxNro = 133

    def serializar(self):
        dados = {
            'figurinhas': self.figurinhas.serializar(),
            'titulo': self.titulo,
            'minNro': self.minNro,
            'maxNro': self.maxNro
        }
        return dados

    @classmethod
    def desserializar(cls, dados):
        return cls(
            figurinhas=Figurinha.desserializar(dados['figurinhas']),
            titulo=dados['titulo'],
            minNro=dados['minNro'],
            maxNro=dados['maxNro']
        )

class Troca:
    def __init__(self, nomeProponente=None, figurinhaRequerida=None, figurinhaDisponivel=None, status=None):
        self.__nomeProponente = nomeProponente
        self.__figurinhaRequerida = figurinhaRequerida
        self.__figurinhaDisponivel = figurinhaDisponivel
        self.__status = status  # 0 = aguardando; 1 (aceita); 2(recusada)

    def aceitar(self, bool):
        pass

    def serializar(self):
        dados = {
            'nomeProponente': self.__nomeProponente,
            'figurinhaRequerida': self.__figurinhaRequerida.serializar() if self.__figurinhaRequerida else None,
            'figurinhaDisponivel': self.__figurinhaDisponivel.serializar() if self.__figurinhaDisponivel else None,
            'status': self.__status
        }
        return dados

    @classmethod
    def desserializar(cls, dados):
        figurinhaRequerida = Figurinha.desserializar(dados['figurinhaRequerida']) if dados['figurinhaRequerida'] else None
        figurinhaDisponivel = Figurinha.desserializar(dados['figurinhaDisponivel']) if dados['figurinhaDisponivel'] else None
        return cls(
            nomeProponente=dados['nomeProponente'],
            figurinhaRequerida=figurinhaRequerida,
            figurinhaDisponivel=figurinhaDisponivel,
            status=dados['status']
        )









def carregarUsuarios():
    global usuarios
    try:
        with open('usuarios.csv', 'r') as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)
            for linha in leitor:
                nome = linha['Nome']
                senha = linha['Senha']
                # Supondo que você tenha implementado o método de desserialização
                album_serializado = linha['Album']
                usuario = Usuario()
                usuario.cadastrar(nome, senha)
                usuario.configurarAlbum(album_serializado)
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
            albumUsuarioSerializado = usuario.getAlbum().serializar()
            escritor.writerow([nomeUsuario, senhaUsuario, albumUsuarioSerializado])
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
        print('0 - Sair\n')
        
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
        print(f'Álbum de {nomeUsuarioAtual}:\n')
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
