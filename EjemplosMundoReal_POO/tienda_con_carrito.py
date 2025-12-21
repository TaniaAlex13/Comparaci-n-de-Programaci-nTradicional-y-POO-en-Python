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

# Clase Tienda
class Tienda:
    def vender(self, cliente, producto):
        cliente.agregar_al_carrito(producto)


# Programa tienda con carrito
producto1 = Producto("Fideos", 2)
producto2 = Producto("Azúcar", 1.5)
producto3 = Producto("Café", 4.20)

cliente = Cliente("Tania")
tienda = Tienda()

tienda.vender(cliente, producto1)
tienda.vender(cliente, producto2)
tienda.vender(cliente, producto3)

cliente.mostrar_carrito()