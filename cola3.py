import os
os.system("cls" if os.name == "nt" else "clear")

class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, item):
        self.elementos.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            raise IndexError("Desencolar de una cola vacía")

    def esta_vacia(self):
        return len(self.elementos) == 0

class InventarioRopa(Cola):
    def __init__(self):
        super().__init__()
        self.inventario = {}

    def agregar_articulo(self, articulo, cantidad=1):
        if articulo in self.inventario:
            self.inventario[articulo] += cantidad
        else:
            self.inventario[articulo] = cantidad
        self.encolar(articulo)
        self.movimientos.append(f"Entrada: {cantidad} {articulo}")

    def eliminar_articulo(self, articulo, cantidad=1):
        try:
            if self.inventario[articulo] >= cantidad:
                self.inventario[articulo] -= cantidad
                self.movimientos.append(f"Salida: {cantidad} {articulo}")
            else:
                print("No hay suficiente cantidad de este artículo en el inventario.")
        except KeyError:
            print("El artículo no está en el inventario.")

    def mostrar_inventario(self):
        print("Inventario de ropa:")
        if not self.esta_vacia():
            for articulo, cantidad in self.inventario.items():
                print("-", articulo, f"({cantidad})")
        else:
            print("El inventario está vacío.")

    def mostrar_movimientos(self):
        print("Movimientos:")
        if self.movimientos:
            for movimiento in self.movimientos:
                print("-", movimiento)
        else:
            print("No hay movimientos registrados.")

# Función para mostrar el menú
def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar producto")
    print("2. Vender producto")
    print("3. Ver inventario")
    print("4. Ver movimientos")
    print("5. Salir")

# Uso del inventario de ropa
inventario = InventarioRopa()

# Bucle para mostrar el menú continuamente
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto a agregar: ")
        cantidad = int(input("Ingrese la cantidad de producto a agregar: "))
        inventario.agregar_articulo(producto, cantidad)
        print(f"{cantidad} producto(s) '{producto}' agregado(s) al inventario.")

    elif opcion == "2":
        producto = input("Ingrese el nombre del producto a vender: ")
        cantidad = int(input("Ingrese la cantidad de producto a vender: "))
        inventario.eliminar_articulo(producto, cantidad)
        print(f"{cantidad} producto(s) '{producto}' vendido(s).")

    elif opcion == "3":
        inventario.mostrar_inventario()

    elif opcion == "4":
        inventario.mostrar_movimientos()

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")
