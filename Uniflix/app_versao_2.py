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
            print(f"Episódio {episodio} adicionado à série {série.título}, temporada {temporada}.")
        else:
            print(f"Erro: Série {série.título} ou temporada {temporada} não encontrada.")

class Perfil:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.favoritos = []
        self.ultimos_assistidos = []

    def exibir_tela_inicial(self, catalogo):
        print(f"\nBem-vindo, {self.nome}!")
        print("1 - Listar Mídia")
        print("2 - Favoritos")
        print("3 - Últimos Assistidos")
        print("4 - Sair para Tela Inicial")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_listar_midia(self, catalogo)
        elif opcao == "2":
            self.listar_favoritos()
        elif opcao == "3":
            self.listar_ultimos_assistidos()
        elif opcao == "4":
            return
        elif opcao == "0":
            exit()
        else:
            print("Opção inválida.")
    
    def editar_perfil(perfil):
        print("\nEditar Perfil")
        print("1 - Alterar Senha")
        print("2 - Alterar Plano de Assinatura")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nova_senha = input("Digite a nova senha: ")
            perfil.alterar_senha(nova_senha)
        elif opcao == "2":
            novo_plano = input("Digite o novo tipo de assinatura (Simples/Premium): ").capitalize()
            perfil.alterar_plano(novo_plano)
        elif opcao == "0":
            return
        else:
            print("Opção inválida.")

    def adicionar_favorito(self, mídia):
        if len(self.favoritos) < 10:
            if mídia not in self.favoritos:
                self.favoritos.append(mídia)
        else:
            # Remover o primeiro favorito para adicionar o novo
            self.favoritos.pop(0)
            self.favoritos.append(mídia)

    def remover_favorito(self, mídia):
        if mídia in self.favoritos:
            self.favoritos.remove(mídia)

    def adicionar_ultimo_assistido(self, mídia):
        if len(self.ultimos_assistidos) < 10:
            if mídia in self.ultimos_assistidos:
                self.ultimos_assistidos.remove(mídia)
            self.ultimos_assistidos.append(mídia)
        else:
            # Remover o primeiro assistido para adicionar o novo
            self.ultimos_assistidos.pop(0)
            self.ultimos_assistidos.append(mídia)

    def listar_midias_apropriadas(self, tipo, catalogo):
        midias_apropriadas = []
        for midia in catalogo.obter_lista(tipo):
            if midia.classificação == "18 anos" or int(midia.classificação.split()[0]) <= self.idade:
                midias_apropriadas.append(midia)
        return midias_apropriadas

    def assistir(self, midia):
        self.ultimos_assistidos.append(midia)
        print(f"Assistindo {midia.título}...")

    def favoritar(self, midia, favoritar):
        if favoritar:
            self.favoritos.append(midia)
            print(f"{midia.título} foi adicionado aos favoritos.")
        else:
            if midia in self.favoritos:
                self.favoritos.remove(midia)
                print(f"{midia.título} foi removido dos favoritos.")
            else:
                print(f"{midia.título} não está nos favoritos.")

    def buscar_por_titulo(self, titulo, catalogo):
        midia_encontrada = None
        for tipo in ["Série", "Filme", "Documentário", "Animação", "ProgramaTV"]:
            lista_midias = catalogo.obter_lista(tipo)
            for midia in lista_midias:
                if midia.título.lower() == titulo.lower():
                    midia_encontrada = midia
                    break
        return midia_encontrada
    
    def listar_favoritos(self):
        if not self.favoritos:
            print("Nenhum favorito encontrado.")
        else:
            print("Favoritos:")
            for midia in self.favoritos:
                midia.exibir_informacoes()

    def listar_ultimos_assistidos(self):
        if not self.ultimos_assistidos:
            print("Nenhum último assistido encontrado.")
        else:
            print("Últimos Assistidos:")
            for midia in self.ultimos_assistidos:
                midia.exibir_informacoes()

#    def listar_favoritos(self):
#    if not self.favoritos:
#        print("Nenhum favorito encontrado.")
#    else:
#        print("Favoritos:")
#        for midia in self.favoritos:
#            midia.exibir_informacoes()


