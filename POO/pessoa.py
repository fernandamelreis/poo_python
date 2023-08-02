class Pessoa:
    def __init__(self, nome, idade, genero, nacionalidade, contato):
        self.nome = nome #instanciando na memória
        self.idade = idade
        self.genero = genero
        self.nacionalidade = nacionalidade
        self.contato = contato

    def Falar(self):
        print("Falando bla bla blá...")

    def Andar(self):
        print("Andando...")

    def Pular(self):
        print("Pulando...")

    def Comer(self):
        print("Comendo...")

