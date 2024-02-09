from queue import Queue

class Producto:

    #Clase que representa un producto en el inventario.

    #Atributos:
        #- nombre (str): Nombre del producto.
        #- precio (float): Precio del producto.
        #- cantidad (int): Cantidad de unidades disponibles en el inventario.

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Inventario:

    #Clase que gestiona el inventario de productos y registra transacciones.

    #Atributos:
        #- productos (dict): Diccionario que almacena los productos en el inventario.
        #- transacciones (Queue): Cola que registra las transacciones de reposición y venta.

    def __init__(self):
        self.productos = {}
        self.transacciones = Queue()

    def agregar_producto(self, producto, cantidad):

        #Agrega un producto al inventario y registra la transacción de reposición.

        #Parámetros:
            #- producto (Producto): Instancia de la clase Producto a agregar.
            #- cantidad (int): Cantidad de unidades para reposición.

        if producto.nombre in self.productos:
            self.productos[producto.nombre].cantidad += cantidad
        else:
            self.productos[producto.nombre] = producto
            self.productos[producto.nombre].cantidad = cantidad

        # Registrar transacción de reposición en la cola

        self.transacciones.put(f"Reposición: {cantidad} unidades de {producto.nombre}")

    def vender_producto(self, nombre_producto, cantidad):

        #Vende un producto del inventario y registra la transacción de venta.

        #Parámetros:
            #- nombre_producto (str): Nombre del producto a vender.
            #- cantidad (int): Cantidad de unidades a vender.

        if nombre_producto in self.productos:
            if self.productos[nombre_producto].cantidad >= cantidad:
                self.productos[nombre_producto].cantidad -= cantidad

                # Registrar transacción de venta en la cola

                self.transacciones.put(f"Venta: {cantidad} unidades de {nombre_producto}")
            else:
                print(f"No hay suficiente stock de {nombre_producto}")
        else:
            print(f"{nombre_producto} no encontrado en el inventario")

    def mostrar_inventario(self):

        #Muestra el inventario actual con detalles de cada producto.

        print("Inventario:")
        for producto in self.productos.values():
            print(f"{producto.nombre}: {producto.cantidad} unidades - Precio: ${producto.precio:.2f}")

    def mostrar_transacciones(self):

        #Muestra el registro de transacciones almacenado en la cola.

        print("Registro de Transacciones:")
        while not self.transacciones.empty():
            print(self.transacciones.get())

# Función para crear un producto con input del usuario

def crear_producto_desde_input():

    #Crea un nuevo producto solicitando información al usuario.

    #Retorna:
        #- Producto: Instancia de la clase Producto creada con la información proporcionada por el usuario.

    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad inicial del producto: "))
    return Producto(nombre, precio, cantidad)

# Ejemplo de uso

if __name__ == "__main__":
    inventario_almacen = Inventario()

    while True:
        print("\n--- Prendas ---")
        print("1. Agregar Producto")
        print("2. Vender Producto")
        print("3. Mostrar Inventario")
        print("4. Mostrar Transacciones")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto_nuevo = crear_producto_desde_input()
            cantidad_reposicion = int(input("Cantidad para reposición: "))
            inventario_almacen.agregar_producto(producto_nuevo, cantidad_reposicion)

        elif opcion == "2":
            nombre_producto = input("Nombre del producto a vender: ")
            cantidad_venta = int(input("Cantidad a vender: "))
            inventario_almacen.vender_producto(nombre_producto, cantidad_venta)

        elif opcion == "3":
            inventario_almacen.mostrar_inventario()

        elif opcion == "4":
            inventario_almacen.mostrar_transacciones()

        elif opcion == "5":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
