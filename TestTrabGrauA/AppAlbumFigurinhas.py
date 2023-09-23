# import csv
# import random
# import os



# # Funcoes para Carregar os Dados do Programa

# def carregarUsuarios():
#     usuarios = []
#     with open('usuarios.csv', 'r') as arquivo_csv:
#         leitor = csv.reader(arquivo_csv)
#         #next(leitor)  # Pula a primeira linha (cabeçalho)
#         for linha in leitor:
#             nome, senha = linha
#             usuarios.append(Usuario(nome, senha))
#     return usuarios

# def carregarFigurinhas():
#     figurinhas = []
#     with open('figurinhas.csv', 'r') as arquivo_csv:
#         leitor = csv.reader(arquivo_csv)
#         #next(leitor)  # Pula a primeira linha (cabeçalho)
#         for linha in leitor:
#             numero, jogador, informacao, status = linha
#             figurinhas.append(Figurinha(int(numero), jogador, informacao, int(status)))
#     return figurinhas

# def carregarTrocas():
#     trocas = []
#     with open('trocas.csv', 'r') as arquivo_csv:
#         leitor = csv.reader(arquivo_csv)
#         #next(leitor)  # Pula a primeira linha (cabeçalho)
#         for linha in leitor:
#             remetente, figurinha_oferecida, figurinha_desejada, status = linha
#             trocas.append(Troca(remetente, int(figurinha_oferecida), int(figurinha_desejada), int(status)))
#     return trocas

# def iniciliazar():
#     usuarios = carregarUsuarios()
#     figurinhas = carregarFigurinhas()
#     trocas = carregarTrocas()


# # Tela Inicial 


# # Função para acessar o álbum do usuário
# def acessarAlbum(usuarios):
#     nome_usuario = input("Digite seu nome de usuário: ")
#     senha = input("Digite sua senha: ")
    
#     for usuario in usuarios:
#         if usuario.nome == nome_usuario and usuario.senha == senha:
#             return usuario

#     print("Usuário não encontrado ou senha incorreta.")
#     return None

# def menuAlbum():
#     print("Menu do Álbum:")
#     print("1. Ver Álbum")
#     print("2. Gerenciar a coleção")
#     print("3. Abrir pacote de Figurinhas")
#     print("4. Voltar ao menu anterior")
#     opcao = input("Escolha uma opção: ")
#     return opcao


# # Função para ver o álbum do usuário
# def verAlbum(album):
#     for pagina_num, pagina in enumerate(album.paginas, start=1):
#         print(f"Página {pagina_num}:")
#         for figurinha in pagina:
#             if figurinha.status == 1:
#                 print(f"{figurinha.numero}: {figurinha.jogador}")
#             elif figurinha.status == 0:
#                 print(f"{figurinha.numero}: [COLAR]")
#             else:
#                 print(f"{figurinha.numero}: [X]")

