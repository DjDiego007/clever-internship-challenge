"""
Pruebas automáticas. Se corren con:  python -m unittest -v
(no necesita instalar nada, unittest viene con Python)
"""

import random
import unittest

from src.ejercicio_1_suma_digitos import digitsSum
from src.ejercicio_2_palindromos import isPalindrome
from src.ejercicio_3_ordenamiento import integerSort


class TestSumaDigitos(unittest.TestCase):
    def test_ejemplos_del_reto(self):
        self.assertEqual(digitsSum("999"), 27)
        self.assertEqual(digitsSum("9184501"), 28)
        self.assertEqual(digitsSum("12345"), 15)

    def test_acepta_enteros(self):
        self.assertEqual(digitsSum(12345), 15)

    def test_cero_y_un_digito(self):
        self.assertEqual(digitsSum(0), 0)
        self.assertEqual(digitsSum(7), 7)

    def test_negativos(self):
        self.assertEqual(digitsSum(-123), 6)


class TestPalindromos(unittest.TestCase):
    def test_ejemplos_del_reto(self):
        self.assertTrue(isPalindrome("aabaa"))
        self.assertFalse(isPalindrome("abac"))
        self.assertTrue(isPalindrome("salas"))

    def test_palabras_del_enunciado(self):
        for palabra in ["salas", "oso", "reconocer", "oro"]:
            self.assertTrue(isPalindrome(palabra))

    def test_casos_borde(self):
        self.assertTrue(isPalindrome(""))
        self.assertTrue(isPalindrome("a"))
        self.assertFalse(isPalindrome("ab"))

    def test_mayusculas_y_espacios(self):
        self.assertTrue(isPalindrome("Anita lava la tina"))


class TestOrdenamiento(unittest.TestCase):
    def test_ejemplo_del_reto(self):
        self.assertEqual(integerSort([5, -2, 10, 0, 3, -7]),
                         [-7, -2, 0, 3, 5, 10])

    def test_no_modifica_la_original(self):
        original = [3, 1, 2]
        resultado = integerSort(original)
        self.assertEqual(original, [3, 1, 2])
        self.assertIsNot(resultado, original)

    def test_casos_borde(self):
        self.assertEqual(integerSort([]), [])
        self.assertEqual(integerSort([1]), [1])
        self.assertEqual(integerSort([2, 1]), [1, 2])

    def test_repetidos_y_ya_ordenada(self):
        self.assertEqual(integerSort([3, 1, 3, 1]), [1, 1, 3, 3])
        self.assertEqual(integerSort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(integerSort([3, 2, 1]), [1, 2, 3])

    def test_contra_listas_aleatorias(self):
        # Aquí SÍ uso sorted(), pero solo para comprobar mi resultado en las pruebas,
        # nunca dentro de la solución.
        for _ in range(200):
            lista = [random.randint(-100, 100) for _ in range(random.randint(0, 30))]
            self.assertEqual(integerSort(lista), sorted(lista))


if __name__ == "__main__":
    unittest.main()
