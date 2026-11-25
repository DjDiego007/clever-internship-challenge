"""
Ejercicio 1 - Suma de dígitos

Idea: sacar cada dígito del número usando matemáticas (sin convertirlo
a lista) y ir sumándolos.

    12345 % 10 = 5  -> último dígito
    12345 // 10 = 1234 -> el número sin el último dígito
"""


def digitsSum(inputInt):
    # Dejé el nombre igual al del enunciado (digitsSum) para que sea fácil de probar.

    # Los ejemplos del reto vienen como texto ("999"), así que lo convierto
    # a entero por si llega así. También uso abs() para que un número
    # negativo (-123) no se quede en un ciclo raro: sus dígitos son 1, 2 y 3.
    numero = abs(int(inputInt))

    suma = 0

    # Mientras queden dígitos por procesar...
    while numero > 0:
        ultimo_digito = numero % 10   # el residuo de dividir entre 10 es el último dígito
        suma += ultimo_digito         # lo acumulo
        numero //= 10                 # quito ese dígito del número

    # Si el número era 0, el ciclo no corre y la suma queda en 0 (correcto).
    return suma
