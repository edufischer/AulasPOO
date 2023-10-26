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





def function_doubleasterix(**keywordargs):
    # Imprime as chaves (nomes dos argumentos) do dicionário keywordargs.
    print("The KEYS in the kwargs dicionary are -", keywordargs.keys())
    
    # Imprime os valores associados às chaves no dicionário keywordargs.
    print("The VALUES in the kwargs dicionary are -", keywordargs.values())

    # Imprime as atribuições de chave-valor no dicionário keywordargs.
    print("--The key value assignment in the 'keywordargs' dictionary are as follows--")
    for key, value in keywordargs.items():
        print ("%s == %s" %(key, value))

# Chamando a função function_doubleasterix com argumentos nomeados arbitrários.
function_doubleasterix(SNo001 ='Alex', SNo002 ='Tom')

#Quando você chama function_doubleasterix(SNo001='Alex', SNo002='Tom'), está passando dois argumentos nomeados (SNo001 e SNo002) para a função. Dentro da função, esses argumentos são tratados como um dicionário chamado keywordargs, onde as chaves são os nomes dos argumentos (SNo001 e SNo002), e os valores são os valores associados a essas chaves ('Alex' e 'Tom').

#O código então imprime as chaves, os valores e as atribuições de chave-valor dentro desse dicionário keywordargs. No exemplo dado, a saída seria algo como:
#
#sql


#The KEYS in the kwargs dicionary are - dict_keys(['SNo001', 'SNo002'])
#The VALUES in the kwargs dicionary are - dict_values(['Alex', 'Tom'])
#--The key value assignment in the 'keywordargs' dictionary are as follows--
#SNo001 == Alex
#SNo002 == Tom


