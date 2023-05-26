"""
Base62 - Duosexagesimal: https://en.wikipedia.org/wiki/Base62
"""
from string import ascii_lowercase, ascii_uppercase, digits

__all__ = ['b62encode', 'b62decode', 'BASE62', 'Base62Exception', 'is_base62_int', 'is_base62_float']

BASE62 = digits + ascii_lowercase + ascii_uppercase

_ENC = {k: v for k, v in enumerate(BASE62)}  # ~ dict(enumerate())
_DEC = {v: k for k, v in enumerate(BASE62)}


class Base62Exception(Exception):
    pass


def is_base62_int(number: str) -> bool:
    if not isinstance(number, str):
        raise Base62Exception(f'number must be <str> not <{type(number).__name__}>')
    return number.isalnum()


def is_base62_float(number: float or str) -> bool:
    """
    >>> is_base62_float('5C')
    False
    >>> is_base62_float('5.C')
    True
    >>> is_base62_float('5C.')
    True
    >>> is_base62_float('.5C')
    True
    >>> is_base62_float('.5C.')
    False
    >>> is_base62_float('..5C')
    False
    >>> is_base62_float('5C..')
    False
    >>> is_base62_float(' 5.C ')
    False
    >>> is_base62_float(5.5)
    Traceback (most recent call last):
    Base62Exception: number must be <str> not <float>
    """
    if not isinstance(number, str):
        raise Base62Exception(f'number must be <str> not <{type(number).__name__}>')
    number = number.split('.')
    return len(number) == 2 and is_base62_int(''.join(number))


def b62encode(number: int) -> str:
    if not isinstance(number, int):
        raise Base62Exception(f'invalid type: {number=} must be int()')
    if number not in _ENC:
        raise Base62Exception(f'invalid value: {number=} must be >= 0 and < 62')
    return _ENC[number]


def b62decode(digit: str) -> int:
    if not isinstance(digit, str):
        raise Base62Exception(f'invalid type: {digit=} must be str()')
    if digit not in _DEC:
        raise Base62Exception(f'invalid value: {digit=} must be [0-9A-Za-z]')
    return _DEC[digit]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
