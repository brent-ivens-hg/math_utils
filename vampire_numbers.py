from math import sqrt
from collections import Counter
from itertools import permutations, product
from functools import reduce
from operator import mul


def has_fangs(n: int) -> bool:
    s = str(n)
    for digits in map(''.join, permutations(s)):
        m = len(digits) // 2
        x, y = digits[:m], digits[m:]
        if x[-1] == '0' == y[-1]: continue
        if int(x) * int(y) == int(s): return True
    return False


def is_vampire(n: int) -> bool:
    return len(str(n)) % 2 == 0 and has_fangs(n)


print(', '.join(map(str, filter(is_vampire, range(16000)))))


def factors(n):
    """
    return the prime factors for n
    >>> factors(600)
    [5, 5, 3, 2, 2, 2]
    >>> factors(1000)
    [5, 5, 5, 2, 2, 2]
    >>>
    """
    step = lambda x: 1 + x * 4 - (x // 2) * 2
    max_q = int(sqrt(n))
    d = 1
    q = n % 2 == 0 and 2 or 3
    while q <= max_q and n % q != 0:
        q = step(d)
        d += 1
    res = []
    if q <= max_q:
        res.extend(factors(n // q))
        res.extend(factors(q))
    else:
        res = [n]
    return res


def pfm(n):
    """
    return the prime factors and their multiplicities for n
    >>> pfm(600)
    dict_items([(5, 2), (3, 1), (2, 3)])
    >>> pfm(1000)
    dict_items([(5, 3), (2, 3)])
    >>>
    """
    return Counter(factors(n)).items()


def divisors(n):
    """Returns all the divisors of n"""
    factors = pfm(n)
    primes, max_powers = zip(*factors)
    power_ranges = (range(m + 1) for m in max_powers)
    powers = product(*power_ranges)
    return [
        reduce(mul, (prime ** power for prime, power in zip(primes, power_group)))
        for power_group in powers
    ]


def vampire(n):
    fangs = set(frozenset([d, n // d])
                for d in divisors(n)
                if (len(str(d)) == len(str(n)) / 2.
                    and sorted(str(d) + str(n // d)) == sorted(str(n))
                    and (str(d)[-1] == 0) + (str(n // d)[-1] == 0) <= 1))
    return sorted(map(sorted, fangs))


if __name__ == '__main__':
    print('First 25 vampire numbers')
    count = n = 0
    while count < 25:
        n += 1
        fangpairs = vampire(n)
        if fangpairs:
            count += 1
            print('%i: %r' % (n, fangpairs))
    print('\nSpecific checks for fangpairs')
    for n in (16758243290880, 24959017348650, 14593825548650):
        fangpairs = vampire(n)
        print('%i: %r' % (n, fangpairs))
