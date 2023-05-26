"""
Signum Function
"""

__all__ = ['sign']


def sign(z: int | float | complex, /) -> int:
    """
    # INTEGERS #
    >>> sign(-5)
    -1
    >>> sign(-0)
    0
    >>> sign(0)
    0
    >>> sign(5)
    1

    # FLOATS #
    >>> sign(-5.0)
    -1
    >>> sign(-0.0)
    0
    >>> sign(0.0)
    0
    >>> sign(5.0)
    1

    # COMPLEX #
    >>> sign(+1 + 1j), sign(+1 - 1j), sign(-1 + 1j), sign(-1 - 1j)  # NON-ZERO, NON-ZERO
    (1, 1, -1, -1)
    >>> sign(+1 + 0j), sign(+1 - 0j), sign(-1 + 0j), sign(-1 - 0j)  # NON-ZERO, ZERO
    (1, 1, -1, -1)
    >>> sign(+0 + 1j), sign(+0 - 1j), sign(-0 + 1j), sign(-0 - 1j)  # ZERO, NON-ZERO
    (1, -1, 1, -1)
    >>> sign(+0 + 0j), sign(+0 - 0j), sign(-0 + 0j), sign(-0 - 0j)  # ZERO, ZERO
    (0, 0, 0, 0)

    # EDGE CASES #
    >>> sign('1')
    Traceback (most recent call last):
    TypeError: must be <class 'int'>, <class 'float'> or <class 'complex'>, not <class 'str'>
    >>> sign([])
    Traceback (most recent call last):
    TypeError: must be <class 'int'>, <class 'float'> or <class 'complex'>, not <class 'list'>
    """

    def _sign(x: int) -> int:
        if x < 0: return -1
        if x > 0: return +1
        return 0

    if not isinstance(z, (int, float, complex)):
        raise TypeError(f'must be {int}, {float} or {complex}, not {type(z)}')

    return _sign(z.real) or _sign(z.imag)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
