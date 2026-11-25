# Clever Internship – Desafío inicial

# Clever Internship – Desafío inicial

![Tests](https://github.com/DjDiego007/clever-internship-challenge/actions/workflows/tests.yml/badge.svg)

Solución de los 3 ejercicios del desafío técnico, escrita en **Python 3** sin librerías externas.

| # | Ejercicio | Función | Archivo |
|---|-----------|---------|---------|
| 1 | Suma de dígitos | `digitsSum(inputInt)` | `src/ejercicio_1_suma_digitos.py` |
| 2 | Palíndromos | `isPalindrome(inputStr)` | `src/ejercicio_2_palindromos.py` |
| 3 | Ordenamiento | `integerSort(inputArray)` | `src/ejercicio_3_ordenamiento.py` |

## Cómo ejecutarlo

```bash
python main.py              # muestra los ejemplos del reto con OK / FALLO
python -m unittest -v       # corre todas las pruebas automáticas
```

Solo se necesita Python 3.8 o superior.

## Explicación de cada solución (versión corta)

### 1. Suma de dígitos
Voy sacando el último dígito con `% 10`, lo sumo, y lo quito con `// 10`, hasta que el número llega a 0.
Ejemplo con `12345`: 5 + 4 + 3 + 2 + 1 = **15**.
- Complejidad: O(d), donde *d* es la cantidad de dígitos.

### 2. Palíndromos
Uso dos índices, uno al inicio y otro al final, y los voy acercando comparando letra por letra.
Si encuentro una pareja distinta, regreso `False`; si llegan al centro sin diferencias, `True`.
Ignoro mayúsculas y espacios como detalle extra.
- Complejidad: O(n). No creo copias invertidas del texto.

### 3. Ordenamiento (Merge Sort)
No usé `sort()` ni `sorted()`. Implementé **Merge Sort**: divido la lista a la mitad hasta tener
pedazos de 1 elemento y luego los mezclo tomando siempre el menor.

```
[5, -2, 10, 0]
 /          \
[5, -2]   [10, 0]      <- dividir
 /  \       /  \
[5] [-2]  [10] [0]
 \  /       \  /
[-2, 5]   [0, 10]      <- mezclar ordenando
    \       /
 [-2, 0, 5, 10]
```
- Devuelve **una lista nueva** y la original no se modifica (hay una prueba que lo verifica).
- Complejidad: O(n log n).

## Decisiones que tomé
- Mantuve los nombres de las funciones tal como están en el enunciado.
- Consideré casos borde: lista vacía, un solo elemento, repetidos, negativos y el número 0.
- Agregué pruebas automáticas para demostrar que funcionan, no solo con los ejemplos.

## Autor

**Juan Diego Juarez Atanacio**

Universidad Hybridge

Estudiante de Ingeniería de Software

Correo: diegojuaa07@gmail.com
