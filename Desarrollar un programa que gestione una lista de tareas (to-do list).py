# Este programa gestiona una lista de tareas (to-do list) en memoria.
# Las tareas se almacenan en una lista de diccionarios.

# Lista global para almacenar las tareas. Cada tarea es un diccionario.
# Ejemplo: {"descripcion": "Comprar leche", "completada": False}
lista_de_tareas = []

def mostrar_menu():
    """Muestra las opciones del menú principal al usuario."""
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Añadir tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("------------------------")

def añadir_tarea():
    """Solicita al usuario una descripción y añade una nueva tarea a la lista."""
    descripcion = input("Introduce la descripción de la nueva tarea: ").strip()
    if descripcion:
        tarea = {"descripcion": descripcion, "completada": False}
        lista_de_tareas.append(tarea)
        print(f"Tarea '{descripcion}' añadida.")
    else:
        print("La descripción de la tarea no puede estar vacía.")

def ver_tareas():
    """Muestra todas las tareas en la lista con su estado (completada/pendiente)."""
    if not lista_de_tareas:
        print("No hay tareas en la lista.")
        return

    print("\n--- TUS TAREAS ---")
    for i, tarea in enumerate(lista_de_tareas):
        estado = "✓" if tarea["completada"] else " "
        print(f"{i + 1}. [{estado}] {tarea['descripcion']}")
    print("------------------")

def marcar_tarea_completada():
    """
    Permite al usuario marcar una tarea existente como completada.
    Solicita el número de la tarea de la lista.
    """
    ver_tareas() # Muestra las tareas para que el usuario pueda elegir.
    if not lista_de_tareas:
        return # No hay tareas para marcar.

    try:
        num_tarea_str = input("Introduce el número de la tarea a marcar como completada: ")
        num_tarea = int(num_tarea_str)
        # Ajustar el índice para que coincida con la lista (base 0)
        indice_tarea = num_tarea - 1

        if 0 <= indice_tarea < len(lista_de_tareas):
            if not lista_de_tareas[indice_tarea]["completada"]:
                lista_de_tareas[indice_tarea]["completada"] = True
                print(f"Tarea '{lista_de_tareas[indice_tarea]['descripcion']}' marcada como completada.")
            else:
                print("Esta tarea ya estaba marcada como completada.")
        else:
            print("Número de tarea inválido. Por favor, introduce un número de la lista.")
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número entero.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def eliminar_tarea():
    """
    Permite al usuario eliminar una tarea de la lista.
    Solicita el número de la tarea a eliminar.
    """
    ver_tareas() # Muestra las tareas para que el usuario pueda elegir.
    if not lista_de_tareas:
        return # No hay tareas para eliminar.

    try:
        num_tarea_str = input("Introduce el número de la tarea a eliminar: ")
        num_tarea = int(num_tarea_str)
        # Ajustar el índice para que coincida con la lista (base 0)
        indice_tarea = num_tarea - 1

        if 0 <= indice_tarea < len(lista_de_tareas):
            tarea_eliminada = lista_de_tareas.pop(indice_tarea)
            print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada.")
        else:
            print("Número de tarea inválido. Por favor, introduce un número de la lista.")
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número entero.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def main():
    """Función principal que ejecuta el bucle del programa."""
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == '1':
            añadir_tarea()
        elif opcion == '2':
            ver_tareas()
        elif opcion == '3':
            marcar_tarea_completada()
        elif opcion == '4':
            eliminar_tarea()
        elif opcion == '5':
            print("¡Hasta luego! Saliendo del gestor de tareas.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
