"""
SoftDes in-class exercise: Going Beyond #1
"""

from geometry import Rect


class Circle(object):
    def __init__(self, x, y, r):
        pass

    def radius(self):
        pass

    def diameter(self):
        pass

    def area(self):
        pass

    def contains_pt(self, x, y):
        pass


def stochastic_area(shape):
    """Use the `random` module and `shape.bbox()` to return an approximate measure of shape's area.

    Arguments
    ---------
    shape: a Circle or Rect

    Returns
    -------
    float
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
