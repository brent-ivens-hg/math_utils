"""
Sequences
"""
from collections.abc import Generator, Sequence
from itertools import count, product
# LOCAL #
from math_utils.numeral_systems.base36 import BASE36, convert

# --- FINITE --- #

# A005188
NARCISSISTIC = 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 548834, 1741725, 4210818, 9800817, 9926315, 24678050, 24678051, 88593477, 146511208, 472335975, 534494836, 912985153, 4679307774, 32164049650, 32164049651, 40028394225, 42678290603, 44708635679, 49388550606, 82693916578, 94204591914, 28116440335967, 4338281769391370, 4338281769391371, 21897142587612075, 35641594208964132, 35875699062250035, 1517841543307505039, 3289582984443187032, 4498128791164624869, 4929273885928088826, 63105425988599693916, 128468643043731391252, 449177399146038697307, 21887696841122916288858, 27879694893054074471405, 27907865009977052567814, 28361281321319229463398, 35452590104031691935943, 174088005938065293023722, 188451485447897896036875, 239313664430041569350093, 1550475334214501539088894, 1553242162893771850669378, 3706907995955475988644380, 3706907995955475988644381, 4422095118095899619457938, 121204998563613372405438066, 121270696006801314328439376, 128851796696487777842012787, 174650464499531377631639254, 177265453171792792366489765, 14607640612971980372614873089, 19008174136254279995012734740, 19008174136254279995012734741, 23866716435523975980390369295, 1145037275765491025924292050346, 1927890457142960697580636236639, 2309092682616190307509695338915, 17333509997782249308725103962772, 186709961001538790100634132976990, 186709961001538790100634132976991, 1122763285329372541592822900204593, 12639369517103790328947807201478392, 12679937780272278566303885594196922, 1219167219625434121569735803609966019, 12815792078366059955099770545296129367, 115132219018763992565095597973971522400, 115132219018763992565095597973971522401


# -- INFINITE -- #


class SequenceException(Exception): pass


def numbers(base: int = 10) -> Generator[str, None, None]:
    """
    >>> hexadecimals = numbers(16)
    >>> [next(hexadecimals) for _ in range(20)]
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', '10', '11', '12', '13']
    """
    digits = BASE36[:base]
    zero, non_zero = digits[:1], digits[1:]
    yield zero
    yield from ('%s%s' % (head, ''.join(tail))
                for n in count()
                for head in non_zero
                for tail in product(digits, repeat=n))


def palindromic(base: int = 10) -> Generator[str, None, None]:  # todo: use numbers() instead of convert()
    """
    Yields Numbers That Are Palindromic In Given Base

    * base  2: A006995
    * base  3: A014190
    * base  4: A014192
    * base  5: A029952
    * base  6: A029953
    * base  7: A029954
    * base  8: A029803
    * base  9: A029955
    * base 10: A002113
    * base 11: A029956
    * base 12: A029957
    * base 13: A029958
    * base 14: A029959
    * base 15: A029960
    * base 16: A029730
    """
    if not 2 <= base <= 36: raise SequenceException('base must be >= 2 and <= 36')
    yield '0'
    for digits in count(1):
        start = base ** ((digits - 1) // 2)
        odd_length = digits % 2
        for half in map(str, range(start, base * start)):
            half = convert(str(half), 10, base)
            yield half + half[~odd_length::-1]


def somos(seed: Sequence) -> Generator[int, None, None]:
    """
    https://en.wikipedia.org/wiki/Somos_sequence

    >>> take = lambda n, it: [next(it) for _ in range(n)]
    >>> take(15, somos([1] * 4))                                                # Somos-4 Sequence: A006720
    [1, 1, 1, 1, 2, 3, 7, 23, 59, 314, 1529, 8209, 83313, 620297, 7869898]
    >>> take(16, somos([1] * 5))                                                # Somos-5 Sequence: A006721
    [1, 1, 1, 1, 1, 2, 3, 5, 11, 37, 83, 274, 1217, 6161, 22833, 165713]
    >>> take(16, somos([1] * 6))                                                # Somos-6 Sequence: A006722
    [1, 1, 1, 1, 1, 1, 3, 5, 9, 23, 75, 421, 1103, 5047, 41783, 281527]
    >>> take(17, somos([1] * 7))                                                # Somos-7 Sequence: A006723
    [1, 1, 1, 1, 1, 1, 1, 3, 5, 9, 17, 41, 137, 769, 1925, 7203, 34081]
    """
    yield from seed
    a = seed[:]
    k = len(a)
    for n in count(k):
        a.append(sum(a[n - j] * a[n - (k - j)] for j in range(1, k // 2 + 1)) // a[n - k])
        yield a[n]


if __name__ == '__main__':
    import doctest

    doctest.testmod()
