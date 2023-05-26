"""
approximations.py
"""
from collections.abc import Callable
from decimal import Context, Decimal, getcontext, localcontext, ROUND_HALF_UP


def approximate(func: Callable) -> Decimal:
    """
    Calculates fixed point of function with context precision
    """
    epsilon = Decimal(f'1e{-getcontext().prec}')
    getcontext().prec += 2
    approx = Decimal(1)
    prev = 0
    while abs(approx - prev) >= epsilon:
        prev, approx = approx, func(approx)
    getcontext().prec -= 2
    return +approx


def nth_root(n: int, x: int, ndigits: int, rounding: str = ROUND_HALF_UP) -> Decimal:
    """
    :returns: nth root of x (up to n digits)

    >>> nth_root(2, 17, ndigits=10)
    Decimal(4.123105626)
    """
    with localcontext(Context(prec=ndigits, rounding=rounding)):
        k = n - 1
        return approximate(lambda xn: (k * xn + x / xn ** k) / n)


def nth_log(n: int, x: int, ndigits: int, rounding: str = ROUND_HALF_UP) -> Decimal:
    """
    :returns: nth log of x (up to n digits)
    """
    with localcontext(Context(prec=ndigits, rounding=rounding)):
        pass


def phi(ndigits: int, rounding: str = ROUND_HALF_UP) -> Decimal:
    """
    >>> 'approximation: %s' % phi(ndigits=10)
    'iterations: 24, approximation: 1.618033989'
    """
    with localcontext(Context(prec=ndigits, rounding=rounding)):
        return approximate(lambda x: 1 + 1 / x)


def dottie(ndigits: int, rounding: str = ROUND_HALF_UP) -> Decimal:
    """
    # https://en.wikipedia.org/wiki/Dottie_number

    >>> 'approximation: %s' % dottie(ndigits=10)
    'iterations: 57, approximation: 0.7390851332'
    """
    with localcontext(Context(prec=ndigits, rounding=rounding)):
        def _cos(x):
            """
            # https://docs.python.org/3/library/decimal.html#decimal-recipes
            """
            getcontext().prec += 2
            i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
            while s != lasts:
                lasts = s
                i += 2
                fact *= i * (i - 1)
                num *= x * x
                sign *= -1
                s += num / fact * sign
            getcontext().prec -= 2
            return +s

        return approximate(_cos)


class NearZeroApproximators:  # Grouping Class
    """
    if x ~ 0

    # https://www.mit.edu/~hlb/StantonGrant/Lecture9/quadratic.pdf

    """

    @staticmethod
    def sin(x):
        """ sin(x) """
        return x

    @staticmethod
    def cos(x):
        """ cos(x) """
        return 1 - x ** 2 / 2

    @staticmethod
    def exp(x):
        """ e^x """
        return 1 + x + x ** 2 / 2

    @staticmethod
    def ln1x(x):
        """ ln(1+x) """
        return x - x ** 2 / 2

    @staticmethod
    def pow1x(x, n):
        """ (1+x)^n """
        return 1 + n * x + n * (n - 1) / 2


if __name__ == '__main__':
    import doctest

    doctest.testmod()
