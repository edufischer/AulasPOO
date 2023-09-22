from Album import Album

class Usuario:
    def __init__ (self, nome=None, senha=None, album=None):
        self.__nome = nome
        self.__senha = senha
        self.__album = Album()

    def getNomeDeUsuario(self):
        return self.__nome
    
    def getSenhaDeUsuario(self):
        return self.__senha
    
    def cadastrar(self, nome, senha):
        self.__nome = nome
        self.__senha = senha
        return self
    
    def verificarLogin(self, nome, senha):
        if nome == self.__nome and senha == self.__senha:
            return True
        else: return False

    def getAlbum (self):
        return self.__album
    
    
