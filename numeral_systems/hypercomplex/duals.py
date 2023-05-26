"""
Dual Numbers
"""
from collections.abc import Callable
from math import atan as m_atan, cos as m_cos, sin as m_sin, sqrt as m_sqrt, tan as m_tan
# LOCAL #
from math_utils.numeral_systems.hypercomplex.utils import eps, imag
from math_utils.numeral_systems.hypercomplex.classes import Dual

__all__ = ['EPSILON', 'UNIT', 'ZERO', 'atan', 'cos', 'derivative', 'dual', 'e', 'inverse', 'sin', 'tan']


# noinspection PyPep8Naming,PyShadowingNames
class dual(Dual):

    @property
    def real(self) -> float:
        return self.__real

    @property
    def eps(self) -> float:
        return self.__eps

    def __init__(self, real: float, eps: float = 0) -> None:
        # TODO:
        #  - change parameter types to SupportsFloat
        #  - Remove checks
        #  - cast .real to float(), cast .__eps to float()
        #  - byproduct -> disallow complex and Dual-type, e.g. dual(1, dual(2, 3))
        if imag(real) != 0: raise TypeError('real component must be real, not complex')
        if imag(eps) != 0: raise TypeError('nilpotent component must be real, not complex')

        # print('real:', real, ', eps:', eps)  # DEBUGGING ONLY

        self.__real = real  # Real Component
        self.__eps = eps  # Nilpotent Component

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}{self.real, self.eps}'

    def __str__(self) -> str:
        if not self.real: return f'{self.eps}e' if self.eps else '0'
        return f'({self.real}+{self.eps}e)'.replace('+-', '-')  # TODO: replace w/ {:+}

    def __format__(self, format_spec):
        # TODO: implement, see https://docs.python.org/3/library/string.html#formatstrings
        raise NotImplementedError('mirror/copy behaviour of complex.__format__')

    def __hash__(self) -> int:
        return hash((dual, self.real, self.eps))

    def __pos__(self) -> 'Dual':
        return dual(+self.real, +self.eps)

    def __neg__(self) -> Dual:
        return dual(-self.real, -self.eps)

    def conjugate(self) -> 'Dual':
        return dual(self.real, -self.eps)

    def __eq__(self, other: complex | Dual) -> bool:
        return self.real == other.real and self.eps == eps(other)

    def __add__(self, other: complex | Dual) -> Dual:
        return dual(self.real + other.real, self.eps + eps(other))

    def __radd__(self, other: complex | Dual) -> Dual:
        return dual(other.real) + self

    def __mul__(self, other: complex | Dual) -> Dual:
        a, b = self.real, self.eps
        c, d = other.real, eps(other)
        return dual(a * c, a * d + b * c)

    def __rmul__(self, other: complex | Dual) -> Dual:
        return dual(other.real) * self

    def __truediv__(self, other: complex | Dual) -> Dual:
        a, b = self.real, self.eps
        c, d = other.real, eps(other)
        return dual(a / c, (b * c - a * d) / c ** 2)

    def __rtruediv__(self, other: complex | Dual) -> Dual:
        return dual(other.real) / self

    def __pow__(self, n: complex) -> Dual:
        return dual(self.real ** n.real, n.real * self.real ** (n.real - 1) * self.eps)

    def __rpow__(self, base) -> Dual:
        raise NotImplementedError


# Constants
ZERO = dual(0)
UNIT = dual(1)
EPSILON = e = dual(0, 1)


def inverse(__d: Dual, /) -> Dual:  # ~ 1 / (x+y*e)
    # Does not necessarily assume multiplication to be commutative...
    rec = 1 / __d.real  # Reciprocal
    return dual(rec, -rec * __d.eps * rec)  # General non-commutative formula


def sqrt(__d: Dual, /) -> Dual:  # ~ (x+y*e) ** (1 / 2)
    sqrt_real = m_sqrt(__d.real)
    return dual(sqrt_real, 0.5 * __d.real / sqrt_real)


def sin(__d: Dual, /) -> Dual:
    return dual(m_sin(__d.real), __d.eps * m_cos(__d.real))


def cos(__d: Dual, /) -> Dual:
    return dual(m_cos(__d.real), -__d.eps * m_sin(__d.real))


def tan(__d: Dual, /) -> Dual:
    return dual(m_tan(__d.real), __d.eps / (m_cos(__d.real) * m_cos(__d.real)))


