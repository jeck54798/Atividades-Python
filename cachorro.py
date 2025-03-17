class Cachorro:

    def __init__(self, nome, raca, comida):
        self.nome = nome
        self.raca = raca
        self.comida = comida
        self.acordado = True
        self.satisfeito = False
        self.feliz = True
    
    def comer(self):
        if self.comida > 0:
            self.comida -= 1
            self.satisfeito = True
            print(f"{self.nome} comeu um lanche bastante satisfatório")
        else:
            print(f"{self.nome} está com fome")

    def dormir (self):
        self.acordado = False
        print(f"{self.nome} foi dormir")

    def acordar (self):
        self.acordado = True
        print(f"{self.nome} acordou")

    def ignorar (self):
        self.feliz = False
        print(f"{self.nome} está triste, porque está sendo ignorado")

    def brincar (self):
        self.feliz = True
        print(f"{self.nome} está feliz porque você brincou com ele")

    def latir (self):
        if self.acordado == True:
            print(f"{self.nome} está latindo! 'AU AU'")
        else: print(f"{self.nome} está sosegado")

