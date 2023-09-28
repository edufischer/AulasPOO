from Album import Album

class Usuario:
    def __init__(self, nome=None, senha=None):
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

    def verificarLogin(self, nome, senha):
        if nome == self.__nome and senha == self.__senha:
            return True

    def getAlbum(self):
        return self.__album

    def configurarAlbum(self, album_serializado):
        # Implemente a lógica para configurar o álbum com os dados serializados
        pass    
    
    def serializar(self):
        dados = {
            'nome': self.__nome,
            'senha': self.__senha,
            'album': self.__album  # Chama o método serializar do álbum
        }
        return dados

    @classmethod
    def desserializar(self, dados):
        return self(
            nome=dados['nome'],
            senha=dados['senha'],
            album=dados['album']
        )



#serializado = o.serializar()
#print(serializado)