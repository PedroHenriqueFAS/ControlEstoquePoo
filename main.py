class Estoque:
    def __init__(self, nome, capacidade_maxima):
        self.nome = nome
        self.espaco = capacidade_maxima
        self.produtos = {}
        self.endereco = ''
        
    def add_produto(self, id, nome, quantidade):
        if id in self.produtos:
            self.produtos[id][nome] += quantidade
        else:
            self.produtos[id] = {nome:quantidade}
        self.espaco -= quantidade

e1 = Estoque('Amazon', 1000)
e2 = Estoque('Americanas', 800)

e1.add_produto('20', 'Caneta', 30)
print(e1.produtos)
print(e1.espaco)