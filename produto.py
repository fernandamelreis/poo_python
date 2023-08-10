class Produto:
    def __init__(self, nome, desc, preco, tamanho):
        self.nome = nome
        self.desc = desc
        self.preco = preco
        self.tamanho = tamanho
        
    def Cadastrar_Produto(self):
        print("--- CADASTRANDO PRODUTO ---")
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
        print("--- VERIFICANDO PRODUTO ---")
        nome = input("Digite o nome do produto: ")
        desc = input("Digite a descrição do produto: ")
        preco = float(input("Digite o preço do produto: "))
        tamanho = input("Digite o tamanho do produto: ")
        
        if ((nome == self.nome) and (desc == self.desc) and (preco == self.preco) and (tamanho == self.tamanho)):
            print("Produto autenticado no sistema!")
        else:
            print("Produto não encontrado no estoque!")
        
    def Atualizar_Produto(self):
        print("Atualizando produto")
        
        print(self.nome)
        print(self.desc)
        print(self.preco)
        print(self.tamanho)
        
        resp = input("Deseja atualizar o produto: [y ou n]")
        
        if (resp == 'y'):
            
            print("[1] NOME PRODUTO")
            print("[2] DESCRIÇÃO PRODUTO")
            print("[3] PREÇO PRODUTO")
            print("[4] TAMANHO PRODUTO")
            
            opcao = int(input("Digite a opção que deseja alterar: "))
            
            if (opcao == 1):
                print("Atualizando nome do produto")
                self.nome = input("Digite o novo nome para o produto: ")
                print("Nome do produto atualizado!")
                print(self.nome)
            elif (opcao == 2):
                print("Atualizando descrição do produto")
                self.desc = input("Digite a nova descrição para o produto: ")
                print("Descrição do produto atualizada!")
                print(self.desc)
            elif (opcao == 3):
                print("Atualizando preço do produto")
                self.preco = float(input("Digite o novo preço para o produto: "))
                print("Preço do produto atualizada!")
                print(self.preco)
            elif (opcao == 4):
                print("Atualizando tamanho do produto")
                self.tamanho = input("Digite o novo tamanho para o produto: ")
                print("Tamanho do produto atualizada!")
                print(self.tamanho)
            else:
                print("Digite uma opção válida!")
        else:
            print("Encerrando operação...")
            
        print("----------------------------------")
        print("----- PRODUTO ATUALIZADO -----")
        print("CONFIRA TODAS AS INFORMAÇÕES DO PRODUTO:")
        print(self.nome)
        print(self.desc)
        print(self.preco)
        print(self.tamanho)
        
    def Deletar_Produto(self):
        print("--- DELETAR PRODUTO ---")
        print("INFORMAÇÕES DO PRODUTO:")
        
        print("Nome: {}".format(self.nome))
        print("Descrição: {}".format(self.desc))
        print("Preço: R$ {}".format(self.preco))
        print("Tamanho: {}".format(self.tamanho))
        
        
        resp = input("Deseja realmente excluir o produto no estoque: [sim] ou [não]")
        
        if (resp == 'sim'):
            self.nome = None
            self.desc = None
            self.preco = None
            self.tamanho = None
            print("Produto excluído do estoque!")
        else:
            print("Fim de operação... Produto não excluído!")
        
        print("----------------------------------")
        print("----- LISTAGEM DE PRODUTO -----")
        print("CONFIRA TODAS AS INFORMAÇÕES DO PRODUTO:")
        print(self.nome)
        print(self.desc)
        print(self.preco)
        print(self.tamanho)
        
p1 = Produto('Pincel', 'cor vermelho', 7.00, 'não especificado')
p1.Deletar_Produto()
