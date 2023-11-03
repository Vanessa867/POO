class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def Comer(self):
        print(f'O animal {self.nome}, de cor {self.cor}, está comendo.')

meu_animal = Animal("Leão", "amarelo")
meu_animal.Comer()
