import random #para utilizar na funcao de criar dados aleatorios
import os #para chamar comandos do sistema

class Data:
    # Caso não receba nenhum parametro, sera usados os estipulados na criacao do construtor.
    def __init__(self, dia=4, mes=4, ano=1998):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def imprimirData(self):
        print(f"\nImprimindo na tela a data completa: {self.dia}/{self.mes}/{self.ano}.")

    def imprimirDataPorExtenso(self, cidade="Canoas"):
        meses = [None,'Janeiro','Feveiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
        
        print(f"\nA data na cidade {cidade} é {self.dia} de {meses[self.mes]} de {self.ano}.\n")

    def instanciarObjetoProprio():
        while True:
            dia_digitado = input('Digite o dia com dois dígitos: ')
            if len(dia_digitado) >= 2:
                dia_usuario = int(dia_digitado)
                break
            else:
                print("Por favor, digite um dia válido. Por exemplo, 02.")
        while True:
            mes_digitado = input('Digite o mês com dois dígitos: ')
            if len(mes_digitado) >= 2 and int(mes_digitado) < 31:
                mes_usuario = int(mes_digitado)
                break
            else:
                print("Por favor, digite um mês válido. Por exemplo, 04.")
        while True:
            ano_digitado = input('Digite o ano com quatro dígitos: ')
            if len(ano_digitado) == 4:
                ano_usuario = int(ano_digitado)
                break
            else:
                print("Por favor, digite um ano válido. Por exemplo, 1998.")

        cidade_usuario = input('Digite o nome da cidade: ')

        #Intanciação de um objeto da classe Data com valores passados pelo usuario:
        print('\nCriando um objeto da classe Data logo abaixo e chamando seus métodos: ')
        data_usuario = Data(dia_usuario, mes_usuario, ano_usuario)
        data_usuario.imprimirData()
        data_usuario.imprimirDataPorExtenso(cidade_usuario)

    
    #Chamando a funçao que efetuara a inntanciação de um objeto da classe Data com valores aleoatórios:
    def instanciarObjetoAleatorio(): 
        cidade_usuario = input('Digite o nome da cidade: ')
        dia_aleatorio = random.randint(1, 31)
        mes_aleatorio = random.randint(1, 12)
        ano_aleatorio = random.randint(1800, 2023)
        print('\nCriando um objeto da classe Data logo abaixo e chamando seus métodos: ')
        data_aleatoria = Data(dia_aleatorio, mes_aleatorio, ano_aleatorio)
        data_aleatoria.imprimirData()
        data_aleatoria.imprimirDataPorExtenso(cidade_usuario)
    
    #Chamando a funçao que efetuara a inntanciação de um objeto da classe Data com valores personalizados
    def instanciarObjetoPadrao():
        print('\nCriando um objeto da classe Data logo abaixo e chamando seus métodos: ')
        data_padrao = Data()
        data_padrao.imprimirData()
        data_padrao.imprimirDataPorExtenso()
        print('Estas informações acima são sobre o developer que criou este código e deixou elas como default no construtor da classe.')



# Programa abaixo

def EscolherOpcao():
    print('''
##########################################################################
        \n Bem vindo(a) ao gerador de datas! O que você deseja fazer?\n
        1) Gerar a própria data.
        2) Gerar a data aleatóriamente.
        3) Gerar a data padrão estipulada pelo DEV.
        0 - Sair\n''')
    resposta = input('Escolha uma opção: ')
    os.system('cls'if os.name== 'nt'else'clear')
    return resposta

def Executar():
    terminarExecucao = False
    while not terminarExecucao:
        acaoUsuario = EscolherOpcao()
        if (acaoUsuario == '1'):
            Data.instanciarObjetoProprio()
        elif (acaoUsuario == '2'):
            Data.instanciarObjetoAleatorio()
        elif (acaoUsuario == '3'):
            Data.instanciarObjetoPadrao()
        elif (acaoUsuario == '0'):
            terminarExecucao = True 
        else:
            print('Escolha invalida!Tente de novo.')

def Finalizar():
    print('O programa foi encerrado!')

# Programa principal
if __name__ == '__main__':
    Executar()
    Finalizar()



