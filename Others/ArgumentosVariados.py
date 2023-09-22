""" o uso de **kwargs em uma função permite que você trate os argumentos passados como um dicionário dentro da função.
 kwargs é uma abreviação de "keyword arguments" (argumentos de palavras-chave) e permite que você passe argumentos nomeados 
 arbitrários para uma função. Dentro da função, você pode acessar esses argumentos nomeados como se fossem pares chave-valor em um dicionário.

Aqui está um exemplo que ilustra como **kwargs funciona como um dicionário:

def mostrar_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

mostrar_info(nome='Alice', idade=30, cidade='São Paulo')
Neste exemplo, os argumentos nome, idade e cidade são passados para a função mostrar_info usando **kwargs. Dentro da função, esses
 argumentos são tratados como um dicionário, onde as chaves são os nomes dos argumentos e os valores são os valores associados a essas
   chaves. A função itera pelo dicionário kwargs e imprime as informações associadas a cada chave.

Portanto, **kwargs é uma maneira conveniente de lidar com argumentos nomeados arbitrários em Python e permite que você trate esses
 argumentos como um dicionário dentro da função. """


def function_doubleasterix(**keywordargs):

    print("The KEYS in the kwargs dicionary are -", keywordargs.keys())
    print("The VALUES in the kwargs dicionary are -", keywordargs.values())

    print("--The key value assignment in the 'keywordargs' dictionary are as follows--")
    for key, value in keywordargs.items():
        print ("%s == %s" %(key, value))
#No exemplo acima, keywordargs está associado a um dicionário como no programa abaixo.

function_doubleasterix(SNo001 ='Alex', SNo002 ='Tom')