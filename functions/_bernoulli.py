"""
Bernoulli Function
"""
from fractions import Fraction
from itertools import count
from typing import SupportsInt

__all__ = ['bernoulli', 'bernoulli2']


def bernoulli(__x: SupportsInt) -> Fraction:
    x = int(__x)
    A: list[int | Fraction] = [0] * (x + 1)
    for m in range(x + 1):
        A[m] = Fraction(1, m + 1)
        for j in range(m, 0, -1):
            A[j - 1] = j * (A[j - 1] - A[j])
    return A[0]


def bernoulli2():
    A = []
    for m in count():
        A.append(Fraction(1, m + 1))
        for j in range(m, 0, -1):
            A[j - 1] = j * (A[j - 1] - A[j])
        yield A[0]
