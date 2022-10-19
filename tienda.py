# 1. Crear una clase Tienda que tenga los siguientes atributos:
# nombres
# direccion
# telefono
# lista de productos
# lista de clientes
# historico de vetnas

# 2. Crear una clase Productos que tenga los siguientes atributos:
# nombre
# precio

# 3. Crear una clase Cliente que tenga los siguientes atributos:
# nombre
# documento
# lista de compras

# 4. crear una clase venta que tenga los siguientes atributos:
# fecha
# lista de productos y cantidades
# cliente


from tkinter import N


class Tienda:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.hstSale = []
        self.products = []
        self.listClients = []
    # definir un metodo para agregar un nuevo producto

    def agregarProducto(self, product):
        self.products.append(product)

    def imprimirProductos(self):
        for product in self.products:
            print(product)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name + "-" + str(self.price)


class Client:
    def __init__(self, name, document):
        self.name = name
        self.document = document
        self.listBuys = []


class Sales:
    def __init__(self, date, client):
        self.date = date
        self.client = client
        self.products = []


# Crear la logica de la aplicacion
tienda = Tienda("PrevalentWare", "Calle 234#323-22", "321 242423")
while True:
    instrucciones = """
        Ingrese P para agregar un producto a la tienda
        Ingrese IP para imprimir productos de la tienda
    """
    operacion = input(instrucciones)
    if operacion == "P":
        nombreProducto = input("Ingrese el nombre del producto")
        precioProducto = float(input("Ingrese el precio del producto"))
        nuevoProducto = Product(nombreProducto, precioProducto)
        tienda.agregarProducto(nuevoProducto)
    elif operacion == "IP":
        tienda.imprimirProductos()
