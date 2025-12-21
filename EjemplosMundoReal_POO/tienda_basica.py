# Clase Producto
# Representa un producto de la tienda
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
# Clase Cliente
# Representa al cliente de la tienda
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def comprar(self, producto):
        print(self.nombre, "compró", producto.nombre, "por $", producto.precio)
# Clase Tienda
# Representa la tienda
class Tienda:
    def vender(self, cliente, producto):
        cliente.comprar(producto)

# Programa tienda basica
tienda = Tienda()
producto = Producto("Pan", 0.15)
cliente = Cliente("Tania")

tienda.vender(cliente, producto)