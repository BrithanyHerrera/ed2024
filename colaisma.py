import os
import queue

class Tarea:
    def __init__(self, descripcion, prioridad):
        self.descripcion = descripcion
        self.prioridad = prioridad

# Diccionario para mapear números de prioridad a descripciones
prioridades_descripciones = {1: "Alta", 2: "Media", 3: "Baja"}

# Crear una cola de prioridad utilizando el módulo queue
cola_prioridad = queue.PriorityQueue()

# Función para mostrar las tareas en la cola de prioridad
def mostrar_tareas():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Tareas actuales en la cola de prioridad:\n")
    # Ordenar la cola de prioridad por el valor de prioridad (de menor a mayor)
    for tarea in sorted(list(cola_prioridad.queue), key=lambda x: x[0]):
        descripcion_prioridad = prioridades_descripciones.get(tarea[0], "Desconocida")
        print(f"Prioridad {descripcion_prioridad}: {tarea[1].descripcion}")
    input("\nPresiona Enter para volver al menú...")

# Función para agregar una nueva tarea a la cola de prioridad
def agregar_tarea():
    os.system('cls' if os.name == 'nt' else 'clear')
    descripcion = input("Ingrese la descripción de la tarea:\n")
    prioridad = int(input("Ingrese la prioridad de la tarea (1: Alta, 2: Media, 3: Baja):\n"))

    # Validar la prioridad y establecerla como Baja por defecto si no es válida
    if prioridad not in prioridades_descripciones:
        print("Prioridad no válida. Se establecerá como Baja.")
        prioridad = 3

    # Crear una instancia de la clase Tarea y agregarla a la cola de prioridad
    tarea = Tarea(descripcion, prioridad)
    cola_prioridad.put((prioridad, tarea))
    print(f"Tarea '{descripcion}' agregada con prioridad {prioridades_descripciones[prioridad]}.")
    input("\nPresiona Enter para volver al menú...")

# Menú interactivo
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Menú:")
    print("1. Mostrar tareas")
    print("2. Agregar tarea")
    print("3. Salir")

    # Solicitar al usuario que seleccione una opción del menú
    opcion = input("Seleccione una opción:\n")

    if opcion == "1":
        mostrar_tareas()
    elif opcion == "2":
        agregar_tarea()
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
