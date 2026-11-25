"""
Ejercicio 2 - Palíndromos

Idea: usar dos "dedos" (índices), uno al inicio y otro al final del texto,
y compararlos. Si todas las parejas son iguales, es palíndromo.

    s a l a s
    ^       ^    's' == 's' -> seguimos
      ^   ^      'a' == 'a' -> seguimos
        ^        se juntaron -> es palíndromo
"""


def isPalindrome(inputStr):
    # Paso todo a minúsculas y quito espacios para que frases como
    # "Anita lava la tina" también funcionen. No era obligatorio,
    # pero me pareció un detalle útil.
    texto = inputStr.lower().replace(" ", "")

    izquierda = 0                # empieza en la primera letra
    derecha = len(texto) - 1     # empieza en la última letra

    # Me detengo cuando los dos índices se cruzan: ya revisé todo.
    while izquierda < derecha:
        if texto[izquierda] != texto[derecha]:
            return False         # encontré una pareja distinta, no es palíndromo
        izquierda += 1           # avanzo desde el inicio
        derecha -= 1             # retrocedo desde el final

    # Si nunca encontré diferencias, es palíndromo.
    # (Un texto vacío o de una letra también cuenta como palíndromo.)
    return True
