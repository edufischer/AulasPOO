import csv

class Mídia:
    def __init__(self, tipo, título, gênero, ano_lançamento, classificação):
        self.tipo = tipo
        self.título = título
        self.gênero = gênero
        self.ano_lançamento = ano_lançamento
        self.classificação = classificação

    def exibir_informacoes(self):
        print(f"Tipo: {self.tipo}")
        print(f"Título: {self.título}")
        print(f"Gênero: {self.gênero}")
        print(f"Ano de Lançamento: {self.ano_lançamento}")
        print(f"Classificação: {self.classificação}")

class Série(Mídia):
    def __init__(self, título, gênero, ano_lançamento, classificação, num_temporadas, episodios_por_temporada):
        super().__init__("Série", título, gênero, ano_lançamento, classificação)
        self.num_temporadas = num_temporadas
        self.episodios_por_temporada = episodios_por_temporada

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Número de Temporadas: {self.num_temporadas}")

    def listar_episodios(self, nro_temporada):
        if nro_temporada in self.episodios_por_temporada:
            print(f"Episódios da Temporada {nro_temporada}:")
            for episodio in self.episodios_por_temporada[nro_temporada]:
                print(episodio)
        else:
            print(f"Temporada {nro_temporada} não encontrada.")

class Filme(Mídia):
    def __init__(self, título, gênero, ano_lançamento, classificação, diretor, produtor):
        super().__init__("Filme", título, gênero, ano_lançamento, classificação)
        self.diretor = diretor
        self.produtor = produtor

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Diretor(a): {self.diretor}")
        print(f"Produtor(a): {self.produtor}")

class Documentário(Mídia):
    def __init__(self, título, gênero, ano_lançamento, classificação, tema):
        super().__init__("Documentário", título, gênero, ano_lançamento, classificação)
        self.tema = tema

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Tema: {self.tema}")

class Animação(Mídia):
    def __init__(self, título, gênero, ano_lançamento, classificação, estúdio):
        super().__init__("Animação", título, gênero, ano_lançamento, classificação)
        self.estúdio = estúdio

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Estúdio: {self.estúdio}")

class ProgramaTV(Mídia):
    def __init__(self, título, gênero, ano_lançamento, classificação, num_episodios, lista_episodios):
        super().__init__("ProgramaTV", título, gênero, ano_lançamento, classificação)
        self.num_episodios = num_episodios
        self.lista_episodios = lista_episodios

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Número de Episódios: {self.num_episodios}")

    def listar_episodios(self):
        print("Lista de Episódios:")
        for episodio in self.lista_episodios:
            print(episodio)

class Catálogo:
    def __init__(self):
        self.lista_series = []
        self.lista_filmes = []
        self.lista_documentarios = []
        self.lista_animacoes = []
        self.lista_programas_tv = []

    def adicionar_midia(self, mídia):
        if isinstance(mídia, Série):
            self.lista_series.append(mídia)
        elif isinstance(mídia, Filme):
            self.lista_filmes.append(mídia)
        elif isinstance(mídia, Documentário):
            self.lista_documentarios.append(mídia)
        elif isinstance(mídia, Animação):
            self.lista_animacoes.append(mídia)
        elif isinstance(mídia, ProgramaTV):
            self.lista_programas_tv.append(mídia)

    def obter_lista(self, tipo):
        if tipo == "Série":
            return self.lista_series
        elif tipo == "Filme":
            return self.lista_filmes
        elif tipo == "Documentário":
            return self.lista_documentarios
        elif tipo == "Animação":
            return self.lista_animacoes
        elif tipo == "ProgramaTV":
            return self.lista_programas_tv
        
    def buscar_por_titulo(self, titulo):
        for tipo in ["Série", "Filme", "Documentário", "Animação", "ProgramaTV"]:
            lista = self.obter_lista(tipo)
            for mídia in lista:
                if mídia.título.lower() == titulo.lower():
                    return mídia
        return None
    
    def adicionar_episodio(self, série, temporada, episodio):
        if série in self.lista_series and temporada in série.episodios_por_temporada:
            série.episodios_por_temporada[temporada].append(episodio)
            return True
        return False
    
    def listar_catalogo(self):
        print("Catálogo de Mídias:")
        for tipo in ["Série", "Filme", "Documentário", "Animação", "ProgramaTV"]:
            lista = self.obter_lista(tipo)
            print(f"\n--- {tipo}s ---")
            for mídia in lista:
                print(mídia.título)
        
    def salvar_catalogo(self):
        with open('catalogo.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Tipo", "Título", "Gênero", "Ano de Lançamento", "Classificação", "Informações Adicionais"])
            
            for tipo in ["Série", "Filme", "Documentário", "Animação", "ProgramaTV"]:
                lista = self.obter_lista(tipo)
                for mídia in lista:
                    if tipo == "Série":
                        writer.writerow([tipo, mídia.título, mídia.gênero, mídia.ano_lançamento,
                                         mídia.classificação, f"Temporadas: {mídia.num_temporadas}"])
                    elif tipo == "Filme":
                        writer.writerow([tipo, mídia.título, mídia.gênero, mídia.ano_lançamento,
                                         mídia.classificação, f"Diretor: {mídia.diretor}, Produtor: {mídia.produtor}"])
                    elif tipo == "Documentário":
                        writer.writerow([tipo, mídia.título, mídia.gênero, mídia.ano_lançamento,
                                         mídia.classificação, f"Tema: {mídia.tema}"])
                    elif tipo == "Animação":
                        writer.writerow([tipo, mídia.título, mídia.gênero, mídia.ano_lançamento,
                                         mídia.classificação, f"Estúdio: {mídia.estúdio}"])
                    elif tipo == "ProgramaTV":
                        writer.writerow([tipo, mídia.título, mídia.gênero, mídia.ano_lançamento,
                                         mídia.classificação, f"Número de Episódios: {mídia.num_episodios}"])

class Usuário:
    def __init__(self, nome, senha, tipo_assinatura):
        self.nome = nome
        self.senha = senha
        self.tipo_assinatura = tipo_assinatura

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Tipo de Assinatura: {self.tipo_assinatura}")

def carregar_catalogo():
    catalogo = Catálogo()

    with open('catalogo.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Pular a linha do cabeçalho
        for row in reader:
            tipo = row[0]
            título = row[1]
            gênero = row[2]
            ano_lançamento = row[3]
            classificação = row[4]

            if tipo == "Série":
                num_temporadas = int(row[5].split(": ")[1])
                catalogo.adicionar_midia(Série(título, gênero, ano_lançamento, classificação, num_temporadas, {}))
            elif tipo == "Filme":
                if len(row) > 5 and ":" in row[5]:
                    diretor_produtor = row[5].split(": ")[1].split(", ")
                    if len(diretor_produtor) == 2:
                        diretor, produtor = diretor_produtor
                    else:
                        diretor, produtor = diretor_produtor[0], ""
                else:
                    diretor, produtor = "", ""
                catalogo.adicionar_midia(Filme(título, gênero, ano_lançamento, classificação, diretor, produtor))
            elif tipo == "Documentário":
                if len(row) > 5 and ":" in row[5]:
                    tema = row[5].split(": ")[1]
                else:
                    tema = ""
                catalogo.adicionar_midia(Documentário(título, gênero, ano_lançamento, classificação, tema))
            elif tipo == "Animação":
                estúdio = row[5].split(": ")[1]
                catalogo.adicionar_midia(Animação(título, gênero, ano_lançamento, classificação, estúdio))
            elif tipo == "ProgramaTV":
                num_episodios = int(row[5].split(": ")[1])
                catalogo.adicionar_midia(ProgramaTV(título, gênero, ano_lançamento, classificação, num_episodios, []))

    return catalogo

def salvar_usuarios(usuarios):
    with open('usuarios.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Senha", "Tipo de Assinatura"])

        for usuario in usuarios:
            writer.writerow([usuario.nome, usuario.senha, usuario.tipo_assinatura])

def carregar_usuarios():
    usuarios = []

    with open('usuarios.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Pular a linha do cabeçalho
        for row in reader:
            nome = row[0]
            senha = row[1]
            tipo_assinatura = row[2]
            usuarios.append(Usuário(nome, senha, tipo_assinatura))

    return usuarios

def menu_principal():
    print("Bem-vindo ao Catálogo de Mídias!")
    catalogo = carregar_catalogo()
    usuarios = carregar_usuarios()
    usuario_atual = None

    
    if usuario_atual is None:
            usuario_atual = fazer_login_ou_cadastrar(usuarios)
        

    while True:
        print("\nMenu Principal:")
        print("1 - Pesquisar Mídia")
        print("2 - Catálogo de Mídias")
        print("3 - Conta do Usuário")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            pesquisar_midia(catalogo)
        elif opcao == "2":
            catalogo.listar_catalogo()
        elif opcao == "3":
            conta_usuario = menu_conta_usuario(usuarios)
            if conta_usuario is not None:
                menu_conta_usuario_logado(conta_usuario, catalogo)
        elif opcao == "0":
            print("Obrigado por usar o Catálogo de Mídias. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def fazer_login_ou_cadastrar(usuarios):
    while True:
        print("\nAutenticação do Usuário:")
        print("1 - Fazer Login")
        print("2 - Criar Nova Conta")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario = fazer_login(usuarios)
            if usuario is not None:
                return usuario
        elif opcao == "2":
            criar_nova_conta(usuarios)
        elif opcao == "0":
            print("Saindo do programa. Até mais!")
            exit()
        else:
            print("Opção inválida. Tente novamente.")


def pesquisar_midia(catalogo):
    titulo_pesquisa = input("Digite o título da mídia que deseja pesquisar: ")
    mídia_encontrada = catalogo.buscar_por_titulo(titulo_pesquisa)

    if mídia_encontrada is not None:
        mídia_encontrada.exibir_informacoes()
    else:
        print("Mídia não encontrada.")

def menu_conta_usuario(usuarios):
    while True:
        print("\nMenu de Conta de Usuário:")
        print("1 - Criar Nova Conta")
        print("2 - Fazer Login")
        print("0 - Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_nova_conta(usuarios)
        elif opcao == "2":
            usuario = fazer_login(usuarios)
            if usuario is not None:
                return usuario
        elif opcao == "0":
            print("Voltando ao Menu Principal.")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_conta_usuario_logado(usuario, catalogo):
    while True:
        print("\nMenu da Conta do Usuário:")
        print("1 - Ver Informações da Conta")
        print("2 - Editar Informações da Conta")
        print("3 - Pesquisar Mídia")
        print("4 - Catálogo de Mídias")
        print("5 - Sair da Conta")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario.exibir_informacoes()
        elif opcao == "2":
            editar_informacoes_conta(usuario)
        elif opcao == "3":
            pesquisar_midia(catalogo)
        elif opcao == "4":
            catalogo.listar_catalogo()
        elif opcao == "5":
            print("Saindo da conta. Retornando ao Menu Principal.")
            break
        elif opcao == "0":
            print("Obrigado por usar o Catálogo de Mídias. Até mais!")
            exit()
        else:
            print("Opção inválida. Tente novamente.")


def editar_informacoes_conta(usuario):
    print("Editar Informações da Conta:")
    novo_nome = input("Novo Nome (deixe em branco para manter o atual): ")
    novo_senha = input("Nova Senha (deixe em branco para manter a atual): ")
    novo_tipo_assinatura = input("Novo Tipo de Assinatura (deixe em branco para manter o atual): ")

    if novo_nome:
        usuario.nome = novo_nome
    if novo_senha:
        usuario.senha = novo_senha
    if novo_tipo_assinatura:
        usuario.tipo_assinatura = novo_tipo_assinatura

    print("Informações da conta atualizadas com sucesso!")


def menu_conta_usuario(usuarios):
    while True:
        print("\nMenu de Conta de Usuário:")
        print("1 - Criar Nova Conta")
        print("2 - Fazer Login")
        print("0 - Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_nova_conta(usuarios)
        elif opcao == "2":
            usuario = fazer_login(usuarios)
            if usuario is not None:
                return usuario
        elif opcao == "0":
            print("Voltando ao Menu Principal.")
            break
        else:
            print("Opção inválida. Tente novamente.")


def criar_nova_conta(usuarios):
    print("Criar Nova Conta:")
    nome = input("Nome: ")
    senha = input("Senha: ")
    tipo_assinatura = input("Tipo de Assinatura: ")

    novo_usuario = Usuário(nome, senha, tipo_assinatura)
    usuarios.append(novo_usuario)

    print("Nova conta criada com sucesso!")


def fazer_login(usuarios):
    print("Fazer Login:")
    nome = input("Nome: ")
    senha = input("Senha: ")

    for usuario in usuarios:
        if usuario.nome == nome and usuario.senha == senha:
            print(f"Login bem-sucedido! Bem-vindo, {usuario.nome}.")
            return usuario

    print("Nome de usuário ou senha incorretos. Tente novamente.")
    return None

if __name__ == "__main__":
    menu_principal()
       
