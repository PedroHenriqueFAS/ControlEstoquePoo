class Estoque:
    def __init__(self, nome, capacidade_maxima):
        self.nome = nome
        self.espaco = capacidade_maxima
        self.produtos = {}
        self.endereco = ''
        
    def add_produto(self, id, nome, quantidade):
        if id in self.produtos:
            if self.produtos[id]['nome'] != nome:
                print(f'Erro: ID {id} já existe para o produto {self.produtos[id]["nome"]}.')
                return None
            self.produtos[id]['quantidade'] += quantidade
        else:
            self.produtos[id] = {'nome':nome, 'quantidade': quantidade}
        self.espaco -= quantidade
        
        print(f'A capcidade livre do estoque é de {self.espaco} itens atualmente.\n')
    
    def buscar_produto(self, id):
        if id in self.produtos:
            produto = self.produtos[id]
            print(f'Existem {produto["quantidade"]} unidades de {produto["nome"]} no estoque {self.nome}')

    def mostra_estoque(self):
        pass
    
e1 = Estoque('Amazon', 1000)
e2 = Estoque('Americanas', 800)

e1.add_produto('20', 'Caneta', 30)
e1.add_produto('30', 'Lapis', 30)
e1.buscar_produto('20')
