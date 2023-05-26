"""
Main Module
"""
from collections import deque
from collections.abc import Generator, Iterable, Sequence
from math import gcd, log, prod, isqrt, isclose
from operator import mul
from typing import SupportsIndex
# LOCAL #
from math_utils.functions._primes import decomposition

__all__ = [
    'divisors',
    'is_perfect_power',
    'is_perfect_square',
    'lcm',
    'linear_recurrence',
]


def divisors(n: int, /, *, proper: bool = False) -> Generator[int, None, None]:
    """ Divisors """
    factor_dict = decomposition(n)
    fs = list(factor_dict)

    def _divisors(i: int = 0) -> Generator[int, None, None]:
        if i == len(fs): yield 1; return
        pows = [1]
        for j in range(factor_dict[fs[i]]): pows.append(pows[-1] * fs[i])
        yield from (p * q for q in _divisors(i + 1) for p in pows)

    if proper:
        yield from filter(n.__ne__, _divisors())
    else:
        yield from _divisors()


def double_factorial(n: int, /) -> int:  # A006882
    """
    :returns: n!!

    >>> double_factorial(5)  # A001147
    15
    >>> double_factorial(8)  # A000165
    384
    """
    return prod(range(n % 2 or 2, n + 1, 2))


def is_perfect_power(a: int, b: int, /) -> bool:
    """ Perfect Power """
    return isclose(b ** int(round(log(a, b))), a)


def is_perfect_square(n: int, /) -> bool:
    """ Perfect Square """
    return n >= 0 and isqrt(n) ** 2 == n


# noinspection PyPep8Naming
class lcm:
    def __new__(cls, *xs: int) -> int:
        return cls.from_iterable(xs)

    @classmethod
    def from_iterable(cls, __iterable: Iterable[SupportsIndex], /) -> int:
        """ :returns: the lowest common multiple of iterable """
        res = 1
        for x in __iterable:
            res //= gcd(res, x)
            res *= x
        return res


def linear_recurrence(ker: Sequence[int], init: Sequence[int]) -> Generator[int, None, None]:
    # NOTE: for nth value use matrix-exponentiation method; see `big_generalized_fibonacci_numbers.py`
    """
    LinearRecurrence[{a, b}, {1, 1}, 5] -> {1,1,a+b,b+a(a+b),b(a+b)+a(b+a(a+b)),...}

    :param ker:  kernel
    :param init: initial-values
    :returns: the sequence of length n obtained by iterating the linear recurrence
              with kernel ker starting with initial-values init.

    >>> from itertools import islice

    >>> list(islice(linear_recurrence([1, 1], [1, 1]), 10))  # Fibonacci
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    >>> list(islice(linear_recurrence([1, 1], [1, 3]), 10))  # Lucas
    [1, 3, 4, 7, 11, 18, 29, 47, 76, 123]
    >>> list(islice(linear_recurrence([2, 1], [0, 1]), 10))  # Pell
    [0, 1, 2, 5, 12, 29, 70, 169, 408, 985]
    >>> list(islice(linear_recurrence([2, 1], [2, 2]), 10))  # Pell-Lucas
    [2, 2, 6, 14, 34, 82, 198, 478, 1154, 2786]

    >>> list(islice(linear_recurrence([1, 1, 1], [1, 1, 1]), 10))  # Tribonacci
    [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
    >>> list(islice(linear_recurrence([0, 1, 1], [1, 0, 0]), 10))  # Padovan
    [1, 0, 0, 1, 0, 1, 1, 1, 2, 2]
    >>> list(islice(linear_recurrence([0, 1, 1], [3, 0, 2]), 10))  # Perrin
    [3, 0, 2, 3, 2, 5, 5, 7, 10, 12]
    """
    if len(ker) != len(init): raise ValueError("'ker' and 'init' must have same length")
    yield from init
    res = deque(reversed(init), maxlen=len(init))
    while True:
        res.appendleft(sum(map(mul, ker, res)))  # dot product
        yield res[0]