class Usuário:
    def __init__(self, nome, senha, tipo_assinatura):
        self.nome = nome
        self.senha = senha
        self.tipo_assinatura = tipo_assinatura
        self.perfis = []

    def adicionar_perfil(self, nome, idade):
        if len(self.perfis) < self.limite_perfis():
            perfil = Perfil(nome, idade)
            self.perfis.append(perfil)
        else:
            print("Limite de perfis atingido para este tipo de assinatura.")

    def remover_perfil(self, nome):
        perfil = next((p for p in self.perfis if p.nome == nome), None)
        if perfil:
            self.perfis.remove(perfil)
        else:
            print("Perfil não encontrado.")

    def limite_perfis(self):
        return 3 if self.tipo_assinatura == "Simples" else 5

    def alterar_senha(self, nova_senha):
        self.senha = nova_senha
        print("Senha alterada com sucesso.")

    def alterar_plano(self, novo_tipo):
        if novo_tipo in ["Simples", "Premium"]:
            self.tipo_assinatura = novo_tipo
            print("Plano alterado com sucesso.")
        else:
            print("Tipo de assinatura inválido.")

    def listar_midias_apropriadas(self, tipo, catálogo):
        midias_apropriadas = []
        for perfil in self.perfis:
            midias_apropriadas.extend(perfil.listar_midias_apropriadas(tipo, catálogo))
        return midias_apropriadas

