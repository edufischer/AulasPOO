# Classe base Assinatura
class Assinatura:

    def __init__(self, tipo):
        self.tipo = tipo

    def calcular_preco(self):
        raise NotImplementedError("O método calcular_preco() deve ser implementado nas subclasses.")

    def exibir_detalhes(self):
        raise NotImplementedError("O método exibir_detalhes() deve ser implementado nas subclasses.")


# Classe derivada AssinaturaSimples
class AssinaturaSimples(Assinatura):

    def calcular_preco(self):
        return 29.99

    def exibir_detalhes(self):
        print(f"Assinatura Simples: acesso a filmes e séries em qualidade padrão.")


# Classe derivada AssinaturaPremium
class AssinaturaPremium(Assinatura):

    def calcular_preco(self):
        return 49.99

    def exibir_detalhes(self):
        print(f"Assinatura Premium: acesso a filmes e séries em qualidade HD e Ultra HD.")


# Criando instâncias das assinaturas
assinatura_simples = AssinaturaSimples("Simples")
assinatura_premium = AssinaturaPremium("Premium")

# Criando um array de assinaturas
assinaturas = [assinatura_simples, assinatura_premium]

# Percorrendo o array de assinaturas
for assinatura in assinaturas:
    print(f"Tipo de assinatura: {assinatura.tipo}")
    print(f"Preço: {assinatura.calcular_preco()}")
    assinatura.exibir_detalhes()