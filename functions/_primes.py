"""
Primes
"""
from collections import Counter
from collections.abc import Generator
from math import isqrt, gcd
from random import randint

# LOCAL #
from utils.supporting import SupportsBool

__all__ = [
    'coprime',
    'decomposition',
    'is_prime',
    'prime_factors',
    'prime_power',
    'primes_up_to',
    'primesieve',
]


def coprime(a: int, b: int, /) -> bool:
    """ Co-Primality """
    return gcd(a, b) == 1


def decomposition(n: int, /) -> dict[int, int]:
    """ Prime Decomposition """
    return dict(Counter(prime_factors(n)))


def is_prime(n: int, /) -> bool:
    """ Primality """
    if n <= 1: return False
    if n <= 3: return True
    if not n % 2 or not n % 3:
        return False
    i = 5
    while i * i <= n:
        if not n % i or not n % (i + 2):
            return False
        i += 6
    return True


# noinspection DuplicatedCode
def prime_factors(n: int, /, strict: bool = False) -> Generator[int, None, None]:
    """ Prime Factors """
    if not isinstance(n, int):
        raise TypeError('n must be integer')
    if n < 2:
        if strict:
            raise ValueError('math domain error, n must be >= 2')
        return

    while not n % 2: yield 2; n //= 2
    while not n % 3: yield 3; n //= 3
    i = 5
    while i * i <= n:
        while not n % i: yield i; n //= i
        i += 2
        while not n % i: yield i; n //= i
        i += 4
    if n > 1: yield n


def _find_witness(n: int, /, k: int = 5) -> int:  # miller-rabin
    s = 0
    d = n - 1
    while not d % 2:
        s += 1
        d //= 2
    for i in range(k):
        a = randint(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for r in range(1, s):
            x = pow(x, 2, n)
            if x == 1: return a
            if x == n - 1: break
        else:
            return a
    return 0


def prime_power(n: int, /) -> tuple:
    """
    This program uses Fermat's Little Theorem and exploits the witness <a>
    to the composite-ness of n that is found by the Miller-Rabin algorithm.

    :returns: p,k such that n=p^k, or 0,0 assumes n is an integer greater than 1
    """

    def check_p(m, p: int) -> tuple[int, int]:
        k = 0
        while m > 1 and not m % p:
            m //= p
            k += 1
        return (p, k) if m == 1 else (0, 0)

    if not n % 2:
        return check_p(n, 2)
    q = n
    while True:
        a = _find_witness(q)
        if a == 0: return check_p(n, q)
        d = gcd(pow(a, q, n) - a, q)
        if d == 1 or d == q: return 0, 0
        q = d


# noinspection DuplicatedCode
def primesieve(n: int, /) -> list[int]:
    """ Sieve For First N Primes """
    res = [0, 0] + [1] * (n - 1)
    for i in range(2, isqrt(n) + 1):
        if res[i]:
            for j in range(i * i, n + 1, i):
                res[j] = 0
    return res


def primes_up_to(n: int, /, sieve: list[SupportsBool] | None = None) -> list[int]:
    """ Primes Below N """
    if sieve is None:
        sieve = primesieve(n)
    elif len(sieve) != n + 1:
        raise ValueError('invalid sieve length')
    return [2] + [i for i in range(3, n + 1, 2) if sieve[i]]
