"""
Polygonal Module

A general formula for polygonal numbers is P(n,k) = (n-2)*(k-1)*k/2 + k, where P(n,k) is the k-th n-gonal number.

...,21,10,3 <- 0 -> 1,6,15,...
'->': A014105:        Hexagonal Numbers: a(n) = n(2n - 1) -> linear_recurrence([3, -3, 1], [0, 1,  6], n)
'<-': A014105: Second Hexagonal Numbers: a(n) = n(2n + 1) -> linear_recurrence([3, -3, 1], [0, 3, 10], n)

x1,x2,x3 = x2,x3,Ax1 + Bx2 + Cx3

p == c - 3b + 3a | p = previous value
p == 6 - 3*1+3*a

* -> SECOND VARIATION => init = [0,n,3n]

NON  = linear_recurrence([3, -3, 1], [0, 1,  9])  # 0  1  9 24 46 ...
NON* = linear_recurrence([3, -3, 1], [0, 6, 19])  # 0  6 19 39 66 ...

OCT  = linear_recurrence([3, -3, 1], [0, 1,  8])  # 0  1  8 21 40 ...
OCT* = linear_recurrence([3, -3, 1], [0, 5, 16])  # 0  5 16 33 56 ...

HEP  = linear_recurrence([3, -3, 1], [0, 1,  7])  # 0  1  7 18 34 ...
HEP* = linear_recurrence([3, -3, 1], [0, 4, 13])  # 0  4 13 27 46 ...

HEX  = linear_recurrence([3, -3, 1], [0, 1,  6])  # 0  1  6 15 28 ...
HEX* = linear_recurrence([3, -3, 1], [0, 3, 10])  # 0  3 10 21 36 ...  ->  odd-indexed triangular numbers?

PEN  = linear_recurrence([3, -3, 1], [0, 1,  5])  # 0  1  5 12 22 ...
PEN* = linear_recurrence([3, -3, 1], [0, 2,  7])  # 0  2  7 15 26 ...

SQR  = linear_recurrence([3, -3, 1], [0, 1,  4])  # 0  1  4  9 16 ...

TRI  = linear_recurrence([3, -3, 1], [0, 1,  3])  # 0  1  3  6 10 ...

INT  = linear_recurrence([3, -3, 1], [0, 1,  2])  # 0  1  2  3  4 ...

def search(n, p):  # finding the second p-gonal numbers
    a, b, c = 0, 1, p
    for _ in range(10):
        a, b, c = c - 3 * b + 3 * a, a, b
        print(a, end=', ')

"""
from math import pi, tan, isqrt

__all__ = ['is_triangular', 'is_perfect_square', 'is_pentagonal', 'is_hexagonal',
           'is_heptagonal', 'is_octagonal', 'is_nonagonal', 'is_decagonal',
           'is_polygonal',
           'triangular_number', 'square_number', 'pentagonal_number', 'hexagonal_number',
           'heptagonal_number', 'octagonal_number', 'nonagonal_number', 'decagonal_number',
           'polygonal_number',
           'triangular_inverse', 'square_inverse', 'pentagonal_inverse', 'hexagonal_inverse',
           'heptagonal_inverse', 'octagonal_inverse', 'nonagonal_inverse', 'decagonal_inverse',
           'polygonal_inverse']


class PolygonalException(Exception):
    pass


def is_triangular(n: int, /) -> bool:
    # equivalent to `is_perfect_square(1 + 8 * n)`
    if n < 0: return False
    k = isqrt(n + n)
    return k * (k + 1) == 2 * n


def is_perfect_square(n: int, /) -> bool:
    return 0 <= n == isqrt(n) ** 2


def is_pentagonal(n: int, /) -> bool:
    # `is_perfect_square(1 + 24 * n)` would yield the generalized pentagonal numbers: A001318
    if n < 0: return False
    if n == 0: return True
    k = 1 + 24 * n
    s = isqrt(k)
    return s * s == k and (s + 1) % 6 == 0


def is_hexagonal(n: int, /) -> bool:
    # `is_perfect_square(1 + 8 * n)` would yield the triangular numbers
    if n < 0: return False
    if n == 0: return True
    k = 1 + 8 * n
    s = isqrt(k)
    return s * s == k and (s + 1) % 4 == 0


def is_heptagonal(n: int, /) -> bool:
    # `is_perfect_square(9 + 40 * n)` would yield the generalized heptagonal numbers: A085787
    if n < 0: return False
    if n == 0: return True
    k = 9 + 40 * n
    s = isqrt(k)
    return s * s == k and (s + 3) % 10 == 0


def is_octagonal(n: int, /) -> bool:
    # `is_perfect_square(1 + 3 * n)` would yield the generalized octagonal numbers: A001082
    if n < 0: return False
    if n == 0: return True
    k = 1 + 3 * n
    s = isqrt(k)
    return s * s == k and (s + 1) % 3 == 0


def is_nonagonal(n: int, /) -> bool:
    # `is_perfect_square(1 + 3 * n)` would yield the generalized nonagonal numbers: A118277
    if n < 0: return False
    if n == 0: return True
    k = 25 + 56 * n
    s = isqrt(k)
    return s * s == k and (s + 5) % 14 == 0


