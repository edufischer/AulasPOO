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
        for pais in self.getNome():
            dimensao += pais.get_dimensao_km2()
        return dimensao

    #d. Um método que retorne a população total do continente;
    def populacao_total(self):
        pass

    #e. Um método que retorne a densidade populacional do continente;
    def densidade_populacional(self):
        pass

    #f. Um método que retorne o país com maior população no continente;
    def pais_maior_populacao(self):
        pass

    #g. Um método que retorne o país com menor população no continente;
    def pais_menor_populacao(self):
        pass

    #h. Um método que retorne o país de maior dimensão territorial no continente;
    def pais_maior_dimensao(self):
        pass

    #i. Um método que retorne o país de menor dimensão territorial no continente;
    def pais_menor_dimensao(self):
        pass

    #j. Um método que retorne a razão territorial do maior país em relação ao menor país.
    def razao_territorial(self):
        pass

# Testes:
continente_americano = Continente("América")

brasil = Pais("BRA", "Brasil", 8515767.049)
argentina = Pais("ARG", "Argentina", 2780400)
paraguai = Pais("PRY", "Paraguai", 406752)

brasil.setPopulacao(211049527)
argentina.setPopulacao(44938712)
paraguai.setPopulacao(7252672)

continente_americano.adicionarPais(brasil)
continente_americano.adicionarPais(argentina)
continente_americano.adicionarPais(paraguai)

print(f"Dimensão total do continente: {continente_americano.dimensao_total()} km²")
print(f"População total do continente: {continente_americano.populacao_total()} pessoas")
print(f"Densidade populacional do continente: {continente_americano.densidade_populacional()} pessoas/km²")
print(f"País com maior população no continente: {continente_americano.pais_maior_populacao().get_nome()}")
print(f"País com menor população no continente: {continente_americano.pais_menor_populacao().get_nome()}")
print(f"País de maior dimensão territorial no continente: {continente_americano.pais_maior_dimensao().get_nome()}")
print(f"País de menor dimensão territorial no continente: {continente_americano.pais_menor_dimensao().get_nome()}")
print(f"Razão territorial (maior/menor): {continente_americano.razao_territorial()}")










