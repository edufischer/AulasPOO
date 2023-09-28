class Figurinha:
    def __init__(self, numero=None, nome=None, conteudo=None, status=0, nroPagina=0):
        self.__numero = numero
        self.__nome = nome
        self.__conteudo = conteudo
        self.__status = status  # 0 = na coleção; 1 = colada no álbum; 2 = disponível para troca
        self.nroPagina = nroPagina

    def serializar(self):
        dados = {
            'numero': self.__numero,
            'nome': self.__nome,
            'conteudo': self.__conteudo,
            'status': self.__status,
            'nroPagina': self.nroPagina
        }
        return dados

    @classmethod
    def desserializar(self, dados):
        return self(
            numero=dados['numero'],
            nome=dados['nome'],
            conteudo=dados['conteudo'],
            status=dados['status'],
            nroPagina=dados['nroPagina']
        )
    
    def setStatus(self,status):
        self.__status = status
    
    def getStatus(self):
        return self.__status 
    
    def getNumero(self):
        return self.__numero 
    

