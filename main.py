class Predio: 
    
    def __init__(self, nome, endereco, espacos_vazios):
        self.nome = nome
        self.endereco = endereco
        self.espacos_vazios = espacos_vazios
        self.estoques = {}
        
    def cria_estoque(self, id, nome, capacidade_maxima):
        if not id in self.estoques:
            self.estoques[id] = Estoque(nome, capacidade_maxima)

class Estoque:
    def __init__(self, nome, capacidade_maxima):
        self.nome = nome
        self.espaco = capacidade_maxima
        self.produtos = {}
        self.produtos2 = {}
        self.endereco = ''
        
    def add_produto2(self, id, produto):
        if not id in self.produtos2:
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
            
class Descricao:
    def __init__(self, peso, tamanho, detalhes):
        self.peso = peso
        self.tamanho = tamanho
        self.detalhes = detalhes
        
    def exibe_detalhes(self):
        print(self.detalhes)
        
class Produto(Descricao):
    
    def __init__(self, nome, quantidade, peso, tamanho, detalhes):
        super().__init__(peso, tamanho, detalhes)
        self.nome = nome
        self.quantidade = quantidade
        self.descricao = 'VAZIO POR PADRAO'
  
e1 = Estoque('Amazon', 1000)
e2 = Estoque('Americanas', 800)

p1 = Produto('Borracha', 20, 30, 100, 'VAZIO')

p1.exibe_detalhes()

ed = Predio('Amorim', 'Educacao', 20)

ed.cria_estoque('30', 'Reciclagem', 1000)

ed.estoques['30'].add_produto2('10', p1)

print(ed.estoques['30'].produtos2['10'].nome)

e1.add_produto2('20', p1)
print(e1.produtos2['20'].descricao)

e1.add_produto('20', 'Caneta', 30)
e1.add_produto('30', 'Lapis', 30)
e1.buscar_produto('20')
e1.mostra_estoque()
