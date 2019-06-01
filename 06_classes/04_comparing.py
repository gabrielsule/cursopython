class Rectangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, otro_obj):
        return self.x == otro_obj.x and self.y == otro_obj.y

    def dibuar(self):
        print(f"base {self.x}, altura {self.y}")

rectangulo = Rectangulo(2, 3)
otro_rect = Rectangulo(2, 3)
print(rectangulo == otro_rect)
