"""

Desenvolva uma classe base chamada Criptografia que contenha os métodos cifrar e decifrar. Essa
classe servirá como base para as subclasses CifraCesar e CifraXor, que implementarão algoritmos
de criptografia específicos.

A classe Criptografia terá os seguintes métodos:

• Método cifrar(texto): Este método receberá um texto como entrada e retornará o texto
cifrado de acordo com o algoritmo de criptografia. Cada subclasse irá implementar sua
própria lógica de cifragem.

• Método decifrar(texto_cifrado): Este método receberá um texto cifrado como entrada e
retornará o texto original decifrado de acordo com o algoritmo de criptografia
correspondente.

A classe CifraCesar herda da classe Criptografia e implementa o algoritmo de criptografia conhecido
como Cifra de César. A Cifra de César desloca cada letra do texto original um número fixo de posições
no alfabeto para cifrar e decifrar o texto.

A classe CifraXor herda da classe Criptografia e implementa o algoritmo de criptografia usando a
operação XOR (OU exclusivo). Nesse algoritmo, cada caractere do texto original é combinado com uma
chave usando a operação XOR para obter o texto cifrado. A operação XOR também é usada para decifrar
o texto cifrado, combinando-o novamente com a mesma chave.

Os métodos cifrar e decifrar de cada subclasse devem ser implementados de acordo com a lógica
específica de cada algoritmo de criptografia.


"""
from abc import ABC, abstractmethod

class Criptografia(ABC):

    @abstractmethod
    def cifrar(self, texto):
       pass 
    
    @abstractmethod
    def decifrar(self, texto_cifrado):
       pass 

class CifraCesar(Criptografia):
    def __init__(self, chave):
        self.chave = chave

    def cifrar(self, texto):
        texto_cifrado = ''
        for char in texto:
            if char.isalpha():
                if char.islower():
                    texto_cifrado += chr((ord(char) - ord('a') + self.chave) % 26 + ord('a'))
                elif char.isupper():
                    texto_cifrado += chr((ord(char) - ord('A') + self.chave) % 26 + ord('A'))
            else:
                texto_cifrado += char
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        return self.cifrar(texto_cifrado)
    
class CifraXor(Criptografia):
    def __init__(self, chave):
        self.chave = chave

    def cifrar(self, texto):
        texto_cifrado = ''
        for char in texto:
            texto_cifrado += chr(ord(char) ^ self.chave)
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        return self.cifrar(texto_cifrado)
    

# TO DO INSTANCIAR E TESTES