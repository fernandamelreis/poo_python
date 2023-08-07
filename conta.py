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
        print("Sacando dinheiro da conta bancária...")
        print("-------------")
    
    def Pix_Conta(self):
        print("---PIX---")
        print("Fazendo um pix...")
        print("-------------")
    
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
        
c1 = Conta('1', 'João', '111.111.111-11', 'joao@email.com', '******', '123-4', '56', 1000.0, 2000.0) #definindo objeto
c1.Saque_Conta()
c1.Pix_Conta()
c1.Extrato_Conta()
c1.Saldo_Conta()
c1.Pagamento_Conta()
c1.Emprestimo_Conta()
print("Id: " , c1.id_conta) 
print("Nome: " , c1.name_titular)
print("CPF: " , c1.cpf_titular)
print("E-mail: ", c1.email_titular)
print("Senha: " , c1.senha_titular)
print("Agência: ", c1.agencia)
print("Conta: ", c1.conta)





    