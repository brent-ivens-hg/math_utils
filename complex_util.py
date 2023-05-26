"""
Complex Utils
"""
from cmath import *


def as_tuple(__z: complex) -> tuple[float, float]:
    """
    >>> as_tuple(1j)
    (0.0, 1.0)
    >>> sorted({1+0j, 0+1j, -1+0j, 0-1j, 1+1j, -1+1j, -1-1j, 1-1j, 0+0j}, key=as_tuple)
    [(-1-1j), (-1+0j), (-1+1j), -1j, 0j, 1j, (1-1j), (1+0j), (1+1j)]
    """
    return __z.real, __z.imag


def modulus(__z: complex) -> float:
    """
    Magnitude

    >>> modulus(1j)
    1.0
    """
    return abs(__z)


def nth_root(__z: complex, n: int) -> list[complex]:
    """
    >>> nth_root(1j, 2)
    [(-0.7071067811865477-0.7071067811865475j), (0.7071067811865476+0.7071067811865476j)]
    """
    mod = modulus(__z) ** (1 / n)
    arg = argument(__z)
    return sorted((mod * exp((arg + k * tau) * 1j / n) for k in range(n)), key=as_tuple)


argument = phase
magnitude = modulus

if __name__ == '__main__':
    import doctest

    doctest.testmod()
