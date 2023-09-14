import secrets

class Dado:

    def __init__(self, numero):
        self.faces = int(numero)

    def rolar(self):
        contagem = 0
        while contagem != 3:
            if self.faces == 6:
                dadoComSeis = [1,2,3,4,5,6]
                numero = secrets.choice(dadoComSeis) 
                contagem += 1
                return numero
            
            elif self.faces == 8:
                dadoComOito = [1,2,3,4,5,6,7,8]
                numero = secrets.choice(dadoComOito) 
                contagem += 1
                return numero
        
            elif self.faces == 12:
                dadoComDoze = [1,2,3,4,5,6,7,8,9,10,11,12]
                numero = secrets.choice(dadoComDoze) 
                contagem += 1
                return numero

    #FUNÇAO ABAIXO UTILIZADA NO EXERCICIO DA CORRIDA MALUCA:
    def rolarDadoSeisLados(self):
                dadoComSeis = [1,2,3,4,5,6]
                numero = secrets.choice(dadoComSeis) 
                return numero
    


dado_com_6_lados = Dado(6)
dado_com_8_lados = Dado(8)
dado_com_12_lados = Dado(12)

