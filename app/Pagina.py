class Pagina:
    def __init__(self,titulo,figurinhas):
        self.__figurinhas = figurinhas
        self.__titulo = titulo
        self.__minNro = 1
        self.__maxNro =  5
      

    def serializar(self):
        dados = {
            'figurinhas': self.__figurinhas,
            'titulo': self.__titulo,
            'minNro': self.__minNro,
            'maxNro': self.__maxNro,
        }
        return dados

    @classmethod
    def desserializar(self, dados):
        return self(
            numero=dados['figurinhas'],
            nome=dados['titulo'],
            conteudo=dados['minNro'],
            status=dados['maxNro'],
        )
    
    def setTitulo(self,titulo):
        self.__titulo = titulo
    
    def getTitulo(self):
        return self.__titulo 
    
    def getFigurinhas(self):
        return self.__figurinhas
    
    def setFigurinhas(self,figurinhas):
        self.__figurinhas = figurinhas
    

