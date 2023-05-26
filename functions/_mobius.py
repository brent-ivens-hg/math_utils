"""
Möbius Function: https://en.wikipedia.org/wiki/M%C3%B6bius_function
"""
from typing import SupportsInt

__all__ = ['mobius']


def mobius(__x: SupportsInt) -> int:
    x = int(__x)

    if x < 1: raise ValueError('math domain error')

    primes = set()

    if x % 2 == 0:
        x //= 2
        if x % 2 == 0: return 0
        primes.add(2)

    i = 3
    while i * i <= x:
        while x % i == 0:
            if i in primes: return 0
            primes.add(i)
            x //= i
        i += 2

    return -1 if (len(primes) + (x > 1)) % 2 else 1
