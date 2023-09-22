from Paginas import Pagina
from Figurinhas import Figurinha
from Trocas import Troca

class Album:
    def __init__(self):
        self.__paginas = Pagina()
        self.__figurinhas = Figurinha()
        self.__requisicoesTrocas = Troca()

