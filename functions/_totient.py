"""
Euler Totient Function
"""


def totient(n: int, /) -> int:
    def calc(m: int, j: int, q: int) -> tuple:
        if not m % j:
            while not m % j: m //= j
            q -= q // j
        return m, q

    p = n  # phi
    n, p = calc(n, 2, p)
    n, p = calc(n, 3, p)
    i = 5
    while i * i <= n:
        n, p = calc(n, i, p)
        n, p = calc(n, i + 2, p)
        i += 6
    if n > 1: p -= p // n
    return p


if __name__ == '__main__':
    import doctest

    doctest.testmod()
