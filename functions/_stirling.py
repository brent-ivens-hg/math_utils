"""
Stirling
"""
from functools import cache
from math import factorial

__all__ = ['s1', 's1_triangle', 's2', 's2_triangle']


@cache
def s1(n: int, k: int) -> int:
    """Stirling Numbers of the First Kind"""
    # https://en.wikipedia.org/wiki/Stirling_numbers_of_the_first_kind#Recurrence_relation
    if n < 0: raise ValueError('n must >= 0')
    if n == k == 0: return 1
    if n == 0 or k <= 0 or n < k: return 0
    return (n - 1) * s1(n - 1, k) + s1(n - 1, k - 1)


# noinspection PyUnusedLocal
def s_1st_diagonal(n: int) -> int:  # A000012: All 1's Sequence
    """Stirling Numbers: s(n, n)"""
    return 1


def s_2nd_diagonal(n: int) -> int:  # A000914: Triangular Numbers
    """Stirling Numbers: s(n+1, n)"""
    return n * (n + 1) // 2


def s1_3rd_diagonal(n: int) -> int:  # A000914
    """Stirling Numbers of the First Kind: s1(n+2, n)"""
    return n * (n + 1) * (n + 2) * (3 * n + 5) // 24


def s1_4th_diagonal(n: int) -> int:  # A000914
    """Stirling Numbers of the First Kind: s1(n+3, n)"""
    return n * (n + 1) * (n + 2) ** 2 * (n + 3) ** 2 // 48


def s1_5th_diagonal(n: int) -> int:  # A000915
    """Stirling Numbers of the First Kind: s1(n+4, n)"""
    return n * (n + 1) * (n + 2) * (n + 3) * (n + 4) * (15 * n ** 3 + 150 * n ** 2 + 485 * n + 502) // 5760


# noinspection PyUnusedLocal
def s1_6th_diagonal(n: int) -> int:  # A053567
    """Stirling Numbers of the First Kind: s1(n+5, n)"""
    raise NotImplementedError


# noinspection PyUnusedLocal
def s1_7th_diagonal(n: int) -> int:  # A112002
    """Stirling Numbers of the First Kind: s1(n+6, n)"""
    raise NotImplementedError


# noinspection PyUnusedLocal
def s1_8th_diagonal(n: int) -> int:  # A191685
    """Stirling Numbers of the First Kind: s1(n+7, n)"""
    raise NotImplementedError


def s_1st_column(n: int) -> int:  # A000007: The characteristic function of {0}: a(n) = 0^n.
    """Stirling Numbers of the First Kind: s1(n, 0)"""
    return 1 if n == 0 else 0


def s1_2nd_column(n: int) -> int:  # A000142: Factorial numbers
    """Stirling Numbers of the First Kind: s1(n+1, 1)"""
    return factorial(n)


def s1_3rd_column(n: int) -> int:  # A000254
    """Stirling Numbers of the First Kind: s1(n+2, 2)"""
    # return n * s1_3rd_column(n - 1) + factorial(n - 1) if n > 0 else 0  # starts with 0
    return (n + 1) * s1_3rd_column(n - 1) + factorial(n) if n > 0 else 1  # starts with 1


# noinspection PyUnusedLocal,DuplicatedCode
def s1_4th_column(n: int) -> int:  # A000254
    """Stirling Numbers of the First Kind: s1(n+3, 3)"""
    raise NotImplementedError


# noinspection PyUnusedLocal
def s1_5th_column(n: int) -> int:  # A000454
    """Stirling Numbers of the First Kind: s1(n+4, 4)"""
    raise NotImplementedError


# noinspection PyUnusedLocal
def s1_6th_column(n: int) -> int:  # A000482
    """Stirling Numbers of the First Kind: s1(n+5, 5)"""
    raise NotImplementedError


# noinspection PyUnusedLocal
def s1_7th_column(n: int) -> int:  # A001233
    """Stirling Numbers of the First Kind: s1(n+6, 6)"""
    raise NotImplementedError


