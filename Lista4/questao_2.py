#Crie uma classe base chamada Veiculo com os seguintes atributos:
#• marca: marca do veículo (string)
#• modelo: modelo do veículo (string)
#• ano: ano de fabricação do veículo (int)
#A classe Veiculo deve ter os seguintes métodos:
#• acelerar(): exibe a mensagem "Acelerando o veículo!"
#• frear(): exibe a mensagem "Freando o veículo!"
#Crie três classes derivadas da classe Veiculo:


#• Carro: com os atributos adicionais:
#• cor: cor do carro (string) A classe Carro deve ter os seguintes métodos adicionais:
#• ligar_radio(): exibe a mensagem "Ligando o rádio do carro!"
#• abrir_porta(): exibe a mensagem "Abrindo a porta do carro!"

#• Moto: com os atributos adicionais:
#• cilindrada: cilindrada da moto (string) A classe Moto deve ter os seguintes métodos
#adicionais:
#• empinar(): exibe a mensagem "Empinando a moto!"
#• buzinar(): exibe a mensagem "Buzinando a moto!"

#• Caminhao: com os atributos adicionais:
#• carga_maxima: capacidade máxima de carga do caminhão (string) A classe
#Caminhao deve ter os seguintes métodos adicionais:
#• carregar(): exibe a mensagem "Carregando o caminhão!"
#• descarregar(): exibe a mensagem "Descarregando o caminhão!"

class Veiculo:

    def __init__(self, nome, modelo, ano):
        self.__marca = nome
        self.__modelo = modelo 
        self.__ano  = ano 

    def acelerar():
        print('Acelerando o veículo!')

    def frear():
        print('Freando o veículo!')

class Carro(Veiculo):
    def __init__(self, nome, modelo, ano, cor):
        super().__init__(nome, modelo, ano)
        self.__cor = cor

    def ligar_radio():
        print('Ligando o rádio do carro!')

    def abrir_porta():
        print('Abrindo a porta do carro!')

class Moto(Veiculo):
    def __init__(self, nome, modelo, ano, cilindrada):
        super().__init__(nome, modelo, ano)
        self.__cilindrada = cilindrada

    def empinar():
        print('Empinando a moto!')

    def buzinar():
        print('Buzinando a moto!')

class Moto(Veiculo):
    def __init__(self, nome, modelo, ano, carga_maxima):
        super().__init__(nome, modelo, ano)
        self.__cargar_maxima = carga_maxima

    def carregar():
        print('Carregando o caminhão!')

    def descarregar():
        print('Descarregando o caminhão!')


## TO DO - EFETUAR INSTANCIACOES E TESTES ABAIXO