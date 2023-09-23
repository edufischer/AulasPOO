class Figurinha:
    def __init__(self, numero=None, nome=None, conteudo=None, status=0):
        self.__numero = numero
        self.__nome = nome
        self.__conteudo = conteudo
        # 0 = na coleção; 1 = colada no álbum; 2 = disponível para troca
        self.__status = status
        self.nroPaginas = 0

    def getNumero(self):
        return self.__numero

    def getNome(self):
        return self.__nome

    def getConteudo(self):
        return self.__conteudo

    def getStatus(self):
        return self.__status

    def setNumero(self, numero):
        self.__numero = numero

    def setNome(self, nome):
        self.__nome = nome

    def setConteudo(self, conteudo):
        self.__conteudo = conteudo

    def setStatus(self, status):
        self.__status = status

    def verificarTipo(self, tipo):
        if isinstance(tipo, type):
            objeto = tipo()
            return objeto
        else:
            raise ValueError("O argumento deve ser um tipo 'type' válido")
