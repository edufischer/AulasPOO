# Criando um dicionário vazio
meu_dicionario = {}

# Adicionando elementos ao dicionário
meu_dicionario["nome"] = "Alice"
meu_dicionario["idade"] = 30
meu_dicionario["cidade"] = "São Paulo"

# Acessando elementos do dicionário
nome = meu_dicionario["nome"]

# Modificando elementos do dicionário
meu_dicionario["idade"] = 31

# Verificando se uma chave existe no dicionário
if "cidade" in meu_dicionário:
    print("A chave 'cidade' existe no dicionário.")

# Removendo elementos do dicionário
meu_dicionario.pop("idade")
del meu_dicionario["cidade"]

# Iterando sobre o dicionário
for chave in meu_dicionario:
    print(chave)  # Itera sobre as chaves

for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")  # Itera sobre pares chave-valor

# Compreensão de dicionário para criar um dicionário a partir de uma lista
numeros = [1, 2, 3, 4, 5]
quadrados = {n: n ** 2 for n in numeros}

# Funções úteis de dicionário
chaves = meu_dicionario.keys()      # Retorna uma lista das chaves
valores = meu_dicionario.values()    # Retorna uma lista dos valores
pares = meu_dicionario.items()       # Retorna uma lista de tuplas chave-valor
valor = meu_dicionario.get("nome")  # Obtém o valor associado a uma chave
