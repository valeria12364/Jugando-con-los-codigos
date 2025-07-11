# Este programa define una función para determinar si un número dado es primo.

def es_primo(numero):
    """
    Determina si un número entero es primo.

    Un número primo es un número natural mayor que 1 que no tiene divisores positivos
    más que 1 y él mismo.

    Args:
        numero (int): El número entero a verificar.

    Returns:
        bool: True si el número es primo, False en caso contrario.
    """
    # Los números menores o iguales a 1 no son primos.
    if numero <= 1:
        return False
    # El 2 es el único número primo par.
    if numero == 2:
        return True
    # Si el número es par y mayor que 2, no es primo.
    if numero % 2 == 0:
        return False

    # Verificar divisores impares desde 3 hasta la raíz cuadrada del número.
    # No necesitamos verificar más allá de la raíz cuadrada porque si un número 'n'
    # tiene un divisor 'd' mayor que su raíz cuadrada, entonces también debe tener
    # un divisor 'n/d' que es menor que su raíz cuadrada.
    i = 3
    while i * i <= numero:
        if numero % i == 0:
            return False
        i += 2  # Solo necesitamos verificar divisores impares

    # Si no se encontraron divisores, el número es primo.
    return True

# Ejemplos de uso:
print(f"¿Es 7 primo? {es_primo(7)}")         # Debería ser True
print(f"¿Es 10 primo? {es_primo(10)}")       # Debería ser False
print(f"¿Es 2 primo? {es_primo(2)}")         # Debería ser True
print(f"¿Es 1 primo? {es_primo(1)}")         # Debería ser False
print(f"¿Es 0 primo? {es_primo(0)}")         # Debería ser False
print(f"¿Es 29 primo? {es_primo(29)}")       # Debería ser True
print(f"¿Es 97 primo? {es_primo(97)}")       # Debería ser True
print(f"¿Es 99 primo? {es_primo(99)}")       # Debería ser False
