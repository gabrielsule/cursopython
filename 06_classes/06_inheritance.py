class Animal:
    def __init__(self):
        self.edad = 3

    def come(self):
        print("come")

class Terrestre(Animal):
    def camina(self):
        print("camina")

class Acuatico(Animal):
    def nada(self):
        print("nada")

pez = Acuatico()
pez.come()
pez.nada()
print(pez.edad)