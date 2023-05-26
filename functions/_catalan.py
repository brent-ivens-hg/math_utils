"""
Catalan
"""
from itertools import pairwise
from math import comb

__all__ = ['catalan', 'catalan2', 'sequence', 'super_trapezoid', 'super_triangle', 'trapezoid', 'triangle']


def catalan(n: int):  # A000108
    """
    Catalan Numbers

    https://en.wikipedia.org/wiki/Catalan_number

    :param n: index
    :returns: C(n) (= nth Catalan number)

    >>> list(map(catalan, range(10)))
    [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]
    >>> catalan(20)
    6564120420
    """
    return comb(2 * n, n) // (n + 1)  # (2n)!/(n!(n+1)!)


def sequence(n: int) -> list[int]:  # A000108
    """
    Catalan Sequence

    :param n: length
    :returns: linear array

    >>> sequence(10)
    [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]
    """
    DP = [0] * (n + 1)
    DP[1] = flag = h = 1
    res = []
    for i in range(2 * n - 1):
        if flag:
            for k in range(h, 0, -1): DP[k] += DP[k - 1]
            h += 1
            res.append(DP[1])
        else:
            for k in range(1, h, +1): DP[k] += DP[k + 1]
        flag ^= 1
    return res


def catalan2(n: int, k: int) -> int:  # A009766
    """
    Catalan's Triangle Numbers

    :param n: row index
    :param k: column index
    :returns: T(n, k)
    """
    if n >= 0 and k == 0: return 1
    if n >= 1 and k == 1: return n
    return comb(n + k, k) - comb(n + k, k - 1)


def triangle(n: int) -> list[list[int]]:  # A009766
    """
    Catalan's Triangle

    https://en.wikipedia.org/wiki/Catalan%27s_triangle#General_formula

    :param n: number of rows
    :returns: triangular array

    t_i = [number above (or 0 if missing)] + [number to the left (or 0 if missing)]

    >>> from pprint import pprint

    >>> pprint(triangle(6))
    [[1],
     [1, 1],
     [1, 2, 2],
     [1, 3, 5, 5],
     [1, 4, 9, 14, 14],
     [1, 5, 14, 28, 42, 42]]
    """
    # By definition, Catalan's trapezoid of order m=1 is Catalan's triangle
    return trapezoid(1, n)


def catalan3(m: int, n: int, k: int) -> int:
    """
    Catalan's Trapezoid Numbers

    https://en.wikipedia.org/wiki/Catalan%27s_triangle#Generalization

    >>> from pprint import pprint

    >>> for M in range(1, 3 + 1):
    ...     print('ORDER:', M)
    ...     pprint([[catalan3(M, N, K) for K in range(5)] for N in range(5)])
    ORDER: 1
    [[1, 0, 0, 0, 0],
     [1, 1, 0, 0, 0],
     [1, 2, 2, 0, 0],
     [1, 3, 5, 5, 0],
     [1, 4, 9, 14, 14]]
    ORDER: 2
    [[1, 1, 0, 0, 0],
     [1, 2, 2, 0, 0],
     [1, 3, 5, 5, 0],
     [1, 4, 9, 14, 14],
     [1, 5, 14, 28, 42]]
    ORDER: 3
    [[1, 1, 1, 0, 0],
     [1, 2, 3, 3, 0],
     [1, 3, 6, 9, 9],
     [1, 4, 10, 19, 28],
     [1, 5, 15, 34, 62]]
    """
    if 0 <= k < m:          return comb(n + k, k)
    if m <= k <= n + m - 1: return comb(n + k, k) - comb(n + k, k - m)
    return 0


def trapezoid(m: int, n: int) -> list[list[int]]:
    """
    Catalan's Trapezoid(s)

    https://en.wikipedia.org/wiki/Catalan%27s_triangle#Generalization

    :param m: order (= number of starting columns)
    :param n: number of rows
    :returns: trapezoidal array

    >>> from pprint import pprint

    >>> pprint(trapezoid(2, 6))
    [[1, 1],
     [1, 2, 2],
     [1, 3, 5, 5],
     [1, 4, 9, 14, 14],
     [1, 5, 14, 28, 42, 42],
     [1, 6, 20, 48, 90, 132, 132]]
    >>> pprint(trapezoid(3, 6))  # A279004
    [[1, 1, 1],
     [1, 2, 3, 3],
     [1, 3, 6, 9, 9],
     [1, 4, 10, 19, 28, 28],
     [1, 5, 15, 34, 62, 90, 90],
     [1, 6, 21, 55, 117, 207, 297, 297]]
    """
    if n < 1: return []
    res = [[1] * m]
    for _ in range(n - 1):
        row = [1]
        for above in res[-1][1:]:
            left = row[-1]
            row.append(above + left)
        row.append(row[-1])
        res.append(row)
    return res


def super_triangle(n: int) -> list[list[int]]:  # A144944
    """
    Super-Catalan Triangle

    :param n: number of rows
    :returns: triangular array

    t_i = [number above and left (or 0 if missing)] + [number above (or 0 if missing)] + [number to the left (or 0 if missing)]

    >>> from pprint import pprint

    >>> pprint(super_triangle(6))
    [[1],
     [1, 1],
     [1, 3, 3],
     [1, 5, 11, 11],
     [1, 7, 23, 45, 45],
     [1, 9, 39, 107, 197, 197]]
    """
    # By definition, Super-Catalan's trapezoid of order m=1 is Super-Catalan's triangle
    return super_trapezoid(1, n)


def super_trapezoid(m: int, n: int) -> list[list[int]]:
    """
    Super-Catalan's Trapezoid(s)

    https://en.wikipedia.org/wiki/Catalan%27s_triangle#Generalization

    :param m: order (= number of starting columns)
    :param n: number of rows
    :returns: trapezoidal array

    >>> from pprint import pprint

    >>> pprint(super_trapezoid(2, 6))
    [[1, 1],
     [1, 3, 3],
     [1, 5, 11, 11],
     [1, 7, 23, 45, 45],
     [1, 9, 39, 107, 197, 197],
     [1, 11, 59, 205, 509, 903, 903]]
    >>> pprint(super_trapezoid(3, 6))
    [[1, 1, 1],
     [1, 3, 5, 5],
     [1, 5, 13, 23, 23],
     [1, 7, 25, 61, 107, 107],
     [1, 9, 41, 127, 295, 509, 509],
     [1, 11, 61, 229, 651, 1455, 2473, 2473]]
    """
    if n < 1: return []
    res = [[1] * m]
    for _ in range(n - 1):
        row = [1]
        for above_left, above in pairwise(res[-1]):
            left = row[-1]
            row.append(above_left + above + left)
        row.append(row[-1])
        res.append(row)
    return res


# TODO:
#   see all balanced parentheses
#   see balanced parentheses string

'''
def dyck_paths(k: int):  # https://www.geeksforgeeks.org/dyck-path/
    yield


def nth_dyck_path(n: int, k: int) -> list[list[int]]:
    return [[1, 1, 0],
            [0, 1, 1],
            [0, 0, 1]]


def dyck_path_to_string(matrix: list[list[int]]) -> str:
    return '/\\/\\'


def dyck_words(n: int, k: int):  # https://www.geeksforgeeks.org/dyck-words-of-given-length/
    """ :param k: length """
    yield


def nth_dyck_word(n: int, k: int) -> str:
    return 'XY'
'''

if __name__ == '__main__':
    import doctest

    doctest.testmod()
