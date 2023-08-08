class Conta: #definição de entidade
    def __init__(self, id_conta, name_titular, cpf_titular, email_titular, senha_titular, agencia, conta, dinheiro, valor): #construtor que vai apontar os atributos da classe
        self.id_conta = id_conta
        self.name_titular = name_titular
        self.cpf_titular = cpf_titular
        self.email_titular = email_titular
        self.senha_titular = senha_titular
        self.agencia = agencia #atributo da classe
        self.conta = conta
        self.dinheiro = dinheiro
        self.valor = valor #instanciando atributos de futuros objetos na memória
        
    def Extrato_Conta(self):
        print("---EXTRATO---")
        print("Imprimindo dados da sua conta bancária...")
        print("Conta: {} Agência: {}".format(self.conta, self.agencia))
        print("-------------")
        
    def Saque_Conta(self):
        print("---SAQUE---")
        print("[1]. R$20.00")
        print("[2]. R$50.00")
        print("[3]. R$100.00")
        print("[4]. R$200.00")
        print("[5]. Outro valor")
        
        opcao = int(input("Digite uma opção: "))
        
        if (opcao == 1):
            senha = input("Digite a sua senha para confirmar o saque:")
            if (senha == self.senha_titular):
                print("Saque realizado com sucesso!")
                print("Quantia de R$ 20.00")
            else:
                print("Erro na operação...Senha incorreta...Finalizando...")
        elif(opcao == 2):
            senha = input("Digite a sua senha para confirmar o saque:")
            if (senha == self.senha_titular):
                print("Saque realizado com sucesso!")
                print("Quantia de R$ 50.00")
            else:
                print("Erro na operação...Senha incorreta...Finalizando...")
        elif(opcao == 3):
            senha = input("Digite a sua senha para confirmar o saque:")
            if (senha == self.senha_titular):
                print("Saque realizado com sucesso!")
                print("Quantia de R$ 100.00")
            else:
                print("Erro na operação...Senha incorreta...Finalizando...")
        elif(opcao == 4):
            senha = input("Digite a sua senha para confirmar o saque:")
            if (senha == self.senha_titular):
                print("Saque realizado com sucesso!")
                print("Quantia de R$ 200.00")
            else:
                print("Erro na operação...Senha incorreta...Finalizando...")
        elif(opcao == 5):
            valor_saque = float(input("Digite um valor para saque: "))
        
            senha = input("Digite a sua senha para confirmar o saque:")
            
            if (senha == self.senha_titular):
                print("Saque realizado com sucesso!")
                print("Quantia de R$ {}".format(valor_saque))
            else:
                print("Erro na operação...Senha incorreta...Finalizando...")
        else:
            print("Digite uma opção válida!")
    
    def Pix_Conta(self):
        print("---PIX---")
        
        chave_pessoa = input("Insira a chave PIX: ")
        print("A chave é {} ".format(chave_pessoa))
        print("----------------------------------")
        
        valor_pix = float(input("Insira o valor do PIX: "))
        print("Confirme o valor do PIX é {}".format(valor_pix))
        
        resp = input("Confirme a transação:_ y ou n ")
        
        if(resp == 'y'):
            print("Você fez um PIX de {} para {}".format(valor_pix, chave_pessoa))
        else:
            print("Encerrando a transação...")
    
    def Saldo_Conta(self):
        print("---SALDO---")
        print("O saldo da sua conta é: {}".format(self.dinheiro))
        print("-------------")
        
    def Pagamento_Conta(self):
        print("---PAGAMENTO---")
        print("{} , você deseja realizar o pagamento do boleto? ".format(self.name_titular)) 
        print("Seu saldo é {}".format(self.dinheiro))
        print("-------------")
    
    def Emprestimo_Conta(self):
        print("---EMPRÉSTIMO---")
        print("{}, você deseja realizar um empréstimo?".format(self.name_titular))
        print("Você tem um valor de R$ {} na sua conta disponível ".format(self.valor))
        print("-------------")
        
    def Depositar_Conta(self):
        print("{}, você deseja realizar o depósito de quanto?".format(self.name_titular))
        print("1. [ 50.00 ]")
        print("2. [ 100.00 ]")
        print("3. [ 200.00 ]")
        print("4. [ 500.00 ]")
        print("5. [ acima de 1000.00 ]")
        
        
        opcao = int(input("Digite a opção que você deseja realizar o depósito: "))
        resp = input("Confirme a transação:_ y ou n ")
        
        while (resp != 'n'):
            if (opcao == 1):
                print("{}, você realizou um depósito de 50.00! ".format(self.name_titular))
                return 0
            elif(opcao == 2):
                print("{}, você realizou um depósito de 100.00! ".format(self.name_titular))
                return 0
            elif( opcao == 3):
                print("{}, você realizou um depósito de 200.00! ".format(self.name_titular))
                return 0
            elif(opcao == 4):
                print("{}, você realizou um depósito de 500.00! ".format(self.name_titular))
                return 0
            elif(opcao == 5):
                print("{}, você realizou um depósito acima de 1000.00! ".format(self.name_titular))
                return 0
            else:
                print("Opção inválida!!!")
                       
c1 = Conta('1', 'João', '111.111.111-11', 'joao@email.com', '123456', '123-4', '56', 1000.0, 2000.0) #definindo objeto
c1.Saque_Conta()






    