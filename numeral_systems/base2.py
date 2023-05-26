"""
Base2 - Binary
"""


class BinaryFloatException(Exception):
    pass


class BinaryFloat:
    """ Binary float value """

    def __init__(self, binary_string: str) -> None:
        if not set(binary_string) <= set('.01'):
            raise BinaryFloatException(f'invalid {binary_string=}')

        match binary_string.split('.'):
            case [integer] | [integer, '']:
                self._int, self._frac = integer, '0'
            case ['', fraction]:
                self._int, self._frac = '0', fraction
            case [integer, fraction]:
                self._int, self._frac = integer, fraction
            case _:
                raise BinaryFloatException(f'invalid {binary_string=}')

        self._bin_string = f'{self._int}.{self._frac}'

    @property
    def integer(self) -> str:
        """ :returns: the integer part of the binary string """
        return self._int

    @property
    def fractional(self) -> str:
        """ :returns: the fractional part of the binary string """
        return self._frac

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._bin_string!r})'

    def __str__(self) -> str:
        return self._bin_string

    def _fractional(self) -> float:
        """ Computes the fractional part of the binary float """
        return sum(int(b) * 2 ** -i for i, b in enumerate(self._frac, 1))

    def __float__(self) -> float:
        return int(self) + self._fractional()

    def __trunc__(self) -> int:
        return int(self._int, 2)


def doctests() -> None:
    """
    >>> bin_float = BinaryFloat('11010.01')
    >>> bin_float
    BinaryFloat('11010.01')
    >>> str(bin_float)
    '11010.01'
    >>> bin_float.integer
    '11010'
    >>> bin_float.fractional
    '01'
    >>> float(bin_float)
    26.25
    >>> int(bin_float)
    26
    >>> bin_float = BinaryFloat('11010')
    >>> bin_float
    BinaryFloat('11010.0')
    >>> bin_float.integer
    '11010'
    >>> bin_float.fractional
    '0'
    >>> float(bin_float)
    26.0
    >>> int(bin_float)
    26
    >>> BinaryFloat('1')
    BinaryFloat('1.0')
    >>> BinaryFloat('1.')
    BinaryFloat('1.0')
    >>> BinaryFloat('.1')
    BinaryFloat('0.1')
    >>> BinaryFloat('0.1')
    BinaryFloat('0.1')
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()
