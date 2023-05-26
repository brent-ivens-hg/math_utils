"""
Sierpinski
"""
from functools import cache
from pprint import pprint


def triangle(n: int) -> list[list[int]]:  # TODO: implement me
    """disable Docstring"""
    """
    >>> pprint(triangle(0))
    [[1]]
    >>> pprint(triangle(1))
    [[1],
     [1, 0, 1]])
    >>> pprint(triangle(2))
    [[1],
     [1, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 1, 0, 1, 0, 1]]
    >>> pprint(triangle(3))
    [[1],
     [1, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 0, 1, 0, 1, 0, 1],
     [1, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
     [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]]
    """
    if n < 1: return [[1]]
    raise NotImplementedError


@cache
def in_carpet(i: int, j: int) -> bool:
    if i == 0 or j == 0:    return True
    if i % 3 == 1 == j % 3: return False
    return in_carpet(i // 3, j // 3)


@cache
def carpet(n: int) -> list[list[int]]:
    """
    equivalent to `return [[int(in_carpet(i, j)) for j in range(3 ** n)] for i in range(3 ** n)]`

    :returns: sierpinski carpet in matrix form

    >>> pprint(carpet(0))
    [[1]]
    >>> pprint(carpet(1))
    [[1, 1, 1],
     [1, 0, 1], [1, 1, 1]]
    >>> pprint(carpet(2))
    [[1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 1, 1, 0, 1, 1, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 0, 0, 0, 1, 1, 1],
     [1, 0, 1, 0, 0, 0, 1, 0, 1],
     [1, 1, 1, 0, 0, 0, 1, 1, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 0, 1, 1, 0, 1, 1, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 1, 1]]
    """
    if n < 1: return [[1]]
    mat = carpet(n - 1)
    y = [0] * len(mat[0])
    return (
            [x + x + x for x in mat] +
            [x + y + x for x in mat] +
            [x + x + x for x in mat]
    )


# https://en.wikipedia.org/wiki/Sierpi%C5%84ski_curve

# ' __ '
# '/  \'

# '   __   '
# '  /  \  '
# '  \  /  '
# '__/  \__'

# '       __       '
# '      /  \      '
# '      \  /      '
# '    __/  \__    '
# '   /        \   '
# '   \__    __/   '
# ' __   \  /   __ '
# '/  \__/  \__/  \'


# '               __               '
# '              /  \              '
# '              \  /              '
# '            __/  \__            '
# '           /        \           '
# '           \__    __/           '
# '         __   \  /   __         '
# '        /  \__/  \__/  \        '
# '        \              /        '
# '      __/              \__      '
# '     /   __          __   \     '
# '     \__/  \        /  \__/     '
# '   __      /        \      __   '
# '  /  \     \__    __/     /  \  '
# '  \  /   __   \  /   __   \  /  '
# '__/  \__/  \__/  \__/  \__/  \__'


if __name__ == '__main__':
    import doctest

    doctest.testmod()
