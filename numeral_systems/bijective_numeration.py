"""
Bijective Numeration: https://en.wikipedia.org/wiki/Bijective_numeration
"""
from collections import deque
from collections.abc import Generator
from dataclasses import dataclass

__all__ = [
    'BijectiveBase2', 'BijectiveBase3', 'BijectiveBase8', 'BijectiveBase10', 'BijectiveBase12', 'BijectiveBase16',
    'BijectiveBase26',
    'BijectiveNumerationTypeException', 'BijectiveNumerationValueException', 'BijectiveNumerationBaseException',
    'bijective_numeration',
]


class BijectiveNumerationBaseException(Exception):  # Error
    pass


class BijectiveNumerationTypeException(BijectiveNumerationBaseException):  # Type Error
    pass


class BijectiveNumerationValueException(BijectiveNumerationBaseException):  # Value Error
    pass


# Create Aliases
TypeException = BijectiveNumerationTypeException
ValueException = BijectiveNumerationValueException


@dataclass(frozen=True, slots=True)
class BijectiveNumeration:
    alphabet: str
    base: int
    table: dict[str, int]

    def to_int(self, numerals: str) -> int:
        """
        :returns: integer in base-10
        """
        if not isinstance(numerals, str):
            raise TypeException(
                f'BijectiveNumeration.to_int() argument must be string, not {type(numerals).__name__!r}')
        try:
            res = 0
            for num in numerals:
                res *= self.base
                res += self.table[num]
            return res
        except KeyError as err:
            raise ValueException(f'numeral {err} not found in alphabet: {self.alphabet!r}') from None

    def to_bijective(self, integer: int) -> str:
        """
        :returns: number in bijective base-k numerals
        """
        if type(integer) != int:
            raise TypeException(
                f'BijectiveNumeration.to_bijective() argument must be an int, not {type(integer).__name__!r}')
        if integer < 0:
            raise ValueException('input must be >= 0')
        res = deque()
        while integer > 0:
            integer, remainder = divmod(integer - 1, self.base)
            res.appendleft(self.alphabet[remainder])
        return ''.join(res)

    def counting(self, __lambda: bool = False, /) -> Generator[str, None, None]:
        """ :param __lambda: when set to true yields the empty string first """

        def counting_util():
            yield from self.alphabet
            yield from (a + b for a in counting_util() for b in self.alphabet)

        if __lambda: yield ''
        yield from counting_util()

    def increment(self, numerals: str) -> str:
        if not isinstance(numerals, str):
            raise TypeException(
                f'BijectiveNumeration.increment() argument must be a string, not {type(numerals).__name__!r}')

        res = []
        first_num, last_num = self.alphabet[0], self.alphabet[-1]
        for index in range(len(numerals) - 1, -1, -1):
            num = numerals[index]
            if num != last_num:
                try:
                    return '%s%s%s' % (numerals[:index], self.alphabet[self.table[num]], ''.join(res))
                except KeyError as err:
                    raise ValueException(f'numeral {err} not found in alphabet: {self.alphabet!r}') from None
            res.append(first_num)
        return '%s%s' % (''.join(res), first_num)

    # TODO: vvvv

    def decrement(self, numerals: str) -> str:
        # temp = ""
        #   for (let i = input.length - 1; i > -1; i--) {
        #     if (input[i] !== "A") {
        #       temp = String.fromCharCode(input.charCodeAt(i) - 1) + temp;
        #       input = input.slice(0, i) + temp;
        #       return input;
        #     }
        #     temp += "Z";
        #   }
        #   return input === "A" ? "A" : temp.slice(0, temp.length - 1);
        # }
        raise NotImplementedError

    # https://github.com/istareatscreens/bb26-spreadsheet/blob/master/src/bb26Compare.ts
    # https://github.com/istareatscreens/bb26-spreadsheet/blob/master/src/bb26Random.ts
    # https://github.com/istareatscreens/bb26-spreadsheet/blob/master/src/bb26Range.ts -> ./generators.py

    # TODO: ^^^^


def bijective_numeration(alphabet: str) -> BijectiveNumeration:
    """ :returns: BijectiveNumeration-object with given alphabet """
    return BijectiveNumeration(
        alphabet,
        len(alphabet),
        {num: val for val, num in enumerate(alphabet, 1)}
    )


# Base-K Bijective Numeration
# ---------------------------
# uses the digit-set {1, 2, ..., k} (k ≥ 1) to uniquely represent every non-negative integer, as follows:
# The integer zero is represented by the empty string
BijectiveBase1 = bijective_numeration('1')
BijectiveBase2 = bijective_numeration('12')
BijectiveBase3 = bijective_numeration('123')
BijectiveBase8 = bijective_numeration('12345678')
# Bijective Base-10 System: https://en.wikipedia.org/wiki/Bijective_numeration#The_bijective_base-10_system
BijectiveBase10 = bijective_numeration('123456789A')
BijectiveBase12 = bijective_numeration('123456789ABC')
BijectiveBase16 = bijective_numeration('123456789ABCDEFG')

# Bijective Base-26 System: https://en.wikipedia.org/wiki/Bijective_numeration#The_bijective_base-26_system
BijectiveBase26 = bijective_numeration('ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def doctests() -> None:
    """
    >>> BijectiveBase2.to_int('1')
    1
    >>> BijectiveBase2.to_int('2')
    2
    >>> BijectiveBase2.to_int('121')
    9
    >>> BijectiveBase2.to_int('2221211112112111112')
    1000000

    >>> BijectiveBase26.to_int('ABC')
    731
    >>> BijectiveBase26.to_int('XFD')
    16384
    >>> BijectiveBase26.to_int('B4B')
    Traceback (most recent call last):
    BijectiveNumerationValueException: numeral '4' not found in alphabet: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


    >>> BijectiveBase2.to_bijective(0)
    ''
    >>> BijectiveBase2.to_bijective(1)
    '1'
    >>> BijectiveBase2.to_bijective(2)
    '2'
    >>> BijectiveBase2.to_bijective(9)
    '121'
    >>> BijectiveBase2.to_bijective(1000000)
    '2221211112112111112'

    >>> BijectiveBase26.to_bijective(731)
    'ABC'
    >>> BijectiveBase26.to_bijective(16384)  # 2^14
    'XFD'
    >>> BijectiveBase26.to_bijective(0)
    ''
    >>> BijectiveBase26.to_bijective(-1)
    Traceback (most recent call last):
    BijectiveNumerationValueException: input must be >= 0


    >>> from utils.more_itertools import nth

    >>> g = BijectiveBase26.counting(True)
    >>> [next(g) for _ in range(5)]
    ['', 'A', 'B', 'C', 'D']

    >>> g = BijectiveBase26.counting()

    >>> next(g), next(g), next(g), nth(g, 22), next(g), next(g), nth(g, 23), next(g), nth(g, 648), next(g)
    ('A', 'B', 'C', 'Z', 'AA', 'AB', 'AZ', 'BA', 'ZZ', 'AAA')

    >>> nth(BijectiveBase26.counting(True), 2 ** 14)
    'XFD'


    >>> BijectiveBase26.increment('A')
    'B'
    >>> BijectiveBase26.increment('Z')
    'AA'
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()