# Persistência de dados com arquivos CSV
def salvar_catalogo(catálogo):
    with open('catalogoGeral.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for mídia in catálogo.lista_series + catálogo.lista_filmes + catálogo.lista_documentarios + catálogo.lista_animacoes + catálogo.lista_programas_tv:
            writer.writerow([mídia.tipo, mídia.título, mídia.gênero, mídia.ano_lançamento, mídia.classificação])

def carregar_catalogo():
    catálogo = Catálogo()
    with open('catalogoGeral.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            tipo, título, gênero, ano_lançamento, classificação = row
            if tipo == "Série":
                num_temporadas = int(input(f"Informe o número de temporadas para a série {título}: "))
                episodios_por_temporada = {}  
                for temporada in range(1, num_temporadas + 1):
                    episodios = input(f"Informe os episódios da temporada {temporada}, separados por vírgula: ")
                    episodios_por_temporada[temporada] = episodios.split(', ')
                mídia = Série(título, gênero, ano_lançamento, classificação, num_temporadas, episodios_por_temporada)
            elif tipo == "Filme":
                diretor = input(f"Informe o diretor para o filme {título}: ")
                produtor = input(f"Informe o produtor para o filme {título}: ")
                mídia = Filme(título, gênero, ano_lançamento, classificação, diretor, produtor)
            # Adicionar lógica para outros tipos de mídia
            catálogo.adicionar_midia(mídia)
    return catálogo

def salvar_usuarios(usuarios):
    with open('usuarios.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for usuario in usuarios:
            writer.writerow([usuario.nome, usuario.senha, usuario.tipo_assinatura])

def carregar_usuarios():
    usuarios = []
    with open('usuarios.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            nome, senha, tipo_assinatura = row
            usuarios.append(Usuário(nome, senha, tipo_assinatura))
    return usuarios


def salvar_perfis(perfis):
    with open('perfis.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for perfil in perfis:
            writer.writerow([perfil.nome, perfil.idade, perfil.favoritos, perfil.ultimos_assistidos])

def carregar_perfis():
    perfis = []
    with open('perfis.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            nome, idade, favoritos, ultimos_assistidos = row
            perfil = Perfil(nome, idade)
            perfil.favoritos = eval(favoritos)
            perfil.ultimos_assistidos = eval(ultimos_assistidos)
            perfis.append(perfil)
    return perfis

# Menus

def tela_inicial():
    print("Bem-vindo ao Sistema de Streaming!")
    print("1 - Menu do Usuário")
    print("2 - Menu do Perfil")
    print("3 - Listar Mídia")
    print("4 - Sair")

#REVER ESTA FUNCAO
def obter_perfil_pelo_nome(nome, usuario):
    for perfil in usuario.perfis:
        if perfil.nome.lower() == nome.lower():
            return perfil
    return None

def menu_usuario(usuario, catalogo):
    while True:
        print("\nMenu do Usuário")
        print("1 - Acessar Perfil")
        print("2 - Editar Perfil")
        print("3 - Criar Conta")
        print("4 - Adicionar Perfil")
        print("5 - Remover Perfil")
        print("0 - Voltar ao Menu Anterior")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_perfil = input("Digite o nome do perfil: ")
            perfil = obter_perfil_pelo_nome(nome_perfil, usuario)
            if perfil:
                menu_perfil(perfil, catalogo)
            else:
                print("Perfil não encontrado.")

        elif opcao == "2":
            editar_perfil(usuario)
        elif opcao == "3":
            criar_conta(usuario)
        elif opcao == "4":
            adicionar_perfil(usuario)
        elif opcao == "5":
            remover_perfil(usuario)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def editar_perfil(usuario):
    # Adicione a lógica para editar perfil
    print("Editando perfil (em construção)...")

def criar_conta(usuarios):
    nome = input("Digite o nome para a nova conta: ")
    senha = input("Digite a senha para a nova conta: ")
    tipo_assinatura = input("Digite o tipo de assinatura (Simples/Premium): ").capitalize()

    novo_usuario = Usuário(nome, senha, tipo_assinatura)
    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)

    print("Conta criada com sucesso.")

def adicionar_perfil(usuario):
    nome = input("Digite o nome para o novo perfil: ")
    idade = int(input("Digite a idade para o novo perfil: "))

    usuario.adicionar_perfil(nome, idade)

    print(f"Perfil {nome} adicionado com sucesso.")

def remover_perfil(usuario):
    nome = input("Digite o nome do perfil que deseja remover: ")

    usuario.remover_perfil(nome)

    print(f"Perfil {nome} removido com sucesso.")

def menu_perfil(perfil, catalogo, usuario):
    while True:
        print("\nMenu do Perfil")
        print("1 - Tela Inicial")
        print("2 - Menu do Usuário")
        print("3 - Listar Mídia")
        print("0 - Voltar ao Menu Anterior")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Adicione a lógica para tela inicial do perfil
            print("Tela inicial do perfil (em construção)...")
        elif opcao == "2":
            menu_usuario(usuario, catalogo)
        elif opcao == "3":
            menu_listar_midia(perfil, catalogo)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def menu_perfil():
    while True:
        print("Menu do Perfil")
        print("1 - Tela Inicial")
        print("2 - Menu do Usuário")
        print("3 - Listar Mídia")
        print("0 - Voltar ao Menu Anterior")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Adicione a lógica para tela inicial do perfil
            print("Tela inicial do perfil (em construção)...")
        elif opcao == "2":
            menu_usuario()
        elif opcao == "3":
            # Adicione a lógica para listar mídia
            print("Listando mídia (em construção)...")
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def menu_listar_midia(perfil, catalogo):
    while True:
        print("\nMenu Listar Mídia")
        print("1 - Listar Mídias Apropriadas")
        print("2 - Exibir Favoritos")
        print("3 - Exibir Últimos Assistidos")
        print("4 - Adicionar Episódio")
        print("5 - Assistir a Mídia")
        print("0 - Voltar ao Menu Anterior")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_midias_apropriadas(perfil, catalogo)
        elif opcao == "2":
            perfil.listar_favoritos()
        elif opcao == "3":
            perfil.listar_ultimos_assistidos()
        elif opcao == "4":
            adicionar_episodio(catalogo)
        elif opcao == "5":
            assistir_midia(perfil, catalogo)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def adicionar_episodio(catalogo):
    serie_titulo = input("Digite o título da série: ")
    temporada_numero = int(input("Digite o número da temporada: "))
    episodio_nome = input("Digite o nome do episódio: ")

    serie = catalogo.buscar_por_titulo(serie_titulo)
    if isinstance(serie, Série):
        catalogo.adicionar_episodio(serie, temporada_numero, episodio_nome)
    else:
        print("Série não encontrada.")
        
def listar_todas_midias(catalogo):
    for tipo in ["Série", "Filme", "Documentário", "Animação", "ProgramaTV"]:
        lista = catalogo.obter_lista(tipo)
        print(f"\n{tipo}s:")
        for mídia in lista:
            mídia.exibir_informacoes()

def listar_midias_por_tipo(catalogo):
    tipo = input("Informe o tipo de mídia (Série, Filme, Documentário, Animação, ProgramaTV): ")
    lista = catalogo.obter_lista(tipo)
    if lista:
        print(f"\n{tipo}s:")
        for mídia in lista:
            mídia.exibir_informacoes()
    else:
        print(f"Nenhuma {tipo} encontrada no catálogo.")

def listar_midias_apropriadas(perfil, catalogo):
    tipo_midia = input("Digite o tipo de mídia a ser listada (Série/Filme/Documentário/Animação/ProgramaTV): ").capitalize()
    midias_apropriadas = perfil.listar_midias_apropriadas(tipo_midia, catalogo)

    if midias_apropriadas:
        print(f"\nMídias Apropriadas para {perfil.nome} ({tipo_midia}):")
        for midia in midias_apropriadas:
            midia.exibir_informacoes()
    else:
        print(f"\nNenhuma mídia apropriada encontrada para {perfil.nome} ({tipo_midia}).")

def menu_da_midia(perfil, catalogo):
    while True:
        print("\nMenu da Mídia")
        print("1 - Assistir Mídia")
        print("2 - Favoritar/Desfavoritar Mídia")
        print("3 - Buscar Mídia por Título")
        print("0 - Voltar ao Menu Anterior")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            assistir_midia(perfil)
        elif opcao == "2":
            favoritar_midia(perfil, catalogo)
        elif opcao == "3":
            buscar_midia_por_titulo(catalogo)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def assistir_midia(perfil, catalogo):
    titulo_midia = input("Digite o título da mídia que deseja assistir: ")
    midia = catalogo.buscar_por_titulo(titulo_midia)

    if midia:
        perfil.assistir(midia)
    else:
        print("Mídia não encontrada.")

def favoritar_midia(perfil, catalogo):
    titulo = input("Digite o título da mídia que deseja favoritar/desfavoritar: ")
    midia = perfil.buscar_por_titulo(titulo, catalogo)
    if midia:
        favoritar = input(f"Deseja favoritar {titulo}? (S/N): ").upper()
        perfil.favoritar(midia, favoritar == "S")
    else:
        print(f"{titulo} não encontrado no catálogo.")

def buscar_midia_por_titulo(catalogo):
    titulo = input("Digite o título da mídia que deseja buscar: ")
    midia = catalogo.buscar_por_titulo(titulo)
    if midia:
        midia.exibir_informacoes()
    else:
        print(f"{titulo} não encontrado no catálogo.")

def menu_de_episodios():
    while True:
        print("Menu de Episódios")
        print("1 - Nome do Episódio 1")
        print("2 - Nome do Episódio 2")
        print("0 - Voltar ao Menu Anterior")

        opcao = input("Escolha uma opção: ")

        if opcao in ["1", "2"]:
            # Adicionar lógica para selecionar episódio
            print(f"Selecionar Episódio {opcao} (em construção)...")
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def criar_nova_conta(usuarios):
        print("\nCriar Nova Conta")
        nome_usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")
        tipo_assinatura = input("Digite o tipo de assinatura (Simples/Premium): ").capitalize()

        # Verifica se o nome de usuário já está em uso
        if any(usuario.nome.lower() == nome_usuario.lower() for usuario in usuarios):
            print("Erro: Nome de usuário já em uso.")
            return None

        novo_usuario = Usuário(nome_usuario, senha, tipo_assinatura)
        usuarios.append(novo_usuario)
        salvar_usuarios(usuarios)
        print("Usuário criado com sucesso!")
        return novo_usuario

def main():
    usuarios = carregar_usuarios()
    catalogo = carregar_catalogo()
    perfis = carregar_perfis()

    while True:
        print("\nBem-vindo ao Sistema de Streaming!")
        print("1 - Login")
        print("2 - Criar Nova Conta")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario = fazer_login(usuarios)
            if usuario:
                perfil = menu_usuario(usuario, perfis, catalogo)
                if perfil:
                    menu_perfil(perfil, catalogo)
            else:
                print("Usuário não encontrado ou senha incorreta.")
        elif opcao == "2":
            novo_usuario = criar_nova_conta(usuarios)
            if novo_usuario:
                usuarios.append(novo_usuario)
                salvar_usuarios(usuarios)
                print("Conta criada com sucesso.")
        elif opcao == "3":
            salvar_usuarios(usuarios)
            salvar_catalogo(catalogo)
            salvar_perfis(perfis)
            print("Obrigado por usar o Sistema de Streaming! Até logo.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
