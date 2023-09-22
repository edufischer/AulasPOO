# Função para carregar dados dos arquivos CSV
#ef carregar_usuarios():
#   usuarios = []
#   with open('usuarios.csv', 'r') as arquivo_csv:
#       leitor = csv.reader(arquivo_csv)
#       #next(leitor)  # Pula a primeira linha (cabeçalho)
#       for linha in leitor:
#           nome, senha = linha
#           usuarios.append(Usuario(nome, senha))
#   return usuarios
#
#ef carregar_figurinhas():
#   figurinhas = []
#   with open('figurinhas.csv', 'r') as arquivo_csv:
#       leitor = csv.reader(arquivo_csv)
#       #next(leitor)  # Pula a primeira linha (cabeçalho)
#       for linha in leitor:
#           numero, jogador, informacao, status = linha
#           figurinhas.append(Figurinha(int(numero), jogador, informacao, int(status)))
#   return figurinhas
#
#ef carregar_trocas():
#   trocas = []
#   with open('trocas.csv', 'r') as arquivo_csv:
#       leitor = csv.reader(arquivo_csv)
#       #next(leitor)  # Pula a primeira linha (cabeçalho)
#       for linha in leitor:
#           remetente, destinatario, figurinha_oferecida, figurinha_desejada, status = linha
#           trocas.append(Troca(remetente, destinatario, int(figurinha_oferecida), int(figurinha_desejada), int(status)))
#   return trocas
#
# Função para salvar dados nos arquivos CSV
#ef salvar_usuarios(usuarios):
#   with open('usuarios.csv', 'w', newline='') as arquivo_csv:
#       escritor = csv.writer(arquivo_csv)
#       escritor.writerow(['nome', 'senha'])
#       for usuario in usuarios:
#           escritor.writerow([usuario.nome, usuario.senha])
#
#ef salvar_figurinhas(figurinhas):
#   with open('figurinhas.csv', 'w', newline='') as arquivo_csv:
#       escritor = csv.writer(arquivo_csv)
#       escritor.writerow(['numero', 'jogador', 'informacao', 'status'])
#       for figurinha in figurinhas:
#           escritor.writerow([figurinha.numero, figurinha.jogador, figurinha.informacao, figurinha.status])
#
#ef salvar_trocas(trocas):
#   with open('trocas.csv', 'w', newline='') as arquivo_csv:
#       escritor = csv.writer(arquivo_csv)
#       escritor.writerow(['remetente', 'destinatario', 'figurinha_oferecida', 'figurinha_desejada', 'status'])
#       for troca in trocas:
#           escritor.writerow([troca.remetente, troca.destinatario, troca.figurinha_oferecida, troca.figurinha_desejada, troca.status])
#
# Função para criar um novo usuário
#ef criar_usuario():
#   nome = input("Digite o nome de usuário: ")
#   senha = input("Digite a senha: ")
#   return Usuario(nome, senha)
#
# Função para acessar o álbum do usuário
#ef acessar_album(usuarios):
#   nome_usuario = input("Digite seu nome de usuário: ")
#   senha = input("Digite sua senha: ")
#   
#   for usuario in usuarios:
#       if usuario.nome == nome_usuario and usuario.senha == senha:
#           return usuario
#
#   print("Usuário não encontrado ou senha incorreta.")
#   return None
#
# Função para mostrar o menu principal
#ef menu_principal():
#   print("Menu Principal:")
#   print("1. Novo Álbum")
#   print("2. Acessar Álbum")
#   print("3. Sair do Aplicativo")
#   opcao = input("Escolha uma opção: ")
#   return opcao
#
# Função para mostrar o menu do álbum
#ef menu_album():
#   print("Menu do Álbum:")
#   print("1. Ver Álbum")
#   print("2. Gerenciar a coleção")
#   print("3. Abrir pacote de Figurinhas")
#   print("4. Voltar ao menu anterior")
#   opcao = input("Escolha uma opção: ")
#   return opcao
#
# Função para ver o álbum do usuário
#ef ver_album(album):
#   for pagina_num, pagina in enumerate(album.paginas, start=1):
#       print(f"Página {pagina_num}:")
#       for figurinha in pagina:
#           if figurinha.status == 1:
#               print(f"{figurinha.numero}: {figurinha.jogador}")
#           elif figurinha.status == 0:
#               print(f"{figurinha.numero}: [COLAR]")
#           else:
#               print(f"{figurinha.numero}: [X]")
#
#
# Função principal
#ef main():
#   usuarios = carregar_usuarios()
#   figurinhas = carregar_figurinhas()
#   trocas = carregar_trocas()
#
#   while True:
#       opcao = menu_principal()
#
#       if opcao == '1':
#           novoUsuario = criar_usuario()
#           usuarios.append(novo_usuario)
#       elif opcao == '2':
#           usuario_logado = acessar_album(usuarios)
#           if usuario_logado:
#               while True:
#                   opcao_album = menu_album()
#                   if opcao_album == '1':
#                       ver_album(usuario_logado.album)
#                   #elif opcao_album == '2':
#                   #    gerenciar_colecao(usuario_logado)
#                   #elif opcao_album == '3':
#                   #    abrir_pacote(usuario_logado)
#                   elif opcao_album == '4':
#                       break
#                   else:
#                       print("Opção inválida.")
#       elif opcao == '3':
#           salvar_usuarios(usuarios)
#           salvar_figurinhas(figurinhas)
#           salvar_trocas(trocas)
#           break
#       else:
#           print("Opção inválida.")
#
#f __name__ == "__main__":
#   main()
# 
#
#
#
#
#
#
#
#########################################################################
#
# Nome do arquivo CSV a ser criado (sem dados)
#arquivo_usuarios = "usuarios.csv"
#arquivo_trocas = "trocas.csv"
#arquivo_figurinhas = "figurinhas.csv"
#
# # Abre o arquivo CSV em modo de escrita e cria o arquivo se não existir
#with open(arquivo_usuarios, 'w', newline='') as arquivo_csv:
#    pass  
#with open(arquivo_figurinhas, 'w', newline='') as arquivo_csv:
#    pass 
#with open(arquivo_trocas, 'w', newline='') as arquivo_csv:
#    pass  # Não é necessário escrever dados, apenas criar o arquivo