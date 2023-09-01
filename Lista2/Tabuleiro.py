from Dado import Dado

class Tabuleiro:
    dado = Dado(6)
    
    def __init_(self, nome):
        self.nome = nome
        self.casas = 20

    def atualizar(self):
        pass # atualiza a posicao de acordo com as regras descritas abaixo

    def getPos(self):
        return self.pos
    
"""
Para isso, você deve inicializar cada competidor com seu nome (a posição de todos começa em
zero). A corrida acontece enquanto nenhum dos competidores tiver vencido - chegado ao fim (pos
> 20). A cada ciclo, deve-se chamar o método atualizar de cada competidor. Neste método, a
posição do competidor é atualizada da seguinte maneira:
• Sorteia-se um número de 1 a 6 (simulando um dado)
• A posição do competidor avança o número sorteado de casas no tabuleiro, respeitando as
seguintes regras:
o Se cair em uma casa com número múltiplo de 5, deve-se recuar 1 casa
o Se cair nas casas de número 7 ou 17, avança 2 casas
o Se cair na casa de número 13, volta ao início (pos = 0)
o Se passar de 20, não tem problema (deve-se sinalizar que a corrida terminou e
guardar o índice do competidor vencedor)
Após chamar o método atualizar de um competidor, deve-se em seguida verificar se ele venceu a
corrida. Se positivo, a corrida termina imediatamente (termina a rodada).
Ao fim de cada rodada, deve-se imprimir o nome e posição atual de cada jogador. Ao final da
corrida, deve-se imprimir o nome do vencedor.

"""