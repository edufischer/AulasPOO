#Definição da classe Mago 
class Mago:
    # Atributos de classe
    possuiMagia = True

    # Método construtor
    def __init__(self, nome, idade, escola, qnt_de_mana, qnt_de_hp):
        # Atributos de instância
        self.nome = nome 
        self.idade = idade   
        self.escola = escola 
        self.qnt_de_mana = qnt_de_mana
        self.qnt_de_hp = qnt_de_hp
        print(f'\nMago {self.nome} foi criado!')

    # Outros métodos    
    def andar(self):
        print(f'\nO Mago {self.nome} está andando')
    
    def falar(self):
        print(f'\nOla amigue! Meu nome é {self.nome}')
        
    def invocarMagia(self):
        print(f'\nInvocando magia do Mago {self.nome}!')

    def verificarMana(self):
        print(f'\nO Mago {self.nome} está com {self.qnt_de_mana} de mana para utilzar.')

    def verificarVida(self):
        print(f'\nO Mago {self.nome} está com {self.qnt_de_hp}% de vida.')    

    # Método destrutor
    def __del__(self):  
        print(f'\nO Mago {self.nome} deixou de existir!') 
        
        
#Intanciação de um objeto da classe Mago
mj = Mago('Magnus Jhon', 17, 'Hogwarts', 100, 60)
pd = Mago('Phoenix Dark', 2000, 'Magia Cinza',60, 80)
zz = Mago('Zephyr Zan', 24, 'Unisinos', 40, 100)

#Invocando métodos
mj.andar()
mj.falar()
mj.invocarMagia()
mj.verificarMana()
mj.verificarVida()

pd.andar()
pd.falar()
pd.invocarMagia()
pd.verificarMana()
pd.verificarVida()

zz.andar()
zz.falar()
zz.invocarMagia()
zz.verificarMana()
zz.verificarVida()


del mj
del pd
del zz


