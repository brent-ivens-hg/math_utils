"""
Other
"""
from math import sqrt
from typing import SupportsFloat

from math_utils.constants import PHI, SQRT3, SQRT3_2


def truncate(number: SupportsFloat, ndigits: int) -> float:
    integral, fractional = str(float(number)).split('.')
    return float(f'{integral}.{fractional[:ndigits]}')


def eq_triangle_area(a: float) -> float:
    """
    :param a: side length
    :returns: Area of Equilateral Triangle with side length a

    >>> eq_triangle_area(1)
    0.4330127018922193
    >>> eq_triangle_area(2)
    1.7320508075688772
    """
    return SQRT3_2 / 2 * a ** 2


def equilateral_side(area: float) -> float:
    """
    >>> round(equilateral_side(sqrt(3) / 4))
    1
    >>> round(equilateral_side(sqrt(3)))
    2
    """
    return sqrt((4 * SQRT3 * area) / 3)


def iso_triangle_area(a: float, b: float) -> float:
    """
    :param a: leg length
    :param b: base length
    :returns: Area of Isosceles Triangle with leg length a and base length b
    """
    # -> (b / 2) * sqrt(a ** 2 - b ** 2 / 4)
    return b / 4 * sqrt((2 * a + b) * (2 * a - b))


def gold_b(a: float) -> float:
    """
    :param a: large quantity
    :returns: small quantity b
    """
    return a * (PHI - 1)


def gold_a(b: float) -> float:
    """
    :param b: small quantity
    :returns: large quantity a
    """
    return b * PHI


def tetrate(a: int, b: int) -> int:
    """
    Tetration Function: computes repeated exponentiation (power tower)

    >>> tetrate(2, 4)
    65536
    >>> tetrate(3, 3)
    7625597484987
    """
    res = 1
    for _ in range(b):
        res = a ** res
    return res


def count_consecutive(number: int) -> int:
    """
    counts in how many ways n can be expressed as a sum of consecutive numbers
    """
    count, k = 0, 1
    while k * (k + 1) < 2 * number:
        a = (1 * number - (k * (k + 1)) / 2) / (k + 1)
        count += a.is_integer()
        k += 1
    return count


def mousetrap(n: int) -> int:
    """
    A002467: The game of Mousetrap with n cards

    >>> list(map(mousetrap, range(10)))
    [0, 1, 1, 4, 15, 76, 455, 3186, 25487, 229384]
    """
    return n if n < 2 else (n - 1) * (mousetrap(n - 1) + mousetrap(n - 2))


def t(n):
    """
    nth-order Triangular Number
    """
    return lambda m: m * (m ** n + 1) // 2


def v2(n: int) -> int:
    """
    A007814: 2-adic valuation of n

    >>> v2(6 * 8), v2(6) + v2(8)
    (4, 4)
    """
    return (n - (n & n - 1)).bit_length() - 1


def w(n: int) -> int:
    """
    A000120: 1's-counting sequence
    """
    return n.bit_count()


def cmp(a, b) -> int:  # lambda a, b: (a > b) - (a < b)
    if a < b: return -1
    if a > b: return +1
    return 0


def egcd(a: int, b: int):
    """
    Extended Euclidean algorithm

    def mod_inv(a, m):
        gcd_, x, y = egcd(a, m)
        if gcd_ != 1: return None
        return x % m
    """
    x, y, u, v = 0, 1, 1, 0
    while a > 0:
        q, r = divmod(b, a)
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd_ = b
    return gcd_, x, y


def mod_inv(a: int, m: int) -> int:
    """
    Modular Inverse

    >>> mod_inv(7, 26)
    15
    """
    try: return pow(a, -1, m)
    except ValueError: return -1  # not co-prime


if __name__ == '__main__':
    import doctest

    doctest.testmod()
