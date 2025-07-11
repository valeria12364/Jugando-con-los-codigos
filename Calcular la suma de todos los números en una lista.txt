# Este programa demuestra cómo calcular la suma de todos los números en una lista.

def sumar_lista(numeros):
    """
    Calcula la suma de todos los números en una lista dada.

    Args:
        numeros (list): Una lista de números (enteros o flotantes).

    Returns:
        float/int: La suma total de los números en la lista.
    """
    # Opción 1: Usando un bucle (más explícito para entender la lógica)
    suma_total = 0
    for numero in numeros:
        suma_total += numero
    return suma_total

    # Opción 2: Usando la función sum() incorporada de Python (más concisa y eficiente)
    # return sum(numeros)

# Ejemplo de uso:
mi_lista_de_numeros = [10, 20, 30, 40, 50, 5.5, 12.3]

# Llamar a la función para sumar los números de la lista
resultado_suma = sumar_lista(mi_lista_de_numeros)

# Imprimir la lista y el resultado de la suma
print(f"La lista de números es: {mi_lista_de_numeros}")
print(f"La suma de todos los números en la lista es: {resultado_suma}")

# Otro ejemplo con una lista diferente
otra_lista = [-1, 0, 100, 25.7]
print(f"\nLa lista de números es: {otra_lista}")
print(f"La suma de todos los números en la lista es: {sumar_lista(otra_lista)}")
