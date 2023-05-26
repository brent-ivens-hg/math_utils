"""
Utils
"""
from collections import namedtuple
from typing import TypeVar

__all__ = ['eps', 'imag', 'real', 'promote']

hypercomplex = TypeVar('hypercomplex')


def eps(__x: hypercomplex, /) -> int | float:
    """ :returns: the epsilon/nilpotent component (.eps) """
    return getattr(__x, 'eps', 0)


def imag(__x: hypercomplex, /) -> int | float:
    """ :returns: the imaginary component (.imag) """
    return getattr(__x, 'imag', 0)


def real(__x: hypercomplex, /) -> int | float:
    """ :returns: the real component (.real) """
    return getattr(__x, 'real', 0)


def promote(x: hypercomplex, /) -> hypercomplex:
    """
    >>> promote(1+0j)
    1.0
    >>> dual = namedtuple('dual', 'real eps')
    >>> promote(dual(1, 0))
    1
    """
    return x.real if imag(x) == eps(x) == 0 else x


if __name__ == '__main__':
    import doctest

    doctest.testmod()
