class Pessoa:
    def __init__(self, nome, email, senha, contato, endereco, cpf, genero):
        self.nome = nome 
        self.email = email
        self.senha = senha
        self.contato = contato
        self.endereco = endereco
        self.cpf = cpf
        self.genero = genero
        
    @property       #recuperação
    def nome(self): 
        return self._nome

    @nome.setter    #atualização
    def nome(self, nome):
        self._nome = nome
    
    @property         
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email
    
    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha):
        self._senha = senha
    
    @property    
    def contato(self):
        return self._contato
    
    @contato.setter
    def contato(self, contato):
        self._contato = contato
        
    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
    
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
    
    @property
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, genero):
        self._genero = genero
                
    def Falar(self):
        print("Bla bla bla...")
        
    def Ouvir(self):
        print("Ouvindo...")
    
    def Andar(self):
        print("Andando...")
        
    def Informacoes_pessoa(self):
        nome = 'Fernanda'
        email = 'fernanda.melo@email.com'
        senha = '123456'
        contato = '(87)98826-4408'
        endereco = 'Rua X no. 18'
        cpf = '111.111.111-11'
        genero = 'feminino'
        
        
        print("--- INFORMAÇÕES PESSOA ---")
        print("Nome: ", nome)
        print("Email: ", email)
        print("Senha: ******")
        print("Contato: ", contato)
        print("Endereço: ", endereco)
        print("CPF: ", cpf)
        print("Gênero: ", genero)
        print("--------------------------")
        
    def Registrar_pessoa(self):
        
        print("--- REGISTRO PESSOA ---")
        nome = input("Digite o nome: ")
        email = input("Digite o e-mail: ")
        senha = input("Digite a senha: ")
        contato = input("Digite o contato: ")
        endereco = input("Digite o endereço: ")
        cpf = input("Digite o cpf: ")
        genero = input("Digite o gênero: ")
        print("------------------------")
        
        print("Nome: ", nome)
        print("Email: ", email)
        print("Senha: ******")
        print("Contato: ", contato)
        print("Endereço: ", endereco)
        print("CPF: ", cpf)
        print("Gênero: ", genero)
        
p1 = Pessoa('', '', '', '', '', '', '')
p1.Informacoes_pessoa()
