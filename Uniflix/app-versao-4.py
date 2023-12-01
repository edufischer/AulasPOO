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
    def __init__(self, título, gênero, ano_lançamento, classificação, num_episódios, lista_episodios):
        super().__init__("ProgramaTV", título, gênero, ano_lançamento, classificação)
        self.num_episódios = num_episódios
        self.lista_episódios = lista_episódios

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Número de Episódios: {self.num_episódios}")

    def listar_episódios(self):
        print("Lista de Episódios:")
        for episódio in self.lista_episódios:
            print(episódio)

class Catálogo:
    def __init__(self):
        self.lista_séries = []
        self.lista_filmes = []
        self.lista_documentários = []
        self.lista_animações = []
        self.lista_programas_tv = []

    def adicionar_mídia(self, mídia):
        if isinstance(mídia, Série):
            self.lista_séries.append(mídia)
        elif isinstance(mídia, Filme):
            self.lista_filmes.append(mídia)
        elif isinstance(mídia, Documentário):
            self.lista_documentários.append(mídia)
        elif isinstance(mídia, Animação):
            self.lista_animações.append(mídia)
        elif isinstance(mídia, ProgramaTV):
            self.lista_programas_tv.append(mídia)

    def obter_lista(self, tipo):
        if tipo == "Série":
            return self.lista_séries
        elif tipo == "Filme":
            return self.lista_filmes
        elif tipo == "Documentário":
            return self.lista_documentários
        elif tipo == "Animação":
            return self.lista_animações
        elif tipo == "ProgramaTV":
            return self.lista_programas_tv

    def buscar_por_título(self, título):
        for tipo in ["Série", "Filme", "Documentário", "Animação", "ProgramaTV"]:
            lista = self.obter_lista(tipo)
            for mídia in lista:
                if mídia.título.lower() == título.lower():
                    return mídia
        return None

    def adicionar_episódio(self, série, temporada, episódio):
        if série in self.lista_séries and temporada in série.episódios_por_temporada:
            série.episódios_por_temporada[temporada].append(episódio)
            return True
        return False

    def listar_catálogo(self):
        print("Catálogo de Mídias:")
        for tipo in ["Série", "Filme", "Documentário", "Animação", "ProgramaTV"]:
            lista = self.obter_lista(tipo)
            print(f"\n--- {tipo}s ---")
            for mídia in lista:
                print(mídia.título)

    def salvar_catálogo(self):
        with open('catálogo.csv', mode='w', newline='', encoding='utf-8') as file:
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
                                         mídia.classificação, f"Número de Episódios: {mídia.num_episódios}"])

class Usuário:
    def __init__(self, nome, senha, tipo_assinatura):
        self.nome = nome
        self.senha = senha
        self.tipo_assinatura = tipo_assinatura

    def exibir_informações(self):
        print(f"Nome: {self.nome}")
        print(f"Tipo de Assinatura: {self.tipo_assinatura}")

class Perfil:
    def __init__(self, nome, usuário, catálogo):
        self.nome = nome
        self.usuário = usuário
        self.catálogo = catálogo

    def exibir_informações(self):
        print(f"Perfil: {self.nome}")
        self.usuário.exibir_informações()

def criar_novo_perfil():
    nome_perfil = input("Nome do Perfil: ")
    nome_usuario = input("Nome do Usuário: ")
    senha_usuario = input("Senha do Usuário: ")
    tipo_assinatura = input("Tipo de Assinatura: ")

    usuário = Usuário(nome_usuario, senha_usuario, tipo_assinatura)
    catálogo = Catálogo()

    novo_perfil = Perfil(nome_perfil, usuário, catálogo)
    return novo_perfil

def carregar_usuários():
    usuários = []

    with open('usuarios.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Pular a linha do cabeçalho
        for row in reader:
            nome = row[0]
            senha = row[1]
            tipo_assinatura = row[2]

            usuário = Usuário(nome, senha, tipo_assinatura)
            usuários.append(usuário)

    return usuários

def carregar_perfis():
    perfis = []

    with open('perfis.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Pular a linha do cabeçalho
        for row in reader:
            nome_perfil = row[0]
            nome_usuario = row[1]

            # Encontrar o usuário correspondente
            usuário = next((u for u in usuários if u.nome == nome_usuario), None)

            if usuário:
                perfil = Perfil(nome_perfil, usuário, Catálogo())
                perfis.append(perfil)

    return perfis

def salvar_perfis(perfis):
    with open('perfis.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Nome Perfil", "Nome Usuário"])

        for perfil in perfis:
            writer.writerow([perfil.nome, perfil.usuário.nome])

# Carregar usuários existentes
usuários = carregar_usuários()

# Carregar perfis existentes
perfis_existentes = carregar_perfis()

# Criar perfis para os usuários fornecidos
for usuario in usuários:
    # Verificar se o perfil já existe
    perfil_existente = next((p for p in perfis_existentes if p.usuário.nome == usuario.nome), None)
    if not perfil_existente:
        # Criar um novo perfil para o usuário
        novo_perfil = criar_novo_perfil()
        novo_perfil.usuário = usuario  # Associar o usuário ao perfil
        perfis_existentes.append(novo_perfil)

# Salvar os perfis atualizados
salvar_perfis(perfis_existentes)
