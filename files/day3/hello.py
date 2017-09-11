import doctest

def is_triangle(a, b, c):
    """Return true iff these are the sides of a triangle.

    Examples:
    >>> is_triangle(1, 3, 5)
    False
    >>> is_triangle(3, 4, 5)
    True
    >>> is_triangle(1, 1, 2)
    True
    """
    return a <= b + c and b <= a + c and c <= a + b

print(is_triangle(1, 1, 2))

if __name__ == '__main__':
    doctest.testmod()