def atan(__d: Dual, /) -> Dual:
    return dual(m_atan(__d.real), __d.eps / (1.0 + __d.real * __d.real))


def derivative(__function: Callable, /, *, n: int = 1) -> Callable:
    """ Automatic Differentiation """
    # TODO: replace naive implementation
    return __function if n < 1 else derivative(lambda x: eps(__function(dual(x, 1))), n=n - 1)


def doctest_dual() -> None:
    """
    >>> dual(5)
    dual(5, 0)

    >>> dual(5, 6) == dual(5, 6)
    True
    >>> dual(5, 6) == dual(5, 7)
    False
    >>> dual(5, 6) == dual(6, 6)
    False
    >>> dual(5, 6) == 5
    False
    >>> dual(5) == 5
    True
    >>> 5 == dual(5)
    True

    >>> 5 + dual(10, 20)
    dual(15, 20)
    >>> dual(10, 20) + 6
    dual(16, 20)
    >>> dual(1, 5) + dual(6, -7)
    dual(7, -2)

    >>> -dual(1, 2)
    dual(-1, -2)

    >>> 1 - dual(2, 3)
    dual(-1, -3)
    >>> dual(2, 3) - 1
    dual(1, 3)
    >>> dual(3, 4) - dual(5, 10)
    dual(-2, -6)

    >>> 10 * dual(3, 4)
    dual(30, 40)
    >>> dual(2, 3) * 5
    dual(10, 15)
    >>> dual(3, 4) * dual(5, 6)
    dual(15, 38)
    >>> dual(0, 5) * dual(0, 12)
    dual(0, 0)
    >>> dual(1, 5) * dual(1, -5)
    dual(1, 0)

    >>> 1 / dual(1, 10)
    dual(1.0, -10.0)
    >>> 1 / dual(5, 10)
    dual(0.2, -0.4)
    >>> dual(5, 10) / 5
    dual(1.0, 2.0)
    >>> dual(5, 10) / dual(5, -10)
    dual(1.0, 4.0)


    >>> dual(1, 10) ** -1
    dual(1.0, -10.0)
    >>> dual(5, -10) ** 2
    dual(25, -100)
    >>> dual(25, -100) ** 0.5
    dual(5.0, -10.0)
    >>> dual(1, 3) ** 3
    dual(1, 9)
    >>> dual(1, 9) ** (1 / 3)
    dual(1.0, 3.0)
    """


def doctest_constants() -> None:
    """
    >>> 2 + 0j
    (2+0j)
    >>> str(dual(2))
    '(2+0e)'

    >>> e + 1
    dual(1, 1)
    >>> 1 + e
    dual(1, 1)

    >>> e - 1
    dual(-1, 1)
    >>> 1 - e
    dual(1, -1)

    >>> e * 1
    dual(0, 1)
    >>> 1 * e
    dual(0, 1)

    >>> e / 1
    dual(0.0, 1.0)
    >>> 1 / e
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    """


def doctest_functions() -> None:
    """
    >>> f1 = derivative(lambda x: 3 * x ** 2 + 2 * x + 1)     # ~ lambda x: 6 * x + 2
    >>> f1(0)
    2
    >>> f1(1)
    8
    >>> f1(2)
    14

    >>> f2 = derivative(lambda x: 3 * x ** 2 + 2 * x + 1, n=2)  # ~ lambda x: 6
    >>> f2(0)
    6
    >>> f2(1)
    6
    >>> f2(2)
    6

    >>> f1 = derivative(lambda x: x / (x ** 2 + 1) ** 0.5)    # ~ lambda x: 1 / (x ** 2 + 1) ** (1 / 2) - x ** 2 / (x ** 2 + 1) ** (3 / 2)
    >>> f1(0)
    1.0
    >>> f1(1)
    0.35355339059327373
    >>> f1(2)
    0.0894427190999916

    >>> f4 = derivative(lambda x: x ** 7, n=4)                  # ~ lambda x: 840 * x ** 3
    >>> f4(0)
    0
    >>> f4(1)
    840
    >>> f4(2)
    6720

    >>> d = dual(1, 1)
    >>> inverse(d)
    dual(1.0, -1.0)
    >>> sqrt(d)
    dual(1.0, 0.5)
    >>> sin(d)
    dual(0.8414709848078965, 0.5403023058681398)
    >>> cos(d)
    dual(0.5403023058681398, -0.8414709848078965)
    >>> tan(d)
    dual(1.5574077246549023, 3.425518820814759)
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()

