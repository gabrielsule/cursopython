class Animal:
    def __init__(self):
        self.edad = 3

    def come(self):
        print("come")

class Acuatico(Animal):
    def __init__(self):
        super().__init__()
        self.peso = 2

    def nada(self):
        print("nada")

pez = Acuatico()
pez.come()
pez.nada()
print(pez.edad)
print(pez.peso)