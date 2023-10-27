class FiguraGeometrica():
    def __init__(self, nome):
        self.__nome = nome
        
    def calcularArea(self):
        pass
    
    def calcularPerimetro(self):
        pass
    
class Retangulo(FiguraGeometrica):
    def __init__(self, nome=None, base=0, altura=0):
        super().__init__(nome)
        self.__base = base
        self.__altura = altura 
        
    def calcularArea(self):
        area = int(self.__base) * int(self.__altura)
        return area
    
    def calcularPerimetro(self):
        perimetro = 2 * (self.__base * self.__altura)
        return perimetro

class Triangulo(FiguraGeometrica):
    def __init__(self, nome=None, base=0, altura=0):
        super().__init__(nome)
        self.__base = base
        self.__altura = altura 
        
    def calcularArea(self):
        area = (int(self.__base) * int(self.__altura)) / 2
        return area
    
    def calcularPerimetro(self):
        pass    

class Circulo(FiguraGeometrica):
    pi = 3.14
    def __init__(self, nome=None, raio=0):
        super().__init__(nome)
        self.__raio = raio

    def calcularArea(self):
        area = ((self.__raio)**2) * Circulo.pi
        return area 

    def calcularPerimetro(self):
        pass
    
# Testes:

retangulo1 = Retangulo(base=2, altura=4)
circulo1 = Circulo(raio=2)
triangulo1 = Triangulo(base=6,altura=12)

print(retangulo1.calcularArea())
print(circulo1.calcularArea())
print(triangulo1.calcularArea())
