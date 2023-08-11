# criaçao de uma funçao cumprimentar
def cumprimentar(nome): # recebe como parametro uma variavel 
    print('Ola, ', nome)


#--------

cumprimentar('Rossana')  # string é um array de vetores

nome = 'Rafael' # em Python não precisar colocar o type da variavel quando for instancia-la.
nome2 = 'Valentina'

cumprimentar(nome)
cumprimentar(nome2)

nome3 = input('Digite um nome: ') # variavel que vai guardar o valor do input do usuario

cumprimentar(nome3) # printa na dela a variavel que o usuario digitou anteriormente

nomes = [ 'Ana', 'Pedro', 'Maria', 'Joao', 'Francisca'] # criação de uma lista

for i in nomes:
    cumprimentar(i) # i vai percorrer a lista nome pegando cada objeto dentro e chamando a função cumprimentar

for i in range(len(nomes)): 
    # i vai percorrer o a funçao range que retorna um objeto com inicio da sequencia e o final
    # ou seja, range(0,3)
    cumprimentar(nomes[i])

