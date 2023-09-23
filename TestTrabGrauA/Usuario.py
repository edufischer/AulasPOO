from Album import Album
import csv


class Usuario:
    def __init__ (self, nome=None, senha=None):
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
       if self.__nome == nome and self.__senha == senha:
           return True
       else: return False

    def getAlbum (self):
        return self.__album
    
    def serializar(self):
        dados = []
        dados.append(self.__nome)
        dados.append(self.__senha)
        album_serializado = self.__album.serializar()  # Serialize o álbum
        dados.append(album_serializado)  # Adicione a representação serializada do álbum
        strUsuario = ','.join(map(str, dados)) + '\n'
        return strUsuario
    
    def setAlbum(self, album):
        self.__album = album


