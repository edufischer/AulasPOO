# Escreva uma classe que represente um País. Um país é representado através dos atributos: código
# ISO 3166-1 (ex.: BRA), nome (ex.:Brasil), população (ex.: 193.946.886) e a sua dimensão em Km2
# (ex.: 8.515.767,049). Além disso, cada país mantém uma lista de outros países com os quais ele faz
# fronteira. Escreva a classe e forneça os seus membros a seguir:

class Pais:


    # a. Construtor que inicialize o código ISO, o nome e a dimensão do país;

    def __init__(self, codigo=None, nome=None, populacao=None, dimensao=None, vizinhos = []):
        self.__codigo = codigo
        self.__nome = nome
        self.__populacao = populacao
        self.__dimensao = dimensao
        self.__vizinhos = vizinhos

    def imprimirInfos(self):
        print ('Nome: ',self.__nome)
        print ('Codigo: ', self.__codigo)
        print ('Populacao: ', self.__populacao)
        print ('Dimensao ', self.__dimensao)
        print ('Lista de paises vizinhos: ')
        for vizinho in self.__vizinhos:
            print(vizinho)


    # b. Métodos de acesso (getter/setter) para as propriedades código ISO, nome, população e  dimensão do país;

    def setCodigo (self, novo_codigo):
        self.__codigo = novo_codigo

    def setNome (self, novo_nome):
        self.__nome = novo_nome

    def setPopulacao (self, nova_populaocao):
        self.__populacao = nova_populaocao

    def setDimensao (self, nova_dimensao):
        self.__dimensao = nova_dimensao

    def getCodigo (self):
        return self.__codigo
    
    def getNome(self):
        return self.__nome
    
    def getPopulacao (self):
        return self.__populacao
        
    def getDimensao (self):
        return self.__dimensao

    def setVizinho (self, novo_vizinho):
        vizinhos = self.getVizinhos()
        vizinhos.append(novo_vizinho)

    def removeVizinho (self, vizinho):
        vizinhos = self.getVizinhos()
        vizinhos.remove(vizinho)

    def getVizinhos (self):
        return self.__vizinhos

    # c. Um método que permita verificar se dois objetos representam o mesmo país (isso se chama igualdade semântica). Dois países são iguais se tiverem o mesmo código ISO;
    def checkCodigo (self, outro_pais):
        codigo_pais = self.getCodigo()
        codigo_outro_pais = outro_pais.getCodigo()

        if codigo_pais == codigo_outro_pais:
            print('Os paises verificados possuem o mesmo código ISO; logo, são o mesmo país.')
        else:
            print('Os paises verificados não possuem o mesmo código ISO; logo, são paises diferentes.')
    
    # d. Um método que informe se outro país é limítrofe (faz fronteira) do país que recebeu a mensagem;
    def checkFronteira(self, outro_pais):
        lista_vizinhos = self.getVizinhos()
        if outro_pais in lista_vizinhos:
            print(f'O pais {outro_pais.getNome()} faz fronteira com o {self.getNome()}.')
        else:
            print(f'O pais {outro_pais.getNome()} não faz fronteira com o {self.getNome()}.')


    # e. Um método que retorne a densidade populacional do país;
    def getDensidade(self):
        populacao = self.getPopulacao
        dimensao = self.getDensidade
        densidade = populacao / dimensao
        return densidade 

    # f. Um método que receba um país como parâmetro e retorne a lista de vizinhos comuns aos dois países.
    def fronteirasIguais (self, outro_pais):
        vizinhos = self.getVizinhos()
        fronteiras_do_outro_pais = outro_pais.getVizinhos()
        nova_lista = []

        for pais in vizinhos:
            if pais in fronteiras_do_outro_pais:
                nova_lista.append(pais)
                
        return nova_lista
