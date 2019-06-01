class Producto:
    def __init__(self, value):
        self.set_precio(value)

    def get_precio(self):
        return self.__precio

    def set_precio(self, value):
        if value < 0 :
            raise ValueError("no se aceptan numeros negativos")
        
        self.__precio = value 

    price = property(get_precio, set_precio)

producto = Producto(5)
print(producto.get_precio()) 