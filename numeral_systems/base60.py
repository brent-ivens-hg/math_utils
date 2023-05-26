"""
Base60: Sexagesimal
"""
from math import modf

__all__ = ['decimal_to_dms', 'dms_to_decimal']


def decimal_to_dms(number: float) -> tuple[int, int, float]:
    """
    Converts number from decimal to degrees, minutes, seconds

    >>> decimal_to_dms(30.263888889)
    (30, 15, 50.0)
    >>> decimal_to_dms(18.3333333333333)
    (18, 20, 0.0)
    """
    number, h = modf(number)
    number, m = modf(number * 60)
    s = round(number * 60, 2)
    if s == 60: s = 0; m += 1
    if m == 60: m = 0; h += 1
    return int(h), int(m), s


def dms_to_decimal(degrees: int, minutes: int, seconds: float) -> float:
    """
    Converts number from degrees, minutes, seconds to decimal

    >>> dms_to_decimal(30, 15, 50.0)
    30.26388888888889
    >>> dms_to_decimal(18, 20, 0)
    18.333333333333332
    """
    return degrees + minutes / 60 + seconds / 3600


def decimal_to_hms(number: float) -> tuple[int, int, float]:
    """
    Converts number from decimal to hours, minutes, seconds

    >>> decimal_to_hms(30.263888889)
    (30, 15, 50.0)
    >>> decimal_to_hms(18.3333333333333)
    (18, 20, 0.0)
    """
    return decimal_to_dms(number)


def hms_to_decimal(hours: int, minutes: int, seconds: float) -> float:
    """
    Converts number from hours, minutes, seconds to decimal

    >>> hms_to_decimal(30, 15, 50.0)
    30.26388888888889
    >>> hms_to_decimal(18, 20, 0)
    18.333333333333332
    """
    return dms_to_decimal(hours, minutes, seconds)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
