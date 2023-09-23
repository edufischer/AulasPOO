from Figurinhas import Figurinha

class Pagina:
    def __init__(self):
        self.figurinhas = []
        self.titulo = 0
        self.minNro = 1
        self.maxNro = 133

    # Verifica se o argumento é uma instância do tipo 'type'
    def verificarTipo(self, tipo):
        if isinstance(tipo, type):
            # Cria uma instância do tipo especificado
            objeto = tipo()
            return objeto
        else:
            raise ValueError("O argumento deve ser um tipo 'type' válido")
