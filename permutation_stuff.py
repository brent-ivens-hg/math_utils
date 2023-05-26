"""
Permutation Stuff
"""
from collections import Counter
from math import factorial, prod


def permutations(string: str) -> int:
    """
    >>> permutations('MISSISSIPPI')
    34650
    >>> permutations('TOOTH')
    30
    """
    multiplicities = Counter(string.upper()).values()
    return factorial(len(string)) // prod(map(factorial, multiplicities))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
