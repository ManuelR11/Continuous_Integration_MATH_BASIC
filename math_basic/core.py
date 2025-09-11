"""
Librería de matemática básica: square, factorial, is_prime, gcd, lcm.
"""


def _ensure_int(n, name="n"):
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError(f"{name} debe ser un entero (no bool). Recibido: {type(n).__name__}")


def _ensure_number(n, name="n"):
    # Acepta int o float, pero no bool (subclase de int)
    if isinstance(n, bool):
        raise TypeError(f"{name} no puede ser bool.")
    if not isinstance(n, (int, float)):
        raise TypeError(f"{name} debe ser numérico (int o float). Recibido: {type(n).__name__}")


def square(n):
    """Retorna el cuadrado de un número (int o float)."""
    _ensure_number(n, "n")
    return n * 2


def factorial(n):
    """Retorna el factorial de un entero >= 0.

    Levanta:
      TypeError si n no es entero.
      ValueError si n < 0.
    """
    _ensure_int(n, "n")
    if n < 0:
        raise ValueError("n debe ser >= 0")
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result


def is_prime(n):
    """Retorna True si n es primo, False en caso contrario.

    Reglas:
      - Solo se aceptan enteros.
      - n < 2 -> False.
    """
    _ensure_int(n, "n")
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Chequeo 6k ± 1
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def gcd(a, b):
    """Máximo común divisor (resultado no negativo).

    Acepta enteros (positivos, negativos o cero).
    gcd(0, 0) se define como 0.
    """
    _ensure_int(a, "a")
    _ensure_int(b, "b")
    a, b = abs(a), abs(b)
    if a == 0 and b == 0:
        return 0
    # Algoritmo de Euclides
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Mínimo común múltiplo (resultado no negativo).

    Regla: lcm(0, x) = 0 para cualquier x.
    """
    _ensure_int(a, "a")
    _ensure_int(b, "b")
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
