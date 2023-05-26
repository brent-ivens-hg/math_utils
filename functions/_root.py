"""
Root
"""
from typing import SupportsFloat, SupportsInt

__all__ = ['int_sqrt', 'int_cbrt', 'floor_root', 'ceil_root']


def floor_root(__x: SupportsFloat, __n: SupportsInt) -> int:
    """
    :returns: floored root of x
    """
    x, n = float(__x), int(__n)  # type check

    if n < 0: return floor_root(1 / x, -n)
    if n % 2 and x < 0: return -ceil_root(-x, n)
    if n == 0 or x < 0: raise ValueError('math domain error')

    root = -1
    lo, hi = 0, 1 << (int(x).bit_length() + 2) // n
    while lo <= hi:
        mid = lo + hi >> 1
        y = mid ** n
        if y == x: return mid
        if y < x:
            lo, root = mid + 1, mid
        else:
            hi = mid - 1
    return root


def ceil_root(__x: SupportsFloat, __n: SupportsInt) -> int:
    """
    :returns: ceiled root of x
    """
    x, n = float(__x), int(__n)  # type check

    if n < 0: return ceil_root(1 / x, -n)
    if n % 2 and x < 0: return -floor_root(-x, n)
    if n == 0 or x < 0: raise ValueError('math domain error')

    root = -1
    lo, hi = 0, 1 << (int(x).bit_length() + 2) // n
    while lo <= hi:
        mid = lo + hi >> 1
        y = mid ** n
        if y == x: return mid
        if y < x:
            lo = root = mid + 1
        else:
            hi = mid - 1
    return root


def int_sqrt(__x: SupportsFloat) -> int:
    """ :returns: integer part of square root of x """
    return floor_root(__x, 2)


def int_cbrt(__x: SupportsFloat) -> int:
    """ :returns: integer part of cube root of x """
    return ceil_root(__x, 3) if float(__x) < 0 else floor_root(__x, 3)
