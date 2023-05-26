"""
Stats Module
"""
from math import comb

__all__ = ['binom']


def binom(n: int, r: int):
    """
    Binomial Probability Formula

    :param n: number of trials
    :param r: number of successes

    >>> from fractions import Fraction

    >>> binom(7, 3)(Fraction(1, 2), Fraction(1, 2))
    Fraction(35, 128)
    >>> binom(5, 1)(Fraction(1, 3), Fraction(2, 3))
    Fraction(80, 243)
    """

    def _binom(p, q):
        """
        :param p: probability of success
        :param q: probability of failure
        :returns: binomial probability B(p, q)
        """
        return comb(n, r) * p ** r * q ** (n - r)

    return _binom


if __name__ == '__main__':
    import doctest

    doctest.testmod()
