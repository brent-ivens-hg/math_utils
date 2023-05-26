"""
Combinatorics
"""
from collections import Counter
from collections.abc import Iterable
from math import factorial, prod
from typing import TypeVar

_T = TypeVar('_T')


def distinct_permutations(iterable: Iterable[_T]) -> int:
    """
    >>> distinct_permutations('MISSISSIPPI')
    34650
    >>> distinct_permutations('TOOTH')
    30
    """
    cnt = Counter(iterable)
    return factorial(cnt.total()) // prod(map(factorial, cnt.values()))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
