"""
Infinite series
"""
from math import *


# CONVERGING SERIES

def p_series(p: int, s: int = 0, n: int = 1):
    """ converges if p > 1 """
    assert p > 1
    yield s
    yield from p_series(p, s + 1 / n ** p, n + 1)


def zenos_paradox(s: int = 0, n: int = 0):  # based of geometric series?
    """ converges to 2 """
    yield s
    yield from zenos_paradox(s + 1 / 2 ** n, n + 1)


def basel(s: int = 0, n: int = 1):  # p_series with p = 2
    """ converges to pi^2 / 6 """
    yield s
    yield from basel(s + 1 / n ** 2, n + 1)


# Basic Maclaurin Expansions #

def exp(x: int, s: int = 1, n: int = 0):  # exponential function
    """ converges to e^x """
    yield s
    yield from exp(x, s + x ** n / factorial(n), n + 1)


def sin(x: int, s: int = 0, n: int = 0):  # sine function
    """ converges to sin(x) """
    yield s
    yield from sin(x, s + ((-1) ** n * x ** (2 * n + 1)) / factorial(2 * n + 1), n + 1)


def cos(x: int, s: int = 0, n: int = 0):  # cosine function
    """ converges to cos(x) """
    yield s
    yield from cos(x, s + ((-1) ** n * x ** (2 * n)) / factorial(2 * n), n + 1)


# DIVERGING SERIES #

def harmonic(s: float = 0, n=1):
    """ diverges """
    yield s
    yield from harmonic(s + 1 / n, n + 1)


def fibonacci(a=0, b=1):
    """ diverges """
    yield a
    yield from fibonacci(b, a + b)

# def factorial(a: int = 1, b: int = 1) -> int:
#     """ diverges """
#     yield b
#     yield from factorial(a + 1, a * b)
