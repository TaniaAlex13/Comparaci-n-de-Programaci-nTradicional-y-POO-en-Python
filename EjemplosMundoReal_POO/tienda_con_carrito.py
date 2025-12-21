#El cliente agrega productos a un carrito de compras
# Clase Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Clase Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


# Clase Cliente
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []

    def agregar_al_carrito(self, producto):
        self.carrito.append(producto)

    def mostrar_carrito(self):
        print("Carrito de", self.nombre)
        for p in self.carrito:
            print("-", p.nombre, "$", p.precio)