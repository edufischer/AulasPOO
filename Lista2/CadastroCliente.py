#Crie uma classe CadastroCliente com os atributos nome, sobrenome, data de nascimento, email,
#CPF e senha. Faça um pequeno programa que permita o cliente se cadastrar e depois consultar
#seus dados. Para consultar seus dados, é necessário que ele faça o login com seu email e senha.
#Se o cliente errar a senha 3x, o cadastro é bloqueado e ele não pode mais acessar

class CadastroCliente:

    def __init__(self, nome=None, sobrenome=None, data_nascimento=None, email=None, cpf=None, senha=None):
        self.nome = nome
        self.sobrenome = sobrenome  
        self.data_nascimento = data_nascimento
        self.email = email
        self.cpf = cpf
        self.senha = senha
        self.cadastrado = False

    def consultar_dados(self):
        contador = 0
        while contador < 3:

            login = input('Digite seu login (email): ')
            senha = input('Digite sua senha: ')

            if login != self.email or senha != self.senha:
                print('Login ou senha inválido(a)! Tente novamente.')
                contador += 1

            elif login == self.email and senha == self.senha:
                print('Seu nome é: \n',self.nome)
                print('Seu sobrenome é: \n',self.sobrenome)
                print('Seu data de nascimento é: \n',self.data_nascimento)
                print('Seu email é \n',self.email)
                print('Seu cpf é: \n',self.cpf)
                print('Seu senha é: \n',self.senha)
                break


    def cadastrar(self):
        if self.cadastrado == True:
            print('Usuário já está cadastrado!')
        
        else:
            nome_user = input('Digite seu primeiro nome: ')
            sobrenome_user = input('Digite seu segundo nome: ')
            data_nascimento_user = input('Digite sua data de nascimento: ')
            email_user = input('Digite seu melhor email: ')
            cpf_user = input('Digite seu CPF ')
            senha_user = input('Crie sua senha: ')

        self.nome = nome_user
        self.sobrenome = sobrenome_user  
        self.data_nascimento = data_nascimento_user
        self.email = email_user
        self.cpf = cpf_user
        self.senha = senha_user
        self.cadastrado = True


user1 = CadastroCliente()
user1.cadastrar()
user1.consultar_dados()