# noinspection PyUnusedLocal
def s1_8th_column(n: int) -> int:  # A001234
    """Stirling Numbers of the First Kind: s1(n+7, 7)"""
    raise NotImplementedError


# noinspection PyUnusedLocal
def s1_9th_column(n: int) -> int:  # A243569
    """Stirling Numbers of the First Kind: s1(n+8, 8)"""
    raise NotImplementedError


# noinspection PyUnusedLocal
def s1_10th_column(n: int) -> int:  # A243570
    """Stirling Numbers of the First Kind: s1(n+9, 9)"""
    raise NotImplementedError


# noinspection PyUnresolvedReferences
def s1_triangle(n: int, *, signed: bool = False) -> list[list[int]]:  # A132393: Triangle of Unsigned Stirling Numbers
    # of the First Kind
    # https://en.wikipedia.org/wiki/Stirling_numbers_of_the_first_kind#Table_of_values
    """
    the first 10 rows of the triangle:

    >>> for idx, t_row in enumerate(s1_triangle(10)):
    ...     print('{:>2}.  {}'.format(idx, ' '.join(map('{:<8}'.format, t_row)).rstrip()))
     0.  1
     1.  0        1
     2.  0        1        1
     3.  0        2        3        1
     4.  0        6        11       6        1
     5.  0        24       50       35       10       1
     6.  0        120      274      225      85       15       1
     7.  0        720      1764     1624     735      175      21       1
     8.  0        5040     13068    13132    6769     1960     322      28       1
     9.  0        40320    109584   118124   67284    22449    4536     546      36       1
    10.  0        362880   1026576  1172700  723680   269325   63273    9450     870      45       1

    >>> for idx, t_row in enumerate(s1_triangle(10, signed=True)):
    ...     print('{:>2}.  {}'.format(idx, ' '.join(f'{i:+d}'.ljust(8) for i in t_row).rstrip()))
     0.  +1
     1.  +0       +1
     2.  +0       -1       +1
     3.  +0       +2       -3       +1
     4.  +0       -6       +11      -6       +1
     5.  +0       +24      -50      +35      -10      +1
     6.  +0       -120     +274     -225     +85      -15      +1
     7.  +0       +720     -1764    +1624    -735     +175     -21      +1
     8.  +0       -5040    +13068   -13132   +6769    -1960    +322     -28      +1
     9.  +0       +40320   -109584  +118124  -67284   +22449   -4536    +546     -36      +1
    10.  +0       -362880  +1026576 -1172700 +723680  -269325  +63273   -9450    +870     -45      +1
    """
    sign = -1 if signed else 1
    rows = n
    res = [[1]]
    for n in range(rows):
        row = res[-1] + [0]
        res.append([sign * n * s + row[k - 1] for k, s in enumerate(row)])
    return res


@cache
def s2(n: int, k: int) -> int:
    """Stirling Number of the Second Kind"""
    # https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind#Recurrence_relation
    if n < 0: raise ValueError('n must be a non-negative integer')
    if n == k == 0: return 1
    if n == 0 or k <= 0 or n < k: return 0
    return k * s2(n - 1, k) + s2(n - 1, k - 1)


def s2_3rd_diagonal(n: int) -> int:  # A001296: 4-dimensional pyramidal numbers
    """Stirling Numbers of the Second Kind: s2(n+2, n)"""
    return n * (n + 1) * (n + 2) * (3 * n + 1) // 24


def s2_4th_diagonal(n: int) -> int:  # A001297
    """Stirling Numbers of the Second Kind: s2(n+3, n)"""
    return (n + 1) ** 2 * (n + 2) * (n + 3) * n ** 2 // 48


def s2_5th_diagonal(n: int) -> int:  # A001298
    """Stirling Numbers of the Second Kind: s2(n+4, n)"""
    return n * (n + 1) * (n + 2) * (n + 3) * (n + 4) * (15 * n ** 3 + 30 * n ** 2 + 5 * n - 2) // 5760


# noinspection PyUnusedLocal
def s2_6th_diagonal(n: int) -> int:  # A112494
    """Stirling Numbers of the Second Kind: s2(n+5, n)"""
    raise NotImplementedError


