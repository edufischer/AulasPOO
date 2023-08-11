import random

baseDeDados = [
    ['Fa fe fi fo Funk',	'Anira', 'Funk', 2019, '3:05'],
    [ 'Sofrência de programar', 'Ada & Turing',	'Sertanejo', 1998, '2:58' ],
    [ 'Rock’n Rolo', 'The Buns','Rock',	1984, '4:01' ],
    [ 'Grifinoria Girls', 'Katy Potter', 'Pop',	2017, '2:25' ],
    ['Outra musica', 'Anira', 'Funk', 2019, '3:05']
]

def ExibirBaseDados():
    id = 0
    for i in baseDeDados:
        for j in i:
            print (id, '\t',j, end = '\t')
        id = id + 1
        print() #quebra de linha

# a) Visualizar base de dados: se escolhida esta opção, o programa deve mostrar ao usuário a tabela com todas as músicas
ExibirBaseDados()

#TO-DO
# TENTAR FAZER LISTA DE REVISÃO (NÃO PRECISA ENTREGAR)