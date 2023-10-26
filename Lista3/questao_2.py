from questao_1 import Pais

#2. Escreva uma classe Continente. Um continente possui um nome e é composto por um conjunto
#de países. Forneça os membros de classe a seguir:

class Continente:

    #a. Construtor que inicialize o nome do continente;
    def __init__(self, nome):
        self.__nome = nome
        self.__paises = []

    def setNome (self, novo_nome):
        self.__nome = novo_nome

    def getNome (self):
        return self.__nome
    
    #b. Um método que permita adicionar países aos continentes;
    def adicionarPais (self, novo_pais):
        self.__paises.append(novo_pais)

    def getPaises (self):
        return self.__paises


    #c. Um método que retorne a dimensão total do continente;
    def dimensao_total(self):
        dimensao = 0
        for pais in self.getPaises():
            dimensao += pais.getDimensao()
        return dimensao

    #d. Um método que retorne a população total do continente;
    def populacao_total(self):
        populacao = 0
        for pais in self.getPaises():
            populacao += pais.getPopulacao()
        return populacao

    #e. Um método que retorne a densidade populacional do continente;
    def densidade_populacional(self):
        densidade = 0
        for pais in self.getPaises():
            densidade += pais.getDensidade()
        return densidade

    #f. Um método que retorne o país com maior população no continente;
    def pais_maior_populacao(self):
        maior_populacao = None
        for pais in self.getPaises():
            if maior_populacao == None:
                maior_populacao = pais
            elif pais.getPopulacao() > maior_populacao.getPopulacao():
                maior_populacao = pais
        return maior_populacao

    #g. Um método que retorne o país com menor população no continente;
    def pais_menor_populacao(self):
        menor_populacao = None
        
        for pais in self.getPaises():
            if menor_populacao == None:
                menor_populacao = pais
            elif pais.getPopulacao() < menor_populacao.getPopulacao():   
                menor_populacao = pais
                
        return menor_populacao

    #h. Um método que retorne o país de maior dimensão territorial no continente;
    def pais_maior_dimensao(self):
        maior_dimensao = None
        for pais in self.getPaises():
            if maior_dimensao == None:
                maior_dimensao = pais
                
            elif pais.getDimensao() > maior_dimensao.getDimensao():
                maior_dimensao = pais
        return maior_dimensao


    #i. Um método que retorne o país de menor dimensão territorial no continente;
    def pais_menor_dimensao(self):
        menor_dimensao = None
        
        for pais in self.getPaises():
            if menor_dimensao == None:
                menor_dimensao = pais
            elif pais.getDimensao() < menor_dimensao.getDimensao():   
                menor_dimensao = pais
                
        return menor_dimensao

    #j. Um método que retorne a razão territorial do maior país em relação ao menor país.
    def razao_territorial(self):
        pais_maior = self.pais_maior_dimensao()
        pais_menor = self.pais_menor_dimensao()
        
        razao = int(pais_maior.getDimensao()) / int(pais_menor.getDimensao())
        # Para retornar apenas com 4 casas decimais (após a vírgula).
        razao_formatada = round(razao, 4)
        
        return [razao_formatada, pais_maior, pais_menor]

# Testes:
continente_americano = Continente("América")

brasil = Pais("BRA", "Brasil", 8515767.049, 423943243242)
argentina = Pais("ARG", "Argentina", 2780400, 432843202)
paraguai = Pais("PRY", "Paraguai", 406752, 42394932)

brasil.setPopulacao(211049527)
argentina.setPopulacao(44938712)
paraguai.setPopulacao(7252672)

continente_americano.adicionarPais(brasil)
continente_americano.adicionarPais(argentina)
continente_americano.adicionarPais(paraguai)

print(f"Dimensão total do continente: {continente_americano.dimensao_total()} km².\n")
print(f"População total do continente: {continente_americano.populacao_total()} pessoas.\n")
print(f"Densidade populacional do continente: {continente_americano.densidade_populacional()} pessoas/km².\n")
print(f"País com maior população no continente: {continente_americano.pais_maior_populacao().getNome()}.\n")
print(f"País com menor população no continente: {continente_americano.pais_menor_populacao().getNome()}.\n")
print(f"País de maior dimensão territorial no continente: {continente_americano.pais_maior_dimensao().getNome()}.\n")
print(f"País de menor dimensão territorial no continente: {continente_americano.pais_menor_dimensao().getNome()}.\n")
resultado_razao = continente_americano.razao_territorial()
print(f"Razão territorial (maior/menor): O País {resultado_razao[1].getNome()} é {resultado_razao[0]} vezes maior que o país {resultado_razao[2].getNome()}.\n")










