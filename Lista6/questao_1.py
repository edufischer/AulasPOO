# Classe base UnidadeMilitar
class UnidadeMilitar:

    def __init__(self, nome):
        self.nome = nome

    def mover(self):
        print(f"A unidade {self.nome} está se movendo.")

    def atacar(self):
        print(f"A unidade {self.nome} está atacando.")


# Classe derivada Soldado
class Soldado(UnidadeMilitar):

    def mover(self):
        print(f"O soldado {self.nome} está marchando.")

    def atacar(self):
        print(f"O soldado {self.nome} está empunhando sua espada.")


# Classe derivada Arqueiro
class Arqueiro(UnidadeMilitar):

    def mover(self):
        print(f"O arqueiro {self.nome} está correndo.")

    def atacar(self):
        print(f"O arqueiro {self.nome} está disparando sua flecha.")


# Classe derivada Cavaleiro
class Cavaleiro(UnidadeMilitar):

    def mover(self):
        print(f"O cavaleiro {self.nome} está cavalgando.")

    def atacar(self):
        print(f"O cavaleiro {self.nome} está golpeando com sua espada.")


# Criando instâncias de cada classe
soldado = Soldado("Soldado João")
arqueiro = Arqueiro("Arqueiro Pedro")
cavaleiro = Cavaleiro("Cavaleiro Paulo")

# Adicionando as instâncias à lista unidades
unidades = [soldado, arqueiro, cavaleiro]

# Percorrendo a lista unidades e chamando os métodos mover() e atacar()
for unidade in unidades:
    unidade.mover()
    unidade.atacar()