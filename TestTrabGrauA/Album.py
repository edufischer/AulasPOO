from Paginas import Pagina
from Figurinhas import Figurinha
from Trocas import Troca

class Album:
    def __init__(self, paginas=0, figurinhas=0, requisicoesTrocas=0):
        self.__paginas = []
        self.__figurinhas = []
        self.__requisicoesTrocas = 0

    def getPaginas(self):
        return self.__paginas
    
    def getFigurinhas(self):
        return self.__figurinhas
    
    def getRequisicoesTrocas(self):
        return self.__requisicoesTrocas

    def setPaginas(self, paginas):
        self.__paginas = paginas
    
    def setFigurinhas(self, figurinhas):
        self.__figurinhas = figurinhas
    
    def setRequisicoesTrocas(self, requisicoesTrocas):
        self.__requisicoesTrocas = requisicoesTrocas

    def serializar(self):
        # Serializa os atributos como um dicionário
        dados = {
            'paginas': self.__paginas,
            'figurinhas': self.__figurinhas,
            'requisicoesTrocas': self.__requisicoesTrocas
        }
        return dados

    @classmethod
    def deserializar(cls, dados):
        # Cria uma instância de Album a partir dos dados serializados
        return cls(
            paginas=dados['paginas'],
            figurinhas=dados['figurinhas'],
            requisicoesTrocas=dados['requisicoesTrocas']
        )
