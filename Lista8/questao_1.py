import random

# Classe base Animal
class Animal:

    def __init__(self, nome):
        self.nome = nome

    def exibirDescricao(self):
        print(f"O animal {self.nome} é um animal.")


# Classe derivada Carnivoro
class Carnivoro(Animal):

    def caçar(self):
        print(f"O animal {self.nome} está caçando.")

    def exibirDescricao(self):
        super().exibirDescricao()
        print(f"O animal {self.nome} é um animal carnívoro.")


# Classe derivada Herbivoro
class Herbivoro(Animal):

    def pastar(self):
        print(f"O animal {self.nome} está pastando.")

    def exibirDescricao(self):
        super().exibirDescricao()
        print(f"O animal {self.nome} é um animal herbívoro.")


# Classe derivada Onivoro
class Onivoro(Carnivoro, Herbivoro):

    def comer(self):
        numero = random.randint(0, 1)
        if numero == 0:
            self.caçar()
        else:
            self.pastar()

    def exibirDescricao(self):
        super().exibirDescricao()
        print(f"O animal {self.nome} é um animal onívoro.")




# Exemplo de uso
animal = Animal("Lobo")
animal.exibirDescricao()  # O animal Lobo é um animal.

carnivoiro = Carnivoro("Leão")
carnivoiro.exibirDescricao()  # O animal Leão é um animal carnívoro.
carnivoiro.caçar()  # O animal Leão está caçando.

herbivoro = Herbivoro("Vaca")
herbivoro.exibirDescricao()  # O animal Vaca é um animal herbívoro.
herbivoro.pastar()  # O animal Vaca está pastando.

onivoro = Onivoro("Urso")
onivoro.exibirDescricao()  # O animal Urso é um animal onívoro.
onivoro.comer()  # O animal Urso está caçando.


