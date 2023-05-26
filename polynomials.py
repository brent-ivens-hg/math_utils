"""
Polynomial stuff
"""
from __future__ import annotations

from dataclasses import astuple, dataclass
from math import hypot, sqrt
from functools import cached_property

EPSILON = 1e-12


# TODO: x1 = x0 - f(x0)/f'(x0) # Newton-Raphson-Method # for cubic roots e.g. x^3-x-1=0 ~ 1.32471

def gradient(p, q) -> float:
    """
    :returns: the slope of (p, q)
    """
    (px, py), (qx, qy) = p, q
    return (py - qy) / (px - qx)


def dist(a: Point | Linear, b: Point | Linear) -> float:  # Todo
    if isinstance(a, Point):
        if isinstance(b, Point):
            return hypot(a.x - b.x, a.y - b.y)
        if isinstance(b, Linear):
            raise NotImplementedError  # abs(b.a * a.x + b.b * a.y + b.c) / hypot(b.a, b.b)
        if isinstance(b, Quadratic):
            raise NotImplementedError
        if isinstance(b, Cubic):
            raise NotImplementedError
        if isinstance(b, Quartic):
            raise NotImplementedError

    if isinstance(a, Linear):
        if isinstance(b, Point):
            raise NotImplementedError  # abs(a.a * b.x + a.b * b.y + a.c) / hypot(a.a, a.b)
        if isinstance(b, Linear):
            if a.a == b.a:  # parallel
                return abs(a.b - b.b) / hypot(a.a, 1)
            return 0.0  # intersecting

    raise PolynomialException('not implemented')


class PolynomialException(Exception):
    pass


@dataclass(frozen=True, slots=True)
class Point:
    x: float
    y: float

    def __getitem__(self, item: int) -> float:
        return astuple(self)[item]


@dataclass(frozen=True, slots=True)
class Hline:
    y: float


@dataclass(frozen=True, slots=True)
class Vline:
    x: float


# noinspection SpellCheckingInspection
class Linear:
    """
    y = ax + b
    """

    def __init__(self, a: int | float, b: int | float = 0) -> None:
        if a == 0:
            raise PolynomialException('a != 0')

        self.a = float(a)
        self.b = float(b)

    def __and__(self, other: Linear) -> Point | Linear | None:
        return self.intersect(other)

    def __contains__(self, point: Point) -> bool:
        return abs(self.a * point.x + self.b - point.y) <= EPSILON

    def root(self) -> Point | None:
        """
        :returns: the x-axis intersection
        """
        return Point(-self.b / self.a, 0)

    def intercept(self) -> Point | None:
        """
        :returns: the y-axis intersection
        """
        if self.a == float('inf'):
            return None
        return Point(0, self.b)

    def intersect(self, other: Linear) -> Point | Linear | None:  # Fixme
        """
        denom = self.b * other.a - self.a * other.b
        if denom == 0:  # equal slopes
            if self.intercept() != other.intercept():
                return None  # identical or parallel
            return Linear(self.a, self.b)
        x = (self.c * other.b - self.b * other.c) / denom
        y = self(x) if self.intercept() is not None else other(x)
        return Point(x, y)
        """

    def __eq__(self, other) -> bool:
        return isinstance(other, Linear) and self.a == other.a and self.b == other.b

    def __call__(self, x: float | None = None, y: float | None = None) -> float:
        """
        :returns: x-value if y-value or y-value if given x-value
        """
        if x is not None and y is None:
            return self.a * x + self.b
        if y is not None and x is None:
            return (y - self.b) / self.a
        raise PolynomialException(f'invalid argument: use x=... or y=...')

    def perpendicular(self, p: Point):
        """
        :returns: perpendicular Linear through point a
        """
        a = -1 / self.a
        b = p.y - a * p.x
        return Linear(a, b)

    @classmethod
    def from_universal_form(cls, a: float, b: float, c: float) -> Linear:
        """
        :returns: Ax + By + C => y = ax + b
        """
        if b == 0:
            raise PolynomialException('b != 0')
        return Linear(-a / b, -c / b)

    @classmethod
    def from_point_slope_form(cls, point: Point, slope: float) -> Linear:
        """
        :returns: y - y1 = m(x - x1) <=> y = mx + (-mx1 - y1)
        """
        return Linear(slope, -slope * point.x - point.y)

    @classmethod
    def from_points(cls, p: Point, q: Point) -> Linear:
        """
        :returns: Linear going through point a and b
        """
        if p.x == q.x:
            raise PolynomialException('a == inf')
        return Linear.from_point_slope_form(p, gradient(p, q))


