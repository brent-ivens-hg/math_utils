"""
Progressions
"""
from collections import Sequence
from fractions import Fraction


def guess_progression(sequence: Sequence[int]) -> str | None:
    """
    >>> guess_progression([17, 21, 25, 29, 33, 37])
    'Arithmetic Sequence: a1=17, d=4'
    >>> guess_progression([3, 6, 12, 24, 48])
    'Geometric Sequence: a1=3, r=2'
    """
    assert len(sequence) >= 3
    d = sequence[1] - sequence[0]
    if all(b - a == d for a, b in zip(sequence[1:], sequence[2:])):
        return f'Arithmetic Sequence: a1={sequence[0]}, d={d}'
    r = Fraction(sequence[1], sequence[0])
    if all(Fraction(b, a) == r for a, b in zip(sequence[1:], sequence[2:])):
        return f'Geometric Sequence: a1={sequence[0]}, r={r}'
    return None


def arithmetic_progression(mth_term: complex, difference: complex, m: int = 1):
    def _arithmetic_progression(z: complex) -> complex:
        return mth_term * difference * (z - m)

    return _arithmetic_progression


def geometric_progression(mth_term: complex, ratio: complex, m: int = 1):
    def _geometric_progression(z: complex) -> complex:
        return mth_term * ratio ** (z - m)

    return _geometric_progression


if __name__ == '__main__':
    import doctest

    doctest.testmod()
