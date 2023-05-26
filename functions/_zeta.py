"""
Riemann-Zeta Function
"""
from math import comb

__all__ = ['zeta', 'zeta_alt', 'zeta_euler', 'zeta_euler_maclaurin', 'zeta_inf', 'zeta_knopp_hasse']

with open('primes_1M.pickle', 'rb') as file:
    PRIMES = __import__('pickle').load(file)

# ITERATIONS #
IOTA = 1_000_000
IOTA2 = 100


def zeta_inf(s: complex) -> complex:  # absolute trash
    """
    Infinite Series

    >>> zeta_inf(2)
    1.64493306684877
    """
    if s == 1:
        return float('inf')
    return sum(1 / n ** s for n in range(1, IOTA + 1))


def zeta_alt(s: complex) -> complex:  # more accurate but slower
    """
    Alternative Series

    >>> zeta_alt(2)
    1.6449340668471673
    """
    if s == 1:
        return float('inf')
    return sum((-1) ** n * n ** -s for n in range(1, IOTA + 1)) / (2 ** (1 - s) - 1)


def zeta_euler(s: complex) -> complex:  # less accurate but faster
    """
    Euler Product formula

    >>> zeta_euler(2)
    1.6449340607865373
    """
    res = 1
    for p in PRIMES:
        res *= 1 - p ** -s
    return 1 / abs(res)


def zeta_knopp_hasse(s: complex) -> complex:  # accurate & fast
    """
    # https://mathworld.wolfram.com/RiemannZetaFunction.html#eqn21

    >>> zeta_knopp_hasse(2)
    1.6449340668482266
    """
    if s == 1:
        return float('inf')
    return sum(
        1 / 2 ** (n + 1) * sum(
            (-1) ** k * comb(n, k) * (k + 1) ** -s for k in range(n + 1)
        ) for n in range(IOTA2)
    ) / (1 - 2 ** (1 - s))


zeta = zeta_knopp_hasse

A = (
    12, -720, 30240, -1209600, 47900160, -1.8924375803183791606e9, 7.47242496e10, -2.950130727918164224e12,
    1.1646782814350067249e14, -4.5979787224074726105e15, 1.8152105401943546773e17, -7.1661652561756670113e18
)


def zeta_euler_maclaurin(x: float, q: float = 1) -> complex:  # scipy: most accurate & fastest
    """
    Euler-Maclaurin Summation Formula

    >>> zeta_euler_maclaurin(2)
    1.6449340668482266
    """
    if x == 1:
        return float('inf')
    if x < 1:
        return float('nan')

    if q <= 0:
        if q == int(q):
            return float('inf')
        if x != int(x):
            raise ValueError('domain error: q^-x not defined')

    if q > 1e8:
        """
        Asymptotic expansion: https://dlmf.nist.gov/25.11#E43
        """
        return (1 / (x - 1) + 1 / (2 * q)) * pow(q, 1 - x)

    s = pow(q, -x)
    a = q
    i = 0
    b = 0
    while (i < 9) or (a <= 9):
        i += 1
        a += 1
        b = pow(a, -x)
        s += b
    w = a
    s += b * w / (x - 1)
    s -= 0.5 * b
    a = 1
    k = 0
    for i in range(12):
        a *= x + k
        b /= w
        t = a * b / A[i]
        s = s + t
        k += 1
        a *= x + k
        b /= w
        k += 1
    return s


if __name__ == '__main__':
    import doctest

    doctest.testmod()