# noinspection PyUnusedLocal
def s2_7th_diagonal(n: int) -> int:  # A144969
    """Stirling Numbers of the Second Kind: s2(n+6, n)"""
    raise NotImplementedError


# noinspection PyUnusedLocal
def s2_2nd_column(n: int) -> int:  # A000012: All 1's Sequence
    """Stirling Numbers of the Second Kind: s2(n+1, 1)"""
    return 1


def s2_3rd_column(n: int) -> int:  # A000225: Mersenne Numbers
    """Stirling Numbers of the Second Kind: s2(n+2, 2)"""
    return 2 ** n - 1


# noinspection PyUnusedLocal,DuplicatedCode
def s2_4th_column(n: int) -> int:  # A000392
    """Stirling Numbers of the Second Kind: s2(n+3, 3)"""
    raise NotImplementedError


# noinspection PyUnusedLocal
def s2_5th_column(n: int) -> int:  # A000453
    """Stirling Numbers of the Second Kind: s2(n+4, 4)"""
    raise NotImplementedError


# noinspection PyUnusedLocal
def s2_6th_column(n: int) -> int:  # A000481
    """Stirling Numbers of the Second Kind: s2(n+5, 5)"""
    raise NotImplementedError


# noinspection PyUnusedLocal
def s2_7th_column(n: int) -> int:  # A000770
    """Stirling Numbers of the Second Kind: s2(n+6, 6)"""
    raise NotImplementedError


# noinspection PyUnusedLocal
def s2_8th_column(n: int) -> int:  # A000771
    """Stirling Numbers of the Second Kind: s2(n+7, 7)"""
    raise NotImplementedError


# noinspection PyUnusedLocal
def s2_9th_column(n: int) -> int:  # A049434
    """Stirling Numbers of the Second Kind: s2(n+8, 8)"""
    raise NotImplementedError


# noinspection PyUnusedLocal
def s2_10th_column(n: int) -> int:  # A049447
    """Stirling Numbers of the Second Kind: s2(n+9, 9)"""
    raise NotImplementedError


# noinspection PyUnusedLocal
def s2_11th_column(n: int) -> int:  # A049435
    """Stirling Numbers of the Second Kind: s2(n+10, 10)"""
    raise NotImplementedError


def s2_triangle(n: int) -> list[list[int]]:  # A008277: Triangle of Stirling Numbers of the Second Kind
    # https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind#Table_of_values
    """
    the first 10 rows of the triangle:

    >>> for idx, t_row in enumerate(s2_triangle(10)):
    ...     print('{:>2}.  {}'.format(idx, ' '.join(map('{:<5}'.format, t_row)).rstrip()))
     0.  1
     1.  0     1
     2.  0     1     1
     3.  0     1     3     1
     4.  0     1     7     6     1
     5.  0     1     15    25    10    1
     6.  0     1     31    90    65    15    1
     7.  0     1     63    301   350   140   21    1
     8.  0     1     127   966   1701  1050  266   28    1
     9.  0     1     255   3025  7770  6951  2646  462   36    1
    10.  0     1     511   9330  34105 42525 22827 5880  750   45    1
    """
    rows = n
    res = [[1]]
    for n in range(rows):
        row = res[-1] + [0]
        res.append([k * s + row[k - 1] for k, s in enumerate(row)])
    return res


# More Sterling Sequences
# -----------------------
# A187646: s1(2n, n) - Central Stirling Numbers of the First Kind
# A237993: s1(3n, n)
# A242676: s1(4n, n)

# A007820: s2(2n,  n)
# A217913: s2(3n,  n)
# A217914: s2(4n,  n)
# A217915: s2(5n,  n)
# A222526: s2(6n,  n)
# A222527: s2(7n,  n)
# A222528: s2(8n,  n)
# A222529: s2(9n,  n)
# A222530: s2(10n, n)

# A218141: s2(n^2, n)
# A218142: s2(n^2+n, n)
# A218143: s2(n(n+1)/2, n)

if __name__ == '__main__':
    import doctest

    doctest.testmod()
