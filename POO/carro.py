class Carro: #definicação de  classe tem que ser maiúscula
    def __init__(self, modelo, cor, preco, fabricante): #construtor que define as características do objeto
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.fabricante = fabricante
    
    def Ligar(self): #definindo ação de ligar
        print("O carro está ligando...")

    def Acelerar(self): #definindo ação de acelerar
        print("Carro está acelerando...")

    def DesligarMotor(self): #definindo ação de desligar
        print("Desligando o motor do carro...")

    

c1 = Carro("CIVIC", "Prata", 244.900, "Honda") #objeto da classe Carro
c1.Ligar()  #chamando o comportamento / ação
c1.Acelerar()
c1.DesligarMotor()

print(c1.modelo) #chamando as informações
print(c1.cor)
print(c1.preco)
print(c1.fabricante)

c2 = Carro("RENEGATE", "Laranja", 134.190, "Jeep")

c2.Ligar()
c2.Acelerar()
c2.DesligarMotor()

print(c2.modelo)
print(c2.cor)
print(c2.preco)
print(c2.fabricante)

c3 = Carro("HILUX", "Vermelho", 273.090, "Toyota")
c3.Ligar()
c3.Acelerar()
c3.DesligarMotor()

print(c3.modelo)
print(c3.cor)
print(c3.preco)
print(c3.fabricante)

    
        