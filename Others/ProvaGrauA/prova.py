# QUESTAO A 
class Pizza:
    def __init__(self, nome, categoria, tipo, ingredientes):
        self.__nome = nome
        self.__categoria = categoria
        self.__tipo = tipo
        self.__ingredientes = ingredientes

    def imprimir_info(self):
        print(f"Nome: {self.__nome}. Categoria: {self.__categoria}. Tipo: {self.__tipo}. Ingredientes: {self.__ingredientes}\n")
        

class PizzaPedido:
    def __init__(self, tamanho, nro_sabores, lista_sabores, status):
        self.tamanho = tamanho
        self.nro_sabores = nro_sabores
        self.lista_sabores = lista_sabores
        self.status = status

    def imprimir_info(self):
        print(f"Tamanho: {self.tamanho}. Número de Sabores: {self.nro_sabores}. Lista de Sabores: {', '.join(self.lista_sabores)}. Status: {self.status}\n")
      

class SistemaPedidos:
    def __init__(self):
        self.__catalogo = []
        self.__listaDePedidos = []
        self.__contador_pedidos = 0

    def getListaDePedidos(self):
        return self.__listaDePedidos

    def adicionar_pedido(self):
        tamanho = input("Qual tamanhao da Pizza desejas? Escolha P, M ou G: ")
        tipo_da_pizza = input("Qual será o tipo da Pizza? Escolha Salgada ou Doce ").capitalize()
        nro_sabores = int(input("\nQuantos sabores desejas: : "))
        
        # pizza pequena até 2 sabores
        if tamanho == 'P':
            max_sabores = 2

        # pizza media até 3 sabores    
        elif tamanho == 'M':
            max_sabores = 3

        # pizza grande até 4 sabores
        elif tamanho == 'G':
            max_sabores = 4
        else:
            print("\nNão trabalhamos com este tamanho, infezlimente!")
            return
        
        if nro_sabores > max_sabores:
            print(f"\nNúmero máximo de sabores é de {max_sabores} sabores para esta pizza de {tamanho} tamanho.")
            return
        
        lista_sabores = []
        for i in range(nro_sabores):
            tipo = input("\n Queres adicionar um sabor Salgado ou Doce? ").capitalize()
            sabor = input(f"Escolha o sabor {i + 1}: ")

            # nao é permitido misturar sabores doces com salgado
            if sabor not in lista_sabores:
                lista_sabores.append(sabor)

            elif tipo_da_pizza == tipo:
                print("\nNão pode acrescentar dois tipos difentes de pizza, infelizmente!.")  
        
        status = "Recebido"

        # metodo retonar o numero do pedido(contador de pedidos)
        self.__contador_pedidos += 1

        pedido = PizzaPedido(tamanho, nro_sabores, lista_sabores, status)
        self.listaDePedidos.append(pedido)
        
        print(f"Pedido {self.__contador_pedidos} adicionado com sucesso!")

    def exibir_catalogo(self):
        print("Catálogo de Pizzas:")
        for pizza in self.__catalogo:
            pizza.imprimir_info()

    def alterar_status_pedido(self, numero_pedido, novo_status):
        if numero_pedido >= 1 and numero_pedido <= len(self.listaDePedidos):
            pedido = self.__listaDePedidos[numero_pedido - 1]
            pedido.status = novo_status
            print(f"O Status do Pedido {numero_pedido} foi alterado para {novo_status}.")
        else:
            print("Número do pedido fornecdo é inválido!")

    def exibir_lista_de_pedidos(self):
        print("Lista de Pedidos:")
        for i, pedido in len(self.listaDePedidos):
            print(f"O Pedido de número {i}:\n")
            pedido.imprimir_info()

# QUESTAO B - INSTANCIANDO OBJETOS
listaParaCatalogo = [
    Pizza("Margherita", "Salgada", "Vegetariana", "Muçarela, Tomate, Manjericão"),
    Pizza("Pepperoni", "Salgada", "Com Carne", "Pepperoni, Muçarela"),
    Pizza("Quatro Queijos", "Salgada", "Vegetariana", "Muçarela, Gorgonzola, Parmesão, Provolone"),
    Pizza("Portuguesa", "Salgada", "Com Carne", "Presunto, Muçarela, Ovo, Ervilhas, Azeitonas"),
    Pizza("Calabresa", "Salgada", "Com Carne", "Calabresa, Muçarela"),
    Pizza("Frango com Catupiry", "Salgada", "Com Carne", "Frango, Catupiry, Muçarela"),
    Pizza("Banana Caramelizada", "Doce", "Vegetariana", "Banana, Creme de Leite Condensado, Canela"),
    Pizza("Chocolate com Morango", "Doce", "Vegetariana", "Chocolate, Morango"),
    Pizza("Vegetariana", "Salgada", "Vegetariana", "Milho, Ervilhas, Pimentão, Tomate Cereja, Muçarela"),
    Pizza("Supreme", "Salgada", "Com Carne", "Pepperoni, Calabresa, Muçarela, Cebola, Pimentão, Azeitonas")
]

# INSTANCIANDO SISTEMA DE PEDIDOS
print('\n############################################################################\n')
print('Bem vindo(a) a Pizzaria Hot. Faça seu pedido direto pelo terminal abaixo: \n')
sistema = SistemaPedidos()
sistema.catalogo = listaParaCatalogo
sistema.adicionar_pedido()

# QUESTAO C

pedidosParaTestar = [
    [1, 'M', 2, ['Margherita', 'Calabresa'], 'Entregue'],
    [2, 'P', 2, ['Banana Caramelizada', 'Chocolate com Morango'], 'Pronto'],
    [3, 'G', 3, ['Vegetariana', 'Supreme', 'Pepperoni'], 'Entregue'],
    [4, 'P', 1, ['Frango com Catupiry'], 'Em preparo'],
    [5, 'G', 4, ['Quatro Queijos', 'Frango com Catupiry', 'Portuguesa', 'Bacon'], 'Pronto'],
    [6, 'M', 3, ['Margherita', 'Calabresa', 'Pepperoni'], 'Em preparo'],
    [7, 'G', 1, ['Bacon'], 'Recebido'],
    [8, 'P', 2, ['Margherita', 'Calabresa'], 'Em preparo'],
    [9, 'G', 2, ['Mussarela', 'Portuguesa'], 'Em preparo'],
    [10, 'M', 3, ['Quatro Queijos', 'Margherita', 'Frango com Catupiry'], 'Recebido']
]

print('\n############################################################################\n')
print('Inicizando impressoes da questão C: ')

sistema.alterar_status_pedido(2, "Em preparo")
sistema.alterar_status_pedido(6, "Entregue")
sistema.alterar_status_pedido(12, "Recebido")
