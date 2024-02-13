# Importa los módulos necesarios.
from queue import Queue #Se utiliza para gestionar una cola de transacciones.
#La clase Queue proporciona una estructura de datos de cola en Python.
import os # Proporciona una interfaz para interactuar con el sistema operativo.

# Limpiar la pantalla de la consola según el sistema operativo.
os.system("cls" if os.name == "nt" else "clear")

# Definir una clase para representar un producto.
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

# Definir una clase para gestionar el inventario.
class Inventario:
    def __init__(self):
        # Inicializar un diccionario para almacenar productos y una cola para transacciones.
        self.productos = {}
        self.movimientos = Queue()

    def agregar_producto(self, producto, cantidad_reposicion):
        # Agregar o actualizar la cantidad de un producto en el inventario.
        if producto.nombre in self.productos:
            self.productos[producto.nombre].cantidad += cantidad_reposicion
        else:
            self.productos[producto.nombre] = producto
            self.productos[producto.nombre].cantidad = cantidad_reposicion

        # Registrar la transacción de reposición en la cola de transacciones.
        self.movimientos.put(f"Se ingresaron: {cantidad_reposicion} unidades de {producto.nombre}")

    def vender_producto(self, nombre_producto, cantidad_venta):
        # Vender una cantidad especificada de un producto si hay suficiente stock.
        if nombre_producto in self.productos:
            if self.productos[nombre_producto].cantidad >= cantidad_venta:
                self.productos[nombre_producto].cantidad -= cantidad_venta
                # Registrar la transacción de venta en la cola de transacciones.
                self.movimientos.put(f"Venta: {cantidad_venta} unidades de {nombre_producto}")
            else:
                print(f"No hay suficiente stock de {nombre_producto}")
        else:
            print(f"{nombre_producto} no encontrado en el inventario")

    def mostrar_inventario(self):
        # Mostrar el inventario actual con nombres de productos, cantidades y precios.
        print("Inventario:")
        for producto in self.productos.values():
            print(f"{producto.nombre}: {producto.cantidad} unidades - Precio: ${producto.precio:.2f}")

    def mostrar_movimientos(self):
        # Mostrar el historial de transacciones desde la cola de transacciones.
        print("Registro de Movimientos:")
        #while not self.movimientos.empty():
            #print(self.movimientos.get())
        # Crear una lista temporal para almacenar los movimientos
        movimientos_temporales = []

        # Obtener y mostrar los movimientos, pero no eliminarlos de la cola.
        while not self.movimientos.empty():
            movimiento = self.movimientos.get()
            print(movimiento)
            movimientos_temporales.append(movimiento)

        # Volver a poner los movimientos en la cola
        for movimiento in movimientos_temporales:
            self.movimientos.put(movimiento)

# Función para crear una instancia de producto a partir de la entrada del usuario.
def crear_producto_desde_input():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    return Producto(nombre, precio, 0)  # La cantidad inicial se establece en 0.

# El programa principal comienza aquí.
if __name__ == "__main__":
    # Crear una instancia de la clase Inventario.
    inventario_almacen = Inventario()

    # Bucle principal del programa.
    while True:
        # Mostrar opciones de menú al usuario.
        print("\n--- Prendas ---\n")
        print("1. Agregar Producto")
        print("2. Vender Producto")
        print("3. Mostrar Inventario")
        print("4. Mostrar Movimientos")
        print("5. Salir")

        # Solicitar entrada al usuario.
        opcion = input("\nSeleccione una opción: ")

        # Realizar acciones según la entrada del usuario.
        # código a ejecutar si la condición_1 es verdadera.
        if opcion == "1":
            print("\n--- Agregar ---\n")
            producto_nuevo = crear_producto_desde_input()
            cantidad_reposicion = int(input("Cantidad: "))
            inventario_almacen.agregar_producto(producto_nuevo, cantidad_reposicion)

        # código a ejecutar si la condición1 es falsa y la condición2 es verdadera.
        elif opcion == "2":
            print("\n--- Vender ---\n")
            nombre_producto = input("Nombre del producto a vender: ")
            cantidad_venta = int(input("Cantidad a vender: "))
            inventario_almacen.vender_producto(nombre_producto, cantidad_venta)

        # código a ejecutar si la condición1 y la condición2 son falsas y la condición3 es verdadera.
        elif opcion == "3":
            print("\n--- Inventario ---\n")
            inventario_almacen.mostrar_inventario()

        # código a ejecutar si la condición1, la condición2, la condición3 son falsas y la condición4 es verdadera.
        elif opcion == "4":
            print("\n--- Movimientos ---\n")
            inventario_almacen.mostrar_movimientos()

        # código a ejecutar si la condición1, la condición2, la condición3, la condición4 son falsas y la condición5 es verdadera.
        elif opcion == "5":
            print("Saliendo del programa.")
            break

        # código a ejecutar si todas las condiciones anteriores son falsas
        else:
            print("Opción no válida. Intente de nuevo.")
