# Incluir bibliotecas/módulos

import os #para chamar comandos do sistema


# Funções

def Iniciar():
    print('Iniciando o programa...')
    # Carregar ou ler dados de entrada


def EscolherOpcao():
    print('1 -Opção 1')
    print('2 -Opção 2')
    print('3 -Opção 3')
    print('0 -Sair\n')
    resposta = input('Escolha uma opção: ')
    os.system('cls'if os.name== 'nt'else'clear')
    return resposta

def ExecutarAcao1(): # Observação 1 : estas funções podem ter parâmetros, ou seja, receber 
    # informações (dados) necessários para sua execução
    print('Executando a ação 1...')
    # Observação 2: estas funções podem retornar valores, de acordo com seu propósito

def ExecutarAcao2(): 
    print('Executando a ação 2...')

def ExecutarAcao3(): 
    print('Executando a ação 3...')

def Executar():
    terminarExecucao = False
    while not terminarExecucao: # enquanto terminar execucao for falso vai ficar no looping
        acaoUsuario = EscolherOpcao()
        if (acaoUsuario == '1'):
            ExecutarAcao1()
        elif (acaoUsuario == '2'):
            ExecutarAcao2()
        elif (acaoUsuario == '3'):
            ExecutarAcao3()
        elif (acaoUsuario == '0'):
            terminarExecucao = True #terminarExecucao é falso, logo vai sair do loop no proximo giro.
        else:
            print('Escolha invalida!Tente de novo.')


def Finalizar():
    print('O programa foi encerrado!')
    # Salvar dados, encerrar processos etc

# Programa principal
if __name__ == '__main__':
    Iniciar()
    Executar()
    Finalizar()