class Quadratic:
    """
    Univariate Function: f(x) = ax^2 + bx + c
    >>> parabola = Quadratic(3, 24, 48)
    >>> parabola
    Quadratic(3.0, 24.0, 48.0)
    >>> str(parabola)
    '3.0x^2 + 24.0x + 48.0'
    >>> parabola.discriminant
    0.0
    >>> parabola.roots
    -4.0
    >>> parabola.is_root(-4.0)
    True
    >>> parabola.vertex
    (-4.0, 0.0)
    >>> parabola.focus
    (-4.0, 0.08333333333333333)
    >>> parabola.directrix
    -6876.0
    """

    def __init__(self, a: int | float, b: int | float = 0, c: int | float = 0) -> None:
        if a == 0:
            raise PolynomialException('a != 0')

        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}{self.a, self.b, self.c}'

    def __str__(self) -> str:
        res = [f'{self.a}x^2']
        if self.b: res += [('-' if self.b < 0 else '+'), f'{self.b}x']
        if self.c: res += [('-' if self.c < 0 else '+'), f'{self.c}']
        return ' '.join(res)

    @cached_property
    def beta(self) -> float:
        return -self.b / (2 * self.a)

    @cached_property
    def discriminant(self) -> float:
        return self.b ** 2 - 4 * self.a * self.c

    # noinspection PyRedundantParentheses
    @cached_property
    def roots(self) -> tuple:
        if self.discriminant < 0: return ()
        if self.discriminant == 0: return (self.beta,)
        delta = sqrt(self.discriminant)
        return -(self.b - delta) / (2 * self.a), -(self.b + delta) / (2 * self.a)

    @cached_property
    def vertex(self) -> tuple:
        return self.beta, self.c - self.b ** 2 / (4 * self.a)

    @cached_property
    def focus(self) -> tuple:
        x, y = self.vertex
        return x, y + 1 / (4 * self.a)

    @cached_property
    def directrix(self) -> float:
        return self.c - (self.b ** 2 + 1) * 4 * self.a

    def is_root(self, root: float) -> bool:
        return abs(self.a * root ** 2 + self.b * root + self.c) <= EPSILON

    def derivative(self):
        return

    @classmethod
    def from_factor_form(cls, r1: float, r2: float, a: float = 1) -> Quadratic:
        """
        y = a * (x - r1) * (x - r2)
        """
        b = -a * (r1 + r2)
        c = a * r1 * r2
        return cls(a, b, c)

    @classmethod
    def from_vertex_form(cls, p: Point, a: float = 1) -> Quadratic:
        """
        y = a * (x - x1) ^ 2 + y1
        """
        b = -2 * a * p.x
        c = a * p.x ** 2 + p.y
        return cls(a, b, c)

    @classmethod
    def from_points(cls, p: Point, q: Point, r: Point) -> Quadratic:
        denom = (p.x - q.x) * (p.x - r.x) * (q.x - r.x)
        a = (p.x * (r.y - q.y) + q.x * (p.y - r.y) + r.x * (q.y - p.y)) / denom
        b = (p.x ** 2 * (q.y - r.y) + q.x ** 2 * (r.y - p.y) + r.x ** 2 * (p.y - q.y)) / denom
        c = (q.x * r.x * (q.x - r.x) * p.y + r.x * p.x * (r.x - p.x) * q.y + p.x * q.x * (p.x - q.x) * r.y) / denom
        return cls(a, b, c)


class Cubic:
    pass


class Quartic:
    pass


if __name__ == '__main__':
    import doctest

    doctest.testmod()
