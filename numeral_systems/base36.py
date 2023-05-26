"""
Base36 - Hexatrigesimal
"""
import string
from collections import deque

__all__ = ['BASE36', 'convert']

BASE36 = string.digits + string.ascii_lowercase


class Base36Exception(Exception):
    pass


def convert(digits: str, /, from_base: int, to_base: int) -> str:
    """
    Convert a number between arbitrary bases

    :param digits: the number to convert
    :param from_base: the base <number> is in
    :param to_base: the base to convert <number> to
    :returns: <number> converted to base <to_base>

    Examples
    --------
    >>> convert('1234', 10, 7)
    '3412'
    >>> convert('1234', 10, 16)
    '4d2'
    >>> convert('4d2', 16, 10)
    '1234'
    >>> convert('1234', 10, 2) == bin(1234)[2:]
    True
    >>> convert('1234', 10, 8) == oct(1234)[2:]
    True
    >>> convert('1234', 10, 16) == hex(1234)[2:]
    True

    Sanity Checks
    -------------
    >>> int('YF', 36)
    1239
    >>> convert('YF.1G90N', 36, 10)
    '1239.0403167384024'

    >>> str(float.fromhex('.ABCDEF')) == convert('.ABCDEF', 16, 10)
    True
    >>> str(float.fromhex('ABC.DEF')) == convert('ABC.DEF', 16, 10)
    True
    """
    if not 2 <=   to_base <= 36: raise Base36Exception(  'to_base must be >= 2 and <= 36')
    if not 2 <= from_base <= 36: raise Base36Exception('from_base must be >= 2 and <= 36')
    # from
    integral, point, fractional = digits.partition('.')
    number = int(integral.lstrip('0') + fractional.rstrip('0') or '0', from_base) * from_base ** -len(fractional)
    # to
    precision = 16 - len(integral) - bool(integral) if point else 0
    number = int(round(number / to_base ** -precision))
    # conversion
    num = abs(number)
    res = deque()
    while num:
        res.appendleft(BASE36[num % to_base])
        num //= to_base
    if number < 0:
        res.appendleft('-')
    res = ''.join(res) or '0'
    # format
    return point.join([res[:-precision] or '0', res[-precision:]]) if point else res


if __name__ == '__main__':
    import doctest

    doctest.testmod()
