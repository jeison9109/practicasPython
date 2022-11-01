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

import json


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

    def convertirProductosADiccionario(self):
        diccProductos = {"productos": []}
        for producto in self.products:
            # diccProductos["productos"].append(
            #     {"nombre": producto.name, "precio": producto.price})
            diccProductos["productos"].append(producto.__dict__)
        with open('productosJSON.json', 'w') as jsonFile:
            json.dump(diccProductos, jsonFile)
            jsonFile.close()

    def convertirDiccionarioAProductos(self):
        with open('productosJSON.json') as jsonFile:
            diccionarioProductos = json.load(jsonFile)
            jsonFile.close()
        for producto in diccionarioProductos["productos"]:
            nuevoProducto = Product(producto["nombre"], producto["precio"])
            self.products.append(nuevoProducto)

    def convertirClientesADiccionario(self):
        diccClientes = {"clientes": []}
        for client in self.listClients:
            diccClientes["clientes"].append(
                {"nombre": client.name, "documento": client.document})
        with open('clients.json', 'w') as jsonFile:
            json.dump(diccClientes, jsonFile)
            jsonFile.close()

    def convertirDiccionarioAClientes(self):
        with open('clients.json') as jsonFile:
            diccionarioCliente = json.load(jsonFile)
            jsonFile.close()
        for client in diccionarioCliente["clientes"]:
            newClient = Client(client["nombre"], client["documento"])
            self.listClients.append(newClient)

    def agregarCliente(self, client):
        self.listClients.append(client)
        self.convertirClientesADiccionario()

    def imprimirClientes(self):
        for client in self.listClients:
            print(client)


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

    def __str__(self):
        return self.name + "-" + str(self.document)


class Sales:
    def __init__(self, date, client):
        self.date = date
        self.client = client
        self.products = []


# Crear la logica de la aplicacion
tienda = Tienda("PrevalentWare", "Calle 234#323-22", "321 242423")

try:
    # products = tienda.convertirDiccionarioAProductos()
    tienda.convertirDiccionarioAProductos()

except:
    print("No existe el archivo producto.Inicialize productos")

try:
    tienda.convertirDiccionarioAClientes()
except:
    print("No existe el archivo de cliente, inicializar clientes")


while True:
    instrucciones = """
        Ingrese P para agregar un producto a la tienda
        Ingrese IP para imprimir productos de la tienda
        Ingrese C para agregar un nuevo cliente
        Ingrese IC para imprimos los clientes d ela tienda
    """
    operacion = input(instrucciones)
    if operacion == "P":
        nombreProducto = input("Ingrese el nombre del producto")
        precioProducto = float(input("Ingrese el precio del producto"))
        nuevoProducto = Product(nombreProducto, precioProducto)
        tienda.agregarProducto(nuevoProducto)
    elif operacion == "IP":
        tienda.imprimirProductos()
        tienda.convertirProductosADiccionario()
    elif operacion == "C":
        nombreCliente = input("Ingrese el nombre del cliente: ")
        documentoCliente = input("Ingrese el documento del cliente: ")
        nuevoCliente = Client(nombreCliente, documentoCliente)
        tienda.agregarCliente(nuevoCliente)
    elif operacion == "IC":
        tienda.imprimirClientes()
