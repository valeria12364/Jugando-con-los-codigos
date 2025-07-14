# Este programa solicita al usuario que ingrese dos números y luego calcula y muestra su suma.

try:
    # Solicitar al usuario el primer número
    # La función input() lee la entrada como una cadena, por lo que necesitamos convertirla a un tipo numérico.
    num1_str = input("Por favor, ingresa el primer número: ")
    num1 = float(num1_str) # Convertir la cadena a un número flotante para permitir decimales

    # Solicitar al usuario el segundo número
    num2_str = input("Por favor, ingresa el segundo número: ")
    num2 = float(num2_str) # Convertir la cadena a un número flotante

    # Calcular la suma de los dos números
    suma = num1 + num2

    # Imprimir el resultado de la suma
    # Usamos una f-string para formatear la salida de manera clara.
    print(f"La suma de {num1} y {num2} es: {suma}")

except ValueError:
    # Manejar el error si el usuario ingresa algo que no es un número
    print("Entrada inválida. Por favor, asegúrate de ingresar solo números.")
except Exception as e:
    # Manejar cualquier otro error inesperado
    print(f"Ocurrió un error inesperado: {e}")
