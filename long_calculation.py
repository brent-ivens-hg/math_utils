"""
Long Calculation
"""


# noinspection PyShadowingBuiltins
def long_division(dividend: int, divisor: int) -> tuple:
    """
    Long Division

    >>> print(long_division(5,3))
     5 | 3 = 1 R 2
    -3
     -
     2
     =
    (1, 2)
    >>> print(long_division(8764, 4))
     8764 | 4 = 2191 R 0
    -8
     -
     07
     -4
      -
      36
     -36
      --
       04
       -4
        -
        0
        =
    (2191, 0)
    """
    if divisor > dividend:
        return 0, dividend

    dividend = str(dividend)
    quotient = remainder = ''
    steps = []

    for i in range(1, len(dividend) + 1):
        num = int(remainder + dividend[i - 1:i])
        sum = multiple = 0
        while sum + divisor <= num:
            sum += divisor
            multiple += 1

        quotient += str(multiple)
        remainder = str(num - sum)

        if sum > 0:
            sum_length = len(str(sum))
            steps.append(' ' * (i - sum_length) + f'-{sum}')
            steps.append(' ' * (i + 1 - sum_length) + '-' * sum_length)
            steps.append(' ' * (i + 1 - len(remainder)) + remainder + dividend[i:i + 1])

    steps.append(' ' * (len(dividend) - len(remainder) + 1) + '=' * len(remainder))
    print(f' {dividend} | {divisor} = {(int(quotient))} R {remainder}\n' + '\n'.join(steps))
    return int(quotient), int(remainder)


def long_multiplication(multiplicand: int, multiplier: int) -> int:
    """
    https://en.wikipedia.org/wiki/Multiplication_algorithm#Long_multiplication
    """
    multiplicand, multiplier = str(multiplicand), str(multiplier)
    for a in multiplier:
        for b in multiplicand:
            pass
    return -1


def abacus():
    ...


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    # long_division(4536, 216)
    # long_division(305_753, 31)
    # print(long_multiplication(23_958_233, 5_830))
