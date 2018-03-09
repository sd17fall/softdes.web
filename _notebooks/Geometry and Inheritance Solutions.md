---
date: 2018-03-05T23:47:27-05:00
source: notebooks/Geometry and Inheritance Solutions.ipynb
---

{% include toc %}


# Inheritance Example: 2D Geometry (Solutions)

The classes below represent simple 2D shapes.

1.  Simplify the code using inheritance.  You can either cut-and-paste the code  and modify it in the cell below, or modify the original code.


```python
from math import sqrt

class Polygon(object):
    """ Represents a polygon in 2D """
    def __init__(self, vertices):
        """ Initialize a polygon from a list of vertices, where each
            vertex is represented as an (x, y) tuple.
            
            vertices: the vertices of the polygone (note: vertices
                      are assumed to be in counterclockwise order) """
        self.vertices = vertices
    
    def get_area(self):
        """
        >>> Polygon([(0, 0), (200, 0), (200, 300), (0, 300)]).get_area()
        60000.0
        """
        # Using formula from http://mathworld.wolfram.com/PolygonArea.html
        area = 0.0
        for i, v_i in enumerate(self.vertices):
            v_i_plus_1 = self.vertices[(i+1) % len(self.vertices)]
            area += 0.5*(v_i[0]*v_i_plus_1[1] - v_i[1]*v_i_plus_1[0])
        return area

    def get_side_lengths(self):
        """ Returns a list of all the side lengths in the Polygon
        
        >>> Polygon([(0, 0), (200, 0), (200, 300), (0, 300)]).get_side_lengths()
        [200.0, 300.0, 200.0, 300.0]
        """
        side_lengths = []
        for i, v_i in enumerate(self.vertices):
            v_i_plus_1 = self.vertices[(i+1) % len(self.vertices)]
            # calculate side_length using the Pythagorean theorem
            side_length = sqrt((v_i[0] - v_i_plus_1[0])**2 + (v_i[1] - v_i_plus_1[1])**2)
            side_lengths.append(side_length)
        return side_lengths
    
class Rectangle(Polygon):
    """ Represents a rectangle in 2D
    
        >>> Rectangle(3, 5, 100, 20).get_area()
        2000.0
    """

    def __init__(self, x1, y1, width, height):
        """ Initialize a rectangle from the upper left corner vertex and
            its width and height.
            
            x1: x-coordinate of the upper left corner of the rectangle
            y1: y-coordinate of the upper left corner of the rectangle
            width: width of the rectangle
            height: height of the rectangle
        """
        super().__init__([(x1, y1), (x1 + width, y1), (x1 + width, y1 + height), (x1, y1 + height)])

class Triangle(Polygon):
    """ Represents a triangle in 2D

        >>> Triangle(0.0, 0.0, 10.0, 0.0, 0.0, 5.0).get_area()
        25.0
    """

    def __init__(self, x1, y1, x2, y2, x3, y3):
        """ Initialize a triangle from its three vertices.  The vertices
            are assumed to be in counterclockwise order.
            
            x1: x-coordinate of the first vertex of the triangle
            y1: y-coordinate of the first vertex of the triangle
            x2: x-coordinate of the second vertex of the triangle
            y2: y-coordinate of the second vertex of the triangle
            x3: x-coordinate of the third vertex of the triangle
            y3: y-coordinate of the third vertex of the triangle
        """
        super().__init__([(x1, y1), (x2, y2), (x3, y3)])

class Square(Rectangle):
    """ Represents a square in 2D

        >>> Square(1.0, 3.0, 50.0).get_area()
        2500.0
    """

    def __init__(self, x1, y1, side_length):
        """ Initialize a square from the upper left corner vertex and
            its side length.
            
            x1: x-coordinate of the upper left corner of the rectangle
            y1: y-coordinate of the upper left corner of the rectangle
            side_length: side length of the square
        """
        super().__init__(x1, y1, side_length, side_length)


import doctest
doctest.testmod()
```

{: class="nb-output"}




    TestResults(failed=0, attempted=5)




<ol start="2">
<li>Create a right triangle class (make sure to use inheritance!)</li>
<li>Add a function called `get_hypotenuse_length` to your right triangle class.</li>
</ol>


```python
class RightTriangle(Triangle):
    """
    Represents a right triangle in 2D
    
    Note: the __init__ method takes three vertices (just like for the normal Triangle class),
          however, in this class we check to make sure the vertices actually represent
          a right triangle.

    >>> RightTriangle(0, 0, 3, 0, 0, 4).get_hypotenuse_length()
    5.0
    """
    def __init__(self, x1, y1, x2, y2, x3, y3):
        super().__init__(x1, y1, x2, y2, x3, y3)
        l = self.get_side_lengths()

        # make sure it's a right triangle by seeing if the Pythagorean theorem is satisfied
        if (l[0]**2 != l[1]**2 + l[2]**2 and
            l[1]**2 != l[0]**2 + l[2]**2 and
            l[2]**2 != l[0]**2 + l[1]**2):
            raise ValueError('The specified triangle is not a right triangle')
    
    def get_hypotenuse_length(self):
        return max(self.get_side_lengths())

doctest.testmod()
```

{: class="nb-output"}




    TestResults(failed=0, attempted=6)



