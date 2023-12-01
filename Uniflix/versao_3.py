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

class Perfil:
    def __init__(self, nome, usuário, catálogo):
        self.nome = nome
        self.usuário = usuário
        self.catálogo = catálogo

    def exibir_informacoes(self):
        print(f"Perfil: {self.nome}")
        self.usuário.exibir_informacoes()

def criar_novo_perfil():
    nome_perfil = input("Nome do Perfil: ")
    nome_usuario = input("Nome do Usuário: ")
    senha_usuario = input("Senha do Usuário: ")
    tipo_assinatura = input("Tipo de Assinatura: ")

    usuário = Usuário(nome_usuario, senha_usuario, tipo_assinatura)
    catálogo = Catálogo()

    novo_perfil = Perfil(nome_perfil, usuário, catálogo)
    return novo_perfil

def carregar_perfis():
    perfis = []

    with open('perfis.csv', mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Pular a linha do cabeçalho
        for row in reader:
            nome_perfil = row[0]
            nome_usuario = row[1]
            senha_usuario = row[2]
            tipo_assinatura = row[3]

            usuário = Usuário(nome_usuario, senha_usuario, tipo_assinatura)
            catálogo = carregar_catalogo()
            
            perfil = Perfil(nome_perfil, usuário, catálogo)
            perfis.append(perfil)

    return perfis

def salvar_perfis(perfis):
    with open('perfis.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Nome Perfil", "Nome Usuário", "Senha Usuário", "Tipo Assinatura"])

        for perfil in perfis:
            writer.writerow([perfil.nome, perfil.usuário.nome, perfil.usuário.senha, perfil.usuário.tipo_assinatura])

def escolher_perfil(perfis):
    if not perfis:
        print("Não há perfis disponíveis. Crie um novo perfil.")
        return None

    print("\nEscolher Perfil:")
    for i, perfil in enumerate(perfis, start=1):
        print(f"{i} - {perfil.nome}")

    try:
        escolha = int(input("Escolha o número do perfil: "))
        if 1 <= escolha <= len(perfis):
            perfil_escolhido = perfis[escolha - 1]
            print(f"Perfil escolhido: {perfil_escolhido.nome}")
            return perfil_escolhido
        else:
            print("Escolha inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Informe um número.")

    return None

def menu_perfis(perfis):
    perfil_atual = escolher_perfil(perfis)

    if perfil_atual is None:
        print("Criando novo perfil...")
        novo_perfil = criar_novo_perfil()
        perfis.append(novo_perfil)
        perfil_atual = novo_perfil

    while True:
        print("\nMenu Perfis:")
        print("1 - Escolher Perfil")
        print("2 - Criar Novo Perfil")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            perfil_atual = escolher_perfil(perfis)
        elif opcao == "2":
            novo_perfil = criar_novo_perfil()
            perfis.append(novo_perfil)
            perfil_atual = novo_perfil
        elif opcao == "3":
            print("Saindo do Menu Perfis.")
            break
        else:
            print("Opção inválida. Tente novamente.")

        if perfil_atual is not None:
            menu_conta_usuario_logado(perfil_atual, perfil_atual.catálogo)

    salvar_perfis(perfis)

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
                if len(row) > 5 and ":" in row[5]:
                    estúdio = row[5].split(": ")[1]
                else:
                    estúdio = ""
                catalogo.adicionar_midia(Animação(título, gênero, ano_lançamento, classificação, estúdio))
            elif tipo == "ProgramaTV":
                if len(row) > 5 and ":" in row[5]:
                    num_episodios = int(row[5].split(": ")[1])
                else:
                    num_episodios = 0
                lista_episodios = []  # Implemente a leitura da lista de episódios do arquivo CSV aqui
                catalogo.adicionar_midia(ProgramaTV(título, gênero, ano_lançamento, classificação, num_episodios, lista_episodios))

    return catalogo

def menu_conta_usuario_logado(perfil, catalogo):
    while True:
        print("\nMenu Conta do Usuário Logado:")
        print("1 - Exibir Informações do Perfil")
        print("2 - Exibir Catálogo")
        print("3 - Buscar Mídia por Título")
        print("4 - Adicionar Episódio a Série")
        print("5 - Listar Catálogo")
        print("6 - Salvar Catálogo")
        print("7 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            perfil.exibir_informacoes()
        elif opcao == "2":
            catalogo.listar_catalogo()
        elif opcao == "3":
            título = input("Digite o título da mídia: ")
            mídia_encontrada = catalogo.buscar_por_titulo(título)
            if mídia_encontrada:
                mídia_encontrada.exibir_informacoes()
            else:
                print("Mídia não encontrada.")
        elif opcao == "4":
            # Implemente a lógica para adicionar episódio a série aqui
            pass
        elif opcao == "5":
            catalogo.listar_catalogo()
        elif opcao == "6":
            catalogo.salvar_catalogo()
        elif opcao == "7":
            print("Voltando ao Menu Perfis.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    perfis = carregar_perfis()
    menu_perfis(perfis)