def is_decagonal(n: int, /) -> bool:
    # `is_perfect_square(1 + 3 * n)` would yield the generalized decagonal numbers: A074377
    if n < 0: return False
    if n == 0: return True
    k = 9 + 16 * n
    s = isqrt(k)
    return s * s == k and (s + 3) % 8 == 0


def is_polygonal(n: int, p: int, /) -> bool:
    if n < 0 or p < 2: return False
    if n == 0: return True
    k = 8 * (p - 2) * n + (p - 4) ** 2
    s = isqrt(k)
    return s * s == k and (s + (p - 4)) % (2 * (p - 2)) == 0


def triangular_number(n: int, /) -> int:  # A000217
    return n * (n + 1) // 2  # equivalent to `comb(n + 1, 2)`


def square_number(n: int, /) -> int:  # A000290
    return n * n


def pentagonal_number(n: int, /) -> int:  # A000326
    return n * (3 * n - 1) // 2


def hexagonal_number(n: int, /) -> int:  # A000384
    return n * (2 * n - 1)


def heptagonal_number(n: int, /) -> int:  # A000566
    return n * (5 * n - 3) // 2


def octagonal_number(n: int, /) -> int:  # A000567
    return n * (3 * n - 2)


def nonagonal_number(n: int, /) -> int:  # A001106
    return n * (7 * n - 5) // 2


def decagonal_number(n: int, /) -> int:  # A001107
    return n * (4 * n - 3)


def polygonal_number(n: int, p: int, /) -> int:
    """ Nth P-gonal Number """
    if n < 0: raise PolygonalException('n should be positive or 0')
    if p < 2: raise PolygonalException('p should be larger than 2')
    # triangle count * triangle surface - overlap
    return (p - 2) * triangular_number(n) - n * (p - 3)


def triangular_inverse(n: int, /) -> int:  # A003056
    # n repeats n+1 times
    return (isqrt(1 + 8 * n) - 1) // 2


def square_inverse(n: int, /) -> int:  # A000196
    # n repeats 2n+1 times
    return isqrt(n)


def pentagonal_inverse(n: int, /) -> int:  # A180447
    # n repeats 3n+1 times
    return (1 + isqrt(1 + 24 * n)) // 6


def hexagonal_inverse(n: int, /) -> int:  # A351846
    # n repeats 4n+1 times
    return (1 + isqrt(1 + 8 * n)) // 4


def heptagonal_inverse(n: int, /) -> int:
    # n repeats 5n+1 times
    return (3 + isqrt(9 + 40 * n)) // 10


def octagonal_inverse(n: int, /) -> int:
    # n repeats 6n+1 times
    return (1 + isqrt(1 + 3 * n)) // 3


def nonagonal_inverse(n: int, /) -> int:
    # n repeats 7n+1 times
    return (5 + isqrt(25 + 56 * n)) // 14


def decagonal_inverse(n: int, /) -> int:
    # n repeats 8n+1 times
    return (3 + isqrt(9 + 16 * n)) // 8


def polygonal_inverse(n: int, p: int, /) -> int:
    # n repeats n(p-2)+1 times
    return ((p - 4) + isqrt(8 * (p - 2) * n + (p - 4) ** 2)) // (2 * (p - 2))


def np_range(p: int, n: int, /) -> list[int]:
    """
    First N P-gonal Numbers

    >>> np_range(3, 10)   # Triangle Numbers
    [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
    >>> np_range(4, 10)   # Square Numbers
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    >>> np_range(5, 10)   # Pentagonal Numbers
    [0, 1, 5, 12, 22, 35, 51, 70, 92, 117]
    >>> np_range(6, 10)   # Hexagonal Numbers
    [0, 1, 6, 15, 28, 45, 66, 91, 120, 153]
    >>> np_range(7, 10)   # Heptagonal Numbers
    [0, 1, 7, 18, 34, 55, 81, 112, 148, 189]
    >>> np_range(8, 10)   # Octagonal Numbers
    [0, 1, 8, 21, 40, 65, 96, 133, 176, 225]
    >>> np_range(9, 10)   # Nonagonal Numbers
    [0, 1, 9, 24, 46, 75, 111, 154, 204, 261]
    >>> np_range(10, 10)  # Decagonal Numbers
    [0, 1, 10, 27, 52, 85, 126, 175, 232, 297]
    """
    return [polygonal_number(i, p) for i in range(n)]


def ASF(n: int, d: int = 1, n0: int = 1, /) -> int:
    """ Arithmetic Sequence Formula for Nth term """
    # first term + position * common difference
    return n0 + (n - 1) * d


# for p in range(3, 10):
#     pn = np_range(p, 10)
#     print([b - a for a, b in zip(pn, pn[1:])], [ASF(i, p - 2) for i in range(1, 10)], sep=' <=> ')


def polygon_perimeter(sides: int, length: int, /) -> int:
    """
    :returns: the perimeter of a regular n-sided polygon with the given length
    """
    return sides * length


def polygon_apothem(sides: int, length: int, /) -> float:
    """
    :returns: the shortest distance from the center to the side in a regular polygon
    """
    return length / (2 * tan(pi / sides))


def polygon_area(sides: int, length: int, /) -> float:
    """
    :returns: the area of a regular n-sided polygon with the given length
    """
    return polygon_perimeter(sides, length) * polygon_apothem(sides, length) / 2

# todo: perimeter/area of polygram: https://en.wikipedia.org/wiki/Polygram_(geometry)
