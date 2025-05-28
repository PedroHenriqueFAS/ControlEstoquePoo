class Estoque:
    def __init__(self, nome, capacidade_maxima):
        self.nome = nome
        self.espaco = capacidade_maxima
        self.produtos = {}
        self.produtos2 = {}
        self.endereco = ''
        
    def add_produto2(self, id, produto):
        if id in self.produtos2:
            self.produtos2[id] = produto
        
    def add_produto(self, id, nome, quantidade):
        if id in self.produtos:
            if self.produtos[id]['nome'] != nome:
                print(f'Erro: ID {id} já existe para o produto {self.produtos[id]["nome"]}.')
                return None
            if quantidade > self.espaco:
                print('O estoque não tem espaço suficiente para adicionar este produto.')
                return None #retorna nada se não houver espaço
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
        print(f'Estado do estoque atual {self.nome}: \n')
        for id, produto in self.produtos.items(): # iterando sobre os itens do dicionário
            print(f'ID: {id}, Nome: {produto["nome"]}, quantidade: {produto["quantidade"]} unidades')
            
class Produto:
    
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
    
e1 = Estoque('Amazon', 1000)
e2 = Estoque('Americanas', 800)

p1 = Produto('Borracha', 20)

e1.add_produto('20', 'Caneta', 30)
e1.add_produto('30', 'Lapis', 30)
e1.buscar_produto('20')
e1.mostra_estoque()
