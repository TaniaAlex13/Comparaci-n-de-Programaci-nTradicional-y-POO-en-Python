# Clase Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

        def vender(self):
            if self.stock > 0:
                self.stock -= 1
                return True
            return False
# Clase Cliente
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

# Clase Tienda
class Tienda:
    def vender(self, cliente, producto):
        if producto.vender():
            print(cliente.nombre, "compró", producto.nombre)
        else:
            print("No hay stock disponible")