class Figurinha:
    def __init__(self, numero=None, nome=None, conteudo=None, status=None):
        self.__numero = numero
        self.__nome = nome
        self.__conteudo = conteudo
        # 0 = na colecao; 1 = colada no album; 2 = disponivel pra troca
        self.__status = status
        self.nroPaginas = 0

    # Verifica se o argumento é uma instância do tipo 'type'
    def verificarTipo(self, tipo):
        if isinstance(tipo, type):
            # Cria uma instância do tipo especificado
            objeto = tipo()
            return objeto
        else:
            raise ValueError("O argumento deve ser um tipo 'type' válido")
        






