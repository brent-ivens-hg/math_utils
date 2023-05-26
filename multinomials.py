"""
Multinomials

| m  | Sequence | Name                     | Polynomial            |
|----|----------|--------------------------|-----------------------|
| 2  | A007318  | Binomial                 | (1 + x)^n             |
| 3  | A027907  | Trinomial                | (1 + x + x^2)^n       |
| 4  | A008287  | Tetranomial/Quadrinomial | (1 + x + x^2 + x^3)^n |
| 5  | A035343  | Pentanomial              | (1 + x + ... + x^4)^n |
| 6  | A063260  | Hexanomial               | (1 + x + ... + x^5)^n |
| 7  | A063265  | Heptanomial              | (1 + x + ... + x^6)^n |
| 8  | A171890  | Octanomial               | (1 + x + ... + x^7)^n |
| 9  | A213652  | Nonanomial               | (1 + x + ... + x^8)^n |
| 10 | A213651  | Decanomial               | (1 + x + ... + x^9)^n |

"""
from functools import cache


def add(*numbers: int) -> int:
    return sum(numbers)


@cache
def binom(n: int, k: int) -> int:
    """
    https://mathworld.wolfram.com/BinomialCoefficient.html

    :param n:
    :param k:
    :returns: the binomial coefficient
    """
    if n < 0:
        if k >= 0: return (-1) ** k * binom(-n + k - 1, k)
        if k <= n: return (-1) ** (n - k) * binom(-k - 1, n - k)
        return 0
    if k < 0 or k > n: return 0
    if k == 0 or k == n: return 1
    return binom(n - 1, k - 1) + binom(n - 1, k)


@cache
def trinom(n: int, k: int) -> int:
    """
    https://mathworld.wolfram.com/TrinomialCoefficient.html

    :param n:
    :param k:
    :returns: the trinomial coefficient

    trinom(n, k) == trinom(n, -k)

    >>> from scipy.special import comb

    >>> trinom2 = lambda n, k: round(sum((-1) ** j * comb(n, j) * comb(2 * n - 2 * j, n - k - j) for j in range(n)))

    >>> trinom(19, 2)
    110797569
    >>> trinom(19, -2)
    110797569
    >>> trinom2(19, 2)
    110797569
    >>> trinomial_triangle(20)[19][19 - 2]
    110797569
    """
    if n == 0 and k == 0: return 1
    if n < abs(k): return 0
    return trinom(n - 1, k - 1) + trinom(n - 1, k) + trinom(n - 1, k + 1)


def multinom(m: int, n: int, k: int) -> int:
    """
    https://mathworld.wolfram.com/MultinomialCoefficient.html

    :param m: order
    :param n:
    :param k:
    :returns: the m-nomial coefficient

    >>> m = 4
    >>> for n in range(4):
    ...     print(list(multinom(m, n, k) for k in range((m - 1) * n + 1)))  # A008287
    [1]
    [1, 1, 1, 1]
    [1, 2, 3, 4, 3, 2, 1]
    [1, 3, 6, 10, 12, 12, 10, 6, 3, 1]
    >>> m = 5
    >>> for n in range(4):
    ...     print(list(multinom(m, n, k) for k in range((m - 1) * n + 1)))  # A035343
    [1]
    [1, 1, 1, 1, 1]
    [1, 2, 3, 4, 5, 4, 3, 2, 1]
    [1, 3, 6, 10, 15, 18, 19, 18, 15, 10, 6, 3, 1]
    """
    return sum((-1) ** i * binom(n, i) * binom(n + k - 1 - m * i, n - 1) for i in range(k // m + 1))


def binomial_triangle(n: int) -> list[list[int]]:  # A007318
    """
    https://en.wikipedia.org/wiki/Pascal%27s_triangle

    :param n: rows
    :returns: Triangle of coefficients in expansion of (1 + x)^n

    >>> for row in binomial_triangle(4): print(row)
    [1]
    [1, 1]
    [1, 2, 1]
    [1, 3, 3, 1]
    """
    return multinomial_triangle(2, n)


def trinomial_triangle(n: int) -> list[list[int]]:  # A027907
    """
    https://en.wikipedia.org/wiki/Trinomial_triangle

    :param n: rows
    :returns: Triangle of coefficients in expansion of (1 + x + x^2)^n

    >>> for row in trinomial_triangle(4): print(row)
    [1]
    [1, 1, 1]
    [1, 2, 3, 2, 1]
    [1, 3, 6, 7, 6, 3, 1]
    """
    return multinomial_triangle(3, n)


def multinomial_triangle(m: int, n: int) -> list[list[int]]:
    """
    https://en.wikipedia.org/wiki/Multinomial_theorem

    :param m: order
    :param n: rows
    :returns: Triangle of coefficients in expansion of (1 + x + x^2 + ... + x^(m-1))^n

    >>> for row in multinomial_triangle(4, 4): print(row)  # A008287
    [1]
    [1, 1, 1, 1]
    [1, 2, 3, 4, 3, 2, 1]
    [1, 3, 6, 10, 12, 12, 10, 6, 3, 1]
    >>> for row in multinomial_triangle(5, 4): print(row)  # A035343
    [1]
    [1, 1, 1, 1, 1]
    [1, 2, 3, 4, 5, 4, 3, 2, 1]
    [1, 3, 6, 10, 15, 18, 19, 18, 15, 10, 6, 3, 1]
    """
    if n < 1: return []
    res = [[1]]
    for _ in range(1, n):
        res.append(list(map(add, *([0] * i + res[-1] + [0] * (m - i - 1) for i in range(m)))))
    return res


if __name__ == '__main__':
    import doctest

    doctest.testmod()
