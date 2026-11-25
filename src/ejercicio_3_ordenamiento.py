"""
Ejercicio 3 - Ordenamiento (sin sort(), sorted() ni similares)

Elegí Merge Sort porque es eficiente (O(n log n)) y se explica fácil:
    1. Divido la lista a la mitad hasta que cada pedazo tenga 1 elemento
       (una lista de 1 elemento ya está ordenada).
    2. Mezclo los pedazos de dos en dos, siempre tomando el menor.

    [5, -2, 10, 0]
     /          \\
  [5, -2]     [10, 0]        <- divido
   /   \\       /    \\
 [5]  [-2]   [10]   [0]
   \\   /       \\    /
  [-2, 5]     [0, 10]        <- mezclo ordenando
     \\          /
  [-2, 0, 5, 10]             <- resultado final
"""


def integerSort(inputArray):
    # Caso base: con 0 o 1 elementos ya está ordenada.
    # Regreso una COPIA (list(...)) para nunca devolver la lista original.
    if len(inputArray) <= 1:
        return list(inputArray)

    # Divido en dos mitades. Los cortes con [:] crean listas nuevas,
    # por eso la lista original nunca se modifica.
    medio = len(inputArray) // 2
    izquierda = integerSort(inputArray[:medio])
    derecha = integerSort(inputArray[medio:])

    # Mezclo las dos mitades ya ordenadas.
    return _mezclar(izquierda, derecha)


def _mezclar(izquierda, derecha):
    """Une dos listas ya ordenadas en una sola lista ordenada."""
    resultado = []
    i = 0  # posición actual en 'izquierda'
    j = 0  # posición actual en 'derecha'

    # Comparo los elementos al frente de cada lista y paso el menor.
    # Uso <= para que, si hay repetidos, se respete su orden original.
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Cuando una lista se acaba, lo que sobra de la otra ya está ordenado
    # y es mayor o igual a todo lo anterior, así que lo agrego tal cual.
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado
