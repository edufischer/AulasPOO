class Album:
    def __init__(self,paginas=100,figurinhas=200,requisicoesTrocas=None):
        self.__paginas = paginas
        self.__figurinhas = figurinhas
        self.__requisicoesTrocas = requisicoesTrocas

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

    #def serializar(self):
    #    dados = {
    #        'paginas': self.__paginas.serializar(),
    #        'figurinhas': self.__figurinhas.serializar(),
    #        'requisicoesTrocas': self.__requisicoesTrocas.serializar()
    #    }
    #    return dados

    #@classmethod
    #def desserializar(cls, dados):
    #    album = cls()
    #    album.setPaginas(Pagina.desserializar(dados['paginas']))
    #    album.setFigurinhas(Figurinha.desserializar(dados['figurinhas']))
    #    album.setRequisicoesTrocas(Troca.desserializar(dados['requisicoesTrocas']))
    #    return album