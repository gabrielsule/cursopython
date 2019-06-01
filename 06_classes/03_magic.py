class Rectangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"    

    def dibuar(self):
        print(f"base {self.x}, altura {self.y}")

rectangulo = Rectangulo(2, 3)
rectangulo.dibuar()
print(rectangulo)
