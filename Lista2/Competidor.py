import os
from Dado import Dado

dado = Dado(6)
numeroCasas = 20

class Competidor:
    


    def __init_(self, nome):
        self.nome = nome
        self.pos = 0

    def atualizar(self):

        resultadoDado = dado.rolar()
        print(f"Jogador {self.nome} rolou o dado e tirou: {resultadoDado}")
        if resultadoDado % 5 == 0:
            self.diminuiPos(1)
            print(f'Como o jogador {self.nome} tirou {resultadoDado} no dado. Logo, ele voltará uma casa no tabuleiro.')
        elif resultadoDado == 7 or resultadoDado == 17:
            self.aumentaPos(2)
            print(f'Como o jogador {self.nome} tirou {resultadoDado} no dado. Logo, ele andará duas casas no tabuleiro.')
        elif resultadoDado == 13: 
            self.pos()
            print(f'Como o jogador {self.nome} tirou {resultadoDado} no dado. Logo, ele voltará ao inicio no tabuleiro.')

        print(f'O jogador {self.nome} esta na posição {self.pos} no tabuleiro agora.')

        if self.venceu() == True: print(f"Jogador {self.nome} ganhou a corrida!")
    
    def setNome(self,nome):
        self.nome = nome

    def getPos(self):
        return self.pos
    
    def aumentaPos(self, pos):
        self.pos = self.pos + pos

    def diminuiPos(self, pos):
        self.pos = self.pos - pos 
    
    def zeraPos(self):
        self.pos = 0

    def venceu(self):
        if self.getPos() == numeroCasas or self.getPos() > numeroCasas:
            return True
        



# vencedor posicao > numeroCasas



"""""
o Se passar de 20, não tem problema (deve-se sinalizar que a corrida terminou e
guardar o índice do competidor vencedor)
Após chamar o método atualizar de um competidor, deve-se em seguida verificar se ele venceu a
corrida. Se positivo, a corrida termina imediatamente (termina a rodada).
Ao fim de cada rodada, deve-se imprimir o nome e posição atual de cada jogador. Ao final da
corrida, deve-se imprimir o nome do vencedor.

"""


#TRABALHO
#arquivo info do user = nome...
#arquivo info do album = 
#arquivo 



# Programa abaixo
listaObjetos = []

def iniciar():
    print()
    print('Iniciando o programa...')

def setandoPartida():
    listaObjetos = []
    contador = 0
    numPlayer = input("Quantos players jogarão está partida? Digite o número: ")
    while contador != int(numPlayer):
        nome = input(f"Digite o nome do player {contador+1}: ")
        jogador = Competidor()
        jogador.setNome(nome)
        listaObjetos.append(jogador)
        contador += 1

def partidaEmAndamento():


    #### TO DO 
    while True:
        for i in listaObjetos:
            listaObjetos[i].atualizar()
            if listaObjetos[i].venceu() is True: break





def escolherOpcao():
    print()
    print('1 - Iniciar Corrida Maluca')
    print('0 -Sair\n')
    resposta = input('Escolha uma opção: ')
    os.system('cls'if os.name== 'nt'else'clear')
    return resposta

def executar():
    terminarExecucao = False
    while not terminarExecucao: # enquanto terminar execucao for falso vai ficar no looping
        acaoUsuario = escolherOpcao()
        if (acaoUsuario == '1'):
            setandoPartida()
            print('Carregando a partida embassada nos dados passados por você...')
            partidaEmAndamento()

        elif (acaoUsuario == '0'):
            terminarExecucao = True #terminarExecucao é falso, logo vai sair do loop no proximo giro.
        else:
            print('Escolha invalida!Tente de novo.')

def finalizar():
    print('O programa foi encerrado!')
    # Salvar dados, encerrar processos etc

# Programa principal
if __name__ == '__main__':
    iniciar()
    executar()
    finalizar()