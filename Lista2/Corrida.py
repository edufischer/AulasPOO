from Dado import Dado
class Competidor:
    def __init__(self, nome):
        self.nome = nome
        self.pos = 0

    def atualizar(self):
        dado = Dado(6) 
        rolagemDado = dado.rolarDadoSeisLados()
        self.pos += int(rolagemDado)

        # VERIFICA AS REGRAS
        if self.pos % 5 == 0:
            self.pos -= 1
        elif self.pos in [7, 17]:
            self.pos += 2
        elif self.pos == 13:
            self.pos = 0

        return self.pos

def corrida():
    competidores = [
        Competidor("Eduardo"),
        Competidor("João"),
        Competidor("Pedro"),
        Competidor("Roberto"),
        Competidor("Zéca")
    ]

    vencedor = None
    rodada = 0

    while not vencedor:
        rodada += 1
        print(f"Rodada {rodada}:")

        for competidor in competidores:
            posicao = competidor.atualizar()
            print(f"{competidor.nome} está na posição {posicao}")

            if posicao >= 20:
                vencedor = competidor
                break

    print(f"\nO vencedor da partida é o competidor{vencedor.nome}!")

# INICIO DO PROGRAMA
if __name__ == "__main__":
    corrida()
