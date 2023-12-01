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
class Onivoro(Animal):

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


## ====================================================================================================================

import random

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def exibirDescricao(self):
        print(f"Nome do animal: {self.nome}")

class Carnivoro(Animal):
    def cacar(self):
        print(f"{self.nome} está caçando.")

    def exibirDescricao(self):
        super().exibirDescricao()
        print("É um animal carnívoro.")

class Herbivoro(Animal):
    def pastar(self):
        print(f"{self.nome} está pastando.")

    def exibirDescricao(self):
        super().exibirDescricao()
        print("É um animal herbívoro.")

class Onivoro(Carnivoro, Herbivoro):
    def comer(self):
        escolha = random.randint(0, 1)
        if escolha == 0:
            self.cacar()
        else:
            self.pastar()

    def exibirDescricao(self):
        super().exibirDescricao()
        print("É um animal onívoro.")

# Exemplo de uso
animal_carnivoro = Carnivoro("Leão")
animal_carnivoro.exibirDescricao()
animal_carnivoro.cacar()

animal_herbivoro = Herbivoro("Zebra")
animal_herbivoro.exibirDescricao()
animal_herbivoro.pastar()

animal_onivoro = Onivoro("Urso")
animal_onivoro.exibirDescricao()
animal_onivoro.comer()