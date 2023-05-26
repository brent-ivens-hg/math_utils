"""
Faulhaber's Function

:IMPLEMENTATION:

from math import comb
from ._bernoulli import bernoulli2

def faulhaber(exp: SupportsInt, num: SupportsInt) -> int:
    n, k = int(exp), int(num)
    s = 0
    for j, a in enumerate(bernoulli2()):
        if j > k: break
        s = s + comb(k + 1, j) * a * n ** (k + 1 - j)
    return s // (k + 1)

IT'S MORE EFFICIENT TO USE 'sum(i ** exp for i in range(1, num))' IN THIS CASE
"""
from collections.abc import Callable
from fractions import Fraction
from typing import SupportsInt

__all__ = ['faulhaber']


def next_u(__u: list[int]) -> list[int]:
    n = len(__u)
    __u.append(1)
    for i in range(n - 1, 0, -1):
        __u[i] = i * __u[i] + __u[i - 1]
    return __u


def next_v(__v: list[int]) -> list[int]:
    n = len(__v) - 1
    v = [i * (1 - n) for i in __v]
    v.append(1)
    for i in range(n):
        v[i + 1] += __v[i]
    return v


def coefficients(n: int) -> list[Fraction]:
    if n == 0: return [Fraction(), Fraction(1)]

    u = [0, 1]
    v = [[1], [1, 1]]

    for _ in range(n - 1):  # TODO : optimize, -bernoulli-, STERLING?
        v.append(next_v(v[-1]))
        u = next_u(u)

    v.append(next_v(v[-1]))

    coeffs = [Fraction()] * (n + 2)
    for j, a in enumerate(u):
        a = Fraction(a, j + 1)
        for k, b in enumerate(v[j + 1]):
            coeffs[k] += a * b
    return coeffs


def faulhaber(exp: SupportsInt) -> Callable[[int], Fraction]:  # Fractions to increase accuracy
    coeffs = coefficients(int(exp))
    return lambda k: sum(coeff * k ** j for j, coeff in enumerate(coeffs) if coeff)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
