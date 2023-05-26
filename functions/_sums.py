"""
Sums
"""
from math import isqrt

__all__ = [
    'aliquot_count',
    'aliquot_sum',
    'div_count',
    'div_sum',
    'evens_sum',
    'gauss_sum',
    'gauss_range_sum',
    'odds_sum',
]


def aliquot_count(n: int) -> int:
    """ Count of Proper Divisors """
    return 1 + sum(len({k, n // k}) for k in range(2, isqrt(n) + 1) if not n % k)


def aliquot_sum(n: int) -> int:
    """ Sum of Proper Divisors """
    return 1 + sum(sum({k, n // k}) for k in range(2, isqrt(n) + 1) if not n % k)


def div_count(n: int) -> int:
    """ Count of Divisors """
    return sum(len({k, n // k}) for k in range(1, isqrt(n) + 1) if not n % k)


def div_sum(n: int) -> int:
    """ Sum of Divisors """
    return sum(sum({k, n // k}) for k in range(1, isqrt(n) + 1) if not n % k)


def evens_sum(a: int, b: int) -> int:
    """ Sum Of Evens from a To b """
    # NOTE: equivalent to sum(i for i in range(a, b + 1) if i % 2 == 0)
    if b < a: return 0
    if a % 2: a += 1
    if b % 2: b -= 1
    return (a + b) * (b - a + 2) // 4  # < ((a+b)/2)(((b-a)/2)+1)


def odds_sum(a: int, b: int) -> int:
    """ Sum Of Odds from a To b """
    # NOTE: equivalent to sum(i for i in range(a, b + 1) if i % 2)
    if b < a: return 0
    if a % 2: a -= 1
    if b % 2: b += 1
    return ((a + b) * (b - a)) // 4  # < (b/2)^2 - (a/2)^2


def gauss_sum(n: int) -> int:  # Triangle Numbers
    """ Gaussian Sum """
    # NOTE: equivalent to sum(range(n + 1))
    return n * (n + 1) // 2


def gauss_range_sum(a: int, b: int) -> int:
    """ Gaussian Range Sum """
    # NOTE: equivalent to sum(range(a, b + 1))
    return (a + b) * (b - a + 1) // 2


def squares_sum(n: int) -> int:  # A000330
    """ Sum Of Squares """
    return n * (n + 1) * (2 * n + 1) // 6


def cubes_sum(n: int) -> int:  # A000537
    """ Sum Of Cubes """
    return n ** 2 * (n + 1) ** 2 // 4


def pow2_sum(n: int) -> int:  # A000918
    """ Sum Of Powers Of Two """
    return 2 * (2 ** n - 1)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
