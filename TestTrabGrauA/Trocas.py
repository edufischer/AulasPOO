class Troca:
    def __init__(self, nomeProponente=None, figurinhaRequerida=None, figurinhaDisponivel=None):
        self.__remetente = nomeProponente
        self.__figurinha_oferecida = figurinhaRequerida
        self.__figurinha_desejada = figurinhaDisponivel
        # 0 = aguardando; 1 (aceita); 2(recusada)
        self.__status = int

    def aceitar(bool):
        pass