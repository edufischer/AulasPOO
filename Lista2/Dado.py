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


dado_com_6_lados = Dado(6)
dado_com_8_lados = Dado(8)
dado_com_12_lados = Dado(12)

#print(f'Rolando dado de 6 lados... O resultado foi: {dado_com_6_lados.Rolar()}\n')
#print(f'Rolando dado de 6 lados... O resultado foi: {dado_com_6_lados.Rolar()}\n')
#print(f'Rolando dado de 6 lados... O resultado foi: {dado_com_6_lados.Rolar()}\n')
#
#print(f'Rolando dado de 8 lados... O resultado foi: {dado_com_8_lados.Rolar()}\n')
#print(f'Rolando dado de 8 lados... O resultado foi: {dado_com_8_lados.Rolar()}\n')
#print(f'Rolando dado de 8 lados... O resultado foi: {dado_com_8_lados.Rolar()}\n')
#
#print(f'Rolando dado de 12 lados... O resultado foi: {dado_com_12_lados.Rolar()}\n')
#print(f'Rolando dado de 12 lados... O resultado foi: {dado_com_12_lados.Rolar()}\n')
#print(f'Rolando dado de 12 lados... O resultado foi: {dado_com_12_lados.Rolar()}\n')

#    Faça um programa que simule um "dado virtual". O dado deve ser modelado como uma classe,
#possuindo apenas o número de faces e o método Rolar, que retorna o valor sorteado. O número
#de faces deve ser definido na criação do objeto (construtor com parâmetro). Deve ser instanciado
#um dado com 6, 8 e 12 faces no main(). Cada dado deve ser jogado 3 vezes e o resultado de cada
#jogada deve ser impresso na tela. Não deve ser usado print dentro da classe.
