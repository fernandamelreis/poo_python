class Produto:
    def __init__(self, nome, desc, preco, tamanho):
        self.nome = nome
        self.desc = desc
        self.preco = preco
        self.tamanho = tamanho
        
    def Cadastrar_Produto(self):
        print("--- CADASTRANDO PRODUTO ---- ")
        nome = input("Digite o nome do produto: ")
        desc = input("Digite a descrição do produto: ")
        preco = float(input("Digite o preço do produto: "))
        tamanho = input("Digite o tamanho do produto: ")
        
        print("Nome: {}".format(nome))
        print("Descrição: {}".format(desc))
        print("Preço: R$ {}".format(preco))
        print("Tamanho: {}".format(tamanho))
        
        resp = input("deseja inserir o produto no estoque: [sim] ou [não]")
        
        if (resp == 'sim'):
            print("Produto inserido no estoque!")
            print("Produto cadastrado sucesso!")
        else:
            print("Fim de operação!")
    
    def Autenticar_Produto(self):
        nome = input("Digite o nome do produto: ")
        desc = input("Digite a descrição do produto: ")
        preco = float(input("Digite o preço do produto: "))
        tamanho = input("Digite o tamanho do produto: ")
        
        if ((nome == self.nome) and (desc == self.desc) and (preco == self.preco) and (tamanho == self.tamanho)):
            print("Produto autenticado no sistema!")
        else:
            print("Produto não encontrado no estoque!")
        
    def Atualizar_Produto(self):
        print("Produto atualizado!")
        
    def Deletar_Produto(self):
        print("Produto deletado!")
        
p1 = Produto('Pincel', 'cor vermelho', 7.00, 'não especificado')
p1.Autenticar_Produto()
