"""
Dual Type
"""
from abc import abstractmethod
from numbers import Number, Real

__all__ = ['Dual', 'HyperComplex']


class HyperComplex(Number):  # https://en.wikipedia.org/wiki/Hypercomplex_number
    """
    HyperComplex defines the operations that work on the HyperComplex type.

    In short, those are: +, -, *, /, **, ==, and !=.
    """

    __slots__ = ()

    @abstractmethod
    def __add__(self, other) -> 'HyperComplex':
        """self + other"""

    @abstractmethod
    def __radd__(self, other) -> 'HyperComplex':
        """other + self"""

    @abstractmethod
    def __neg__(self) -> 'HyperComplex':
        """-self"""

    @abstractmethod
    def __pos__(self) -> 'HyperComplex':
        """+self"""

    def __sub__(self, other) -> 'HyperComplex':
        """self - other"""
        return self + -other

    def __rsub__(self, other) -> 'HyperComplex':
        """other - self"""
        return -self + other

    @abstractmethod
    def __mul__(self, other) -> 'HyperComplex':
        """self * other"""

    @abstractmethod
    def __rmul__(self, other) -> 'HyperComplex':
        """other * self"""

    @abstractmethod
    def __truediv__(self, other) -> 'HyperComplex':
        """self / other"""

    @abstractmethod
    def __rtruediv__(self, other) -> 'HyperComplex':
        """other / self"""

    @abstractmethod
    def __pow__(self, exponent) -> 'HyperComplex':
        """self ** exponent"""

    @abstractmethod
    def __rpow__(self, base) -> 'HyperComplex':
        """base ** self"""

    @abstractmethod
    def __eq__(self, other) -> bool:
        """self == other"""


class Dual(HyperComplex):  # https://en.wikipedia.org/wiki/Dual_number
    """
    To HyperComplex, Dual adds the operations that work on dual numbers.

    In short, those are: a conversion to dual, .real, .epsilon.
    """

    __slots__ = ()

    def __bool__(self) -> bool:
        """True if self != 0. Called for bool(self)."""
        return self != 0

    @property
    @abstractmethod
    def real(self) -> Real:
        """Retrieve the real component of this number.

        This should subclass Real.
        """

    @property
    @abstractmethod
    def eps(self) -> Real:
        """Retrieve the nilpotent/epsilon component of this number.

        This should subclass Real.
        """

    @abstractmethod
    def conjugate(self) -> 'Dual':
        """(x+y*e).conjugate() returns (x-y*e)."""
