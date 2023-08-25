#Crie uma classe chamada Calculadora, com os métodos somar, subtrair, multiplicar e dividir dois
#números. Cada um destes métodos recebe por parâmetro dois números reais e retorna o
#resultado da operação com os dois números. Se houver divisão por zero, imprimir um aviso na
#execução do método e retornar -1.

class Calculadora:

    def __init__(self,first_num, second_num):
        self.first_num = int(first_num)
        self.second_num = int(second_num)

    
    def Somar(self):
        soma = self.first_num + self.second_num
        return soma
    
    def Subtrair(self):
        subtracao = self.first_num - self.second_num
        return subtracao
    
    def Multiplicar(self):
        multiplicacao = self.first_num * self.second_num
        return multiplicacao
    
    def Dividir(self):
        if self.first_num or self.first_num is 0:
            print('Aviso: impossível de efetuar divisão com 0!')
            return -1
        else:
            divisao = self.first_num // self.second_num
            return divisao



