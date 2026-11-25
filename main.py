"""
Corre los casos de ejemplo del desafío y muestra si cada uno pasa (OK) o falla (FALLO).
Uso:  python main.py
"""

from src.ejercicio_1_suma_digitos import digitsSum
from src.ejercicio_2_palindromos import isPalindrome
from src.ejercicio_3_ordenamiento import integerSort


def revisar(descripcion, obtenido, esperado):
    estado = "OK   " if obtenido == esperado else "FALLO"
    print(f"[{estado}] {descripcion} -> {obtenido}")


print("=== Ejercicio 1: Suma de dígitos ===")
revisar('digitsSum("999")', digitsSum("999"), 27)
revisar('digitsSum("9184501")', digitsSum("9184501"), 28)
revisar('digitsSum("12345")', digitsSum("12345"), 15)

print("\n=== Ejercicio 2: Palíndromos ===")
revisar('isPalindrome("aabaa")', isPalindrome("aabaa"), True)
revisar('isPalindrome("abac")', isPalindrome("abac"), False)
revisar('isPalindrome("salas")', isPalindrome("salas"), True)

print("\n=== Ejercicio 3: Ordenamiento ===")
original = [5, -2, 10, 0, 3, -7]
ordenada = integerSort(original)
revisar("integerSort([5, -2, 10, 0, 3, -7])", ordenada, [-7, -2, 0, 3, 5, 10])
revisar("la lista original NO cambió", original, [5, -2, 10, 0, 3, -7])